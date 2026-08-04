#!/usr/bin/env python3
"""Generate the profile stat cards as static SVG.

The public github-readme-stats / profile-trophy deployments are dead
(DEPLOYMENT_PAUSED / DEPLOYMENT_DISABLED), so the cards are rendered here from
the GitHub API and committed as plain SVG. No third-party service at read time.

Usage: GITHUB_TOKEN=... python3 scripts/gen_cards.py <user> <outdir>
"""

import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"

# Palette, matching the README header gradient.
THEMES = {
    "": dict(  # light
        bg="#ffffff", border="#d8dee4", title="#C77E9B", label="#57606a",
        value="#24292f", muted="#8b949e", accent="#5E9C82",
    ),
    "-dark": dict(
        bg="#0d1117", border="#30363d", title="#E4A0B7", label="#8b949e",
        value="#e6edf3", muted="#6e7681", accent="#7FB79B",
    ),
}

# Linguist colours for the languages that actually show up here.
LANG_COLOR = {
    "Fortran": "#4d41b1", "Julia": "#a270ba", "Python": "#3572A5",
    "C++": "#f34b7d", "C": "#555555", "Cuda": "#3A4E3A", "TeX": "#3D6117",
    "Shell": "#89e051", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "HTML": "#e34c26", "CSS": "#563d7c", "Vue": "#41b883", "Jupyter Notebook": "#DA5B0B",
    "Makefile": "#427819", "Ren'Py": "#ff7f7f", "Rust": "#dea584", "Java": "#b07219",
    "MATLAB": "#e16737", "Roff": "#ecdebe", "Gnuplot": "#f0a9f0", "Perl": "#0298c3",
}
FALLBACK = ["#7FB79B", "#E4A0B7", "#9BC4CF", "#C9A227", "#B07AA1", "#76B7B2"]


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body, headers={
        "Content-Type": "application/json",
        "User-Agent": "profile-card-generator",
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.load(r)
    if "errors" in out:
        raise RuntimeError(out["errors"])
    return out["data"]


CONTRIB_Q = """
query($login:String!,$from:DateTime!,$to:DateTime!){
  user(login:$login){
    contributionsCollection(from:$from,to:$to){
      contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
    }
  }
}
"""


def contributions(user, start_year):
    """Daily contribution counts from start_year to today, oldest first.

    The calendar query is capped at one year per call, so it is walked year by
    year. streak-stats.demolab.com used to do this, but it is too slow for
    GitHub's camo proxy, which returns 504 and leaves a broken image.
    """
    import datetime as dt
    today = dt.date.today()
    days = {}
    for y in range(start_year, today.year + 1):
        frm = dt.date(y, 1, 1).isoformat() + "T00:00:00Z"
        to = min(dt.date(y, 12, 31), today).isoformat() + "T23:59:59Z"
        data = graphql(CONTRIB_Q, {"login": user, "from": frm, "to": to})
        cal = data["user"]["contributionsCollection"]["contributionCalendar"]
        for w in cal["weeks"]:
            for d in w["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
    return sorted(days.items())


def streaks(days):
    """Total, current and longest streak. Today counts as pending, not broken."""
    import datetime as dt
    today = dt.date.today().isoformat()
    total = sum(c for _, c in days)

    longest = cur = 0
    long_end = cur_start = None
    prev = None
    for date, count in days:
        if count > 0:
            cur = cur + 1 if prev else 1
            if cur == 1:
                cur_start = date
            if cur > longest:
                longest, long_end = cur, date
            prev = True
        else:
            # An empty day today does not break the streak yet.
            if date != today:
                prev = False
                cur = 0
    return {
        "total": total,
        "current": cur,
        "current_start": cur_start,
        "longest": longest,
        "longest_end": long_end,
        "first": days[0][0] if days else None,
    }


def get(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "profile-card-generator",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
           if os.environ.get("GITHUB_TOKEN") else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect(user):
    repos, page = [], 1
    while True:
        batch = get(f"{API}/users/{user}/repos?type=owner&per_page=100&page={page}")
        if not batch:
            break
        repos += batch
        page += 1
    own = [r for r in repos if not r["fork"]]

    # Count repositories by primary language rather than summing bytes. Byte
    # counts are dominated by the vendored assets in the conference and talk
    # sites, which says nothing about what the work actually is.
    langs = {}
    for r in own:
        name = r.get("language")
        if name:
            langs[name] = langs.get(name, 0) + 1

    profile = get(f"{API}/users/{user}")
    return {
        "repos": len(own),
        "stars": sum(r["stargazers_count"] for r in own),
        "followers": profile["followers"],
        "langs": sorted(langs.items(), key=lambda kv: (-kv[1], kv[0])),
    }


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(data, c, top_n=8):
    W, H = 860, 268
    langs = data["langs"][:top_n]
    total = sum(v for _, v in data["langs"]) or 1
    fb = iter(FALLBACK * 4)
    langs = [(n, v, LANG_COLOR.get(n) or next(fb)) for n, v in langs]
    shown = sum(v for _, v, _ in langs)

    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="GitHub profile summary">',
        '<style>'
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}'
        '.t{font-size:17px;font-weight:600}.n{font-size:30px;font-weight:700}'
        '.l{font-size:12px}.k{font-size:12.5px}'
        '</style>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" '
        f'fill="{c["bg"]}" stroke="{c["border"]}"/>',
        f'<text x="32" y="42" class="t" fill="{c["title"]}">GitHub at a glance</text>',
    ]

    # Counters.
    for i, (label, value) in enumerate([
        ("repositories, not forks", data["repos"]),
        ("stars earned", data["stars"]),
        ("followers", data["followers"]),
        ("languages used", len(data["langs"])),
    ]):
        x = 32 + i * 205
        p.append(f'<text x="{x}" y="90" class="n" fill="{c["value"]}">{value}</text>')
        p.append(f'<text x="{x}" y="110" class="l" fill="{c["label"]}">{label}</text>')

    p.append(f'<text x="32" y="152" class="t" fill="{c["title"]}">'
             f'Repositories by primary language</text>')

    # Stacked bar.
    bar_x, bar_w, bar_y = 32, W - 64, 166
    x = float(bar_x)
    p.append(f'<clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" '
             f'height="11" rx="5.5"/></clipPath>')
    p.append('<g clip-path="url(#bar)">')
    p.append(f'<rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="11" fill="{c["border"]}"/>')
    for _, v, col in langs:
        w = bar_w * v / shown
        p.append(f'<rect x="{x:.2f}" y="{bar_y}" width="{w:.2f}" height="11" fill="{col}"/>')
        x += w
    p.append('</g>')

    # Legend, two rows of four. The count sits in a fixed column so a long
    # language name can never collide with it.
    for i, (name, v, col) in enumerate(langs):
        cx = 38 + (i % 4) * 208
        cy = 206 + (i // 4) * 26
        p.append(f'<circle cx="{cx}" cy="{cy-4}" r="5" fill="{col}"/>')
        p.append(f'<text x="{cx+13}" y="{cy}" class="k" fill="{c["value"]}">{esc(name)}</text>')
        p.append(f'<text x="{cx+178}" y="{cy}" class="l" text-anchor="end" '
                 f'fill="{c["muted"]}">{v}</text>')

    p.append('</svg>')
    return "\n".join(p)


def pretty(d):
    import datetime as dt
    if not d:
        return ""
    return dt.date.fromisoformat(d).strftime("%b %-d, %Y")


def render_streak(s, c):
    W, H = 860, 150
    cols = [
        ("Total contributions", f"{s['total']:,}", f"{pretty(s['first'])} to today"),
        ("Current streak", f"{s['current']}", pretty(s["current_start"]) or "-"),
        ("Longest streak", f"{s['longest']}", f"ended {pretty(s['longest_end'])}"),
    ]
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="Contribution streaks">',
        '<style>'
        'text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}'
        '.t{font-size:17px;font-weight:600}.n{font-size:34px;font-weight:700}'
        '.l{font-size:12.5px}.s{font-size:11.5px}'
        '</style>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="10" '
        f'fill="{c["bg"]}" stroke="{c["border"]}"/>',
        f'<text x="32" y="42" class="t" fill="{c["title"]}">Contributions</text>',
    ]
    for i, (label, value, sub) in enumerate(cols):
        x = 32 + i * 274
        if i:
            p.append(f'<line x1="{x-30}" y1="58" x2="{x-30}" y2="126" '
                     f'stroke="{c["border"]}"/>')
        p.append(f'<text x="{x}" y="96" class="n" fill="{c["value"]}">{value}</text>')
        p.append(f'<text x="{x}" y="116" class="l" fill="{c["label"]}">{label}</text>')
        p.append(f'<text x="{x}" y="133" class="s" fill="{c["muted"]}">{esc(sub)}</text>')
    p.append('</svg>')
    return "\n".join(p)


def main():
    user = sys.argv[1] if len(sys.argv) > 1 else "jinleiphys"
    outdir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    os.makedirs(outdir, exist_ok=True)

    data = collect(user)
    start_year = int(get(f"{API}/users/{user}")["created_at"][:4])
    s = streaks(contributions(user, start_year))

    for suffix, colors in THEMES.items():
        for name, svg in [("profile-card", render(data, colors)),
                          ("streak-card", render_streak(s, colors))]:
            path = os.path.join(outdir, f"{name}{suffix}.svg")
            with open(path, "w") as f:
                f.write(svg)
            print("wrote", path)
    print(f"{data['repos']} repos, {data['stars']} stars, "
          f"{data['followers']} followers, {len(data['langs'])} languages")
    print(f"{s['total']} contributions, current streak {s['current']}, "
          f"longest {s['longest']}")


if __name__ == "__main__":
    main()
