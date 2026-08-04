<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7FB79B,60:9BC4CF,100:E4A0B7&height=190&section=header&text=Jin%20Lei&fontSize=58&fontColor=ffffff&fontAlignY=36&animation=fadeIn&desc=Nuclear%20Reaction%20Theory%20%C2%B7%20Tongji%20University&descAlignY=57&descSize=17" width="100%" alt="Jin Lei" />

<a href="https://jinlei.fewbody.com">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=19&duration=4000&pause=900&color=7FB79B&center=true&vCenter=true&width=720&height=45&lines=Why+do+weakly+bound+nuclei+break+up+the+way+they+do%3F;What+can+elastic+scattering+really+tell+us+about+the+potential%3F;Making+reaction+theory+fast+enough+to+do+inference+on." alt="research questions" />
</a>

<br/>

<a href="https://jinlei.fewbody.com"><img src="https://img.shields.io/badge/Website-jinlei.fewbody.com-7FB79B?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" /></a>
<a href="https://orcid.org/0000-0002-2323-2061"><img src="https://img.shields.io/badge/ORCID-0000--0002--2323--2061-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" /></a>
<a href="https://scholar.google.com/citations?user=ft9l8c8AAAAJ&hl=en"><img src="https://img.shields.io/badge/Scholar-Citations-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar" /></a>
<a href="https://inspirehep.net/authors/1671469"><img src="https://img.shields.io/badge/INSPIRE--HEP-Profile-B31B1B?style=for-the-badge&logo=arxiv&logoColor=white" alt="INSPIRE-HEP" /></a>
<a href="mailto:jinl@tongji.edu.cn"><img src="https://img.shields.io/badge/Email-jinl%40tongji.edu.cn-E4A0B7?style=for-the-badge&logo=maildotru&logoColor=white" alt="Email" /></a>

<br/>

<img src="https://img.shields.io/badge/Fortran-734F96?style=flat-square&logo=fortran&logoColor=white" alt="Fortran" />
<img src="https://img.shields.io/badge/Julia-9558B2?style=flat-square&logo=julia&logoColor=white" alt="Julia" />
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/JAX-D34F1E?style=flat-square&logo=google&logoColor=white" alt="JAX" />
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
<img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA" />
<img src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white" alt="LaTeX" />

<img src="https://komarev.com/ghpvc/?username=jinleiphys&style=flat-square&color=7FB79B&label=profile+views" alt="profile views" />

</div>

---

## About

I am a professor in the Department of Physics at Tongji University, working on the theory of
direct nuclear reactions. Most of my work starts from one question: when a loosely bound nucleus
hits a target, where does the flux actually go, and which part of that can we hope to measure?

That question has taken me through the Ichimura-Austern-Vincent formalism for inclusive breakup,
coupled-channel descriptions of the continuum, and more recently into what a measurement can and
cannot constrain at all. Elastic scattering, it turns out, pins down far fewer directions in
optical-potential space than the number of parameters we routinely fit. Chasing that has pulled
me into emulators, differentiable solvers, and Bayesian inference, not because the machine
learning is interesting on its own, but because the physics question needs calculations that are
cheap enough to repeat a million times.

I write most of my own solvers. They are listed below.

<details>
<summary><b>Background</b></summary>

<br/>

| Period | Where | With |
|---|---|---|
| 2020 - now | Tongji University, Shanghai | Professor, NSFC PI |
| 2026 - 2027 | SCNT, Institute of Modern Physics, CAS, Huizhou | Visiting Scientist |
| 2019 - 2020 | INFN Pisa | Postdoc, A. Bonaccorso |
| 2016 - 2019 | Ohio University | Postdoc, Ch. Elster |
| 2014 - 2016 | Universidad de Sevilla | PhD, A. M. Moro |

</details>

---

## Research lines

| | Line | What it is about |
|---|---|---|
| **A** | Inclusive breakup and incomplete fusion | The IAV formalism: post-prior equivalence, IAV-CDCC, why complete fusion looks suppressed. Complete fusion suppression is a Trojan Horse effect, and incomplete fusion is one-step direct capture. |
| **B** | Reduction methods and threshold anomaly | Universal reduced excitation functions across ~127 systems. Later shown by bootstrap UQ to be partly a precision artifact. Frozen. |
| **C** | Few-body universality | Faddeev-AGS calculations of three-body halos. <sup>6</sup>Li behaves as a deuteron halo. |
| **D** | Statistical inference and information geometry | How much information a measurement actually carries. Fisher-matrix limits on optical-potential extraction, Bayesian calibration of coupled-channel models, and whether chiral EFT respects its own power counting. |
| **E** | Bound-state techniques and scattering emulators | Making scattering solvable in an L<sup>2</sup> basis, then making it fast: direct boundary matching, reduced-basis emulation, physics-informed networks. |
| **F** | Coupled-channel absorption mechanisms | Exact flux decompositions of coupled-channel absorption, the Feshbach dynamic polarization potential built without the weak-coupling approximation, and a uniqueness proof for the coupled-channel Green's function. |

---

## Codes

Everything here I wrote or co-wrote. Where a code was released with a paper, the paper is the
reference to cite.

| Code | Language | What it does | Released with |
|---|---|---|---|
| [**SLAM.jl**](https://github.com/jinleiphys/SLAM.jl) | Julia | General scattering solver on a Lagrange-Legendre basis, direct boundary matching, built to be emulated | [PRC **113**, 024614](https://doi.org/10.1103/ddcx-cslb) |
| [**swift.jl**](https://github.com/jinleiphys/swift.jl) | Julia | Three-body Faddeev solver, AV18 / AV14 / Nijmegen with UIX; <sup>3</sup>H bound state and Nd scattering with Coulomb and complex scaling | in progress |
| [**HPRMAT**](https://github.com/jinleiphys/HPRMAT) | Fortran + CUDA | High-performance R-matrix linear algebra: direct LU, mixed precision, multi-GPU. 18x speedup at N = 25600 on a single RTX 3090 | CPC, in press |
| [**COLOSS**](https://github.com/jinleiphys/COLOSS) | Fortran | Complex-scaled two-body scattering with local and Perey-Buck nonlocal optical potentials | [CPC **311**, 109568](https://doi.org/10.1016/j.cpc.2025.109568) |
| [**inhomoR**](https://github.com/jinleiphys/inhomoR) | Fortran | Lagrange-mesh R-matrix solver for inhomogeneous equations, with Vincent-Fortune contour integration | [PRC **102**, 014608](https://doi.org/10.1103/PhysRevC.102.014608) |
| [**opticalfisher**](https://github.com/jinleiphys/opticalfisher) | Python | Fisher-information analysis of what elastic scattering constrains in the optical potential | in review |
| [**fresco_gui**](https://github.com/jinleiphys/fresco_gui) | Fortran | A usable front end for building FRESCO input decks | - |

Some production codes are not public and are available on request:

| Code | Language | What it does | Reference |
|---|---|---|---|
| **smoothie** | Fortran 95 | Production IAV-DWBA and IAV-CDCC nonelastic breakup, the daily driver behind most of Line A | [PRL **123**, 232501](https://doi.org/10.1103/PhysRevLett.123.232501) |
| **PINN-ECS** | Python / JAX | Physics-informed network for scattering with an exterior-complex-scaling boundary | [PRC **113**, 064618](https://doi.org/10.1103/sjz4-pq6p) |
| **BiLNN** | PyTorch | Bidirectional liquid neural network mapping the KD02 optical potential to scattering wave functions, differentiable and global over 1-200 MeV | [PRC **114**, 014620](https://doi.org/10.1103/qw54-df4l) |
| **transfer** | Fortran 95 | DWBA and IAV transfer engine, carries the phase-equivalent nonlocality machinery | in review |
| **STARS** | Fortran + CUDA | GPU coupled-channels and CDCC production code with a Fortran-side reduced-basis emulator | - |

---

## Selected work

<details open>
<summary><b>Recent</b></summary>

<br/>

- **Inclusive breakup with nonspectator fragments: generalization of the IAV sum rules**
  *Phys. Rev. C* **114**, 014632 (2026) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/rbph-64rs) &nbsp;·&nbsp; [arXiv:2604.11226](https://arxiv.org/abs/2604.11226)
  Removes the spectator approximation on the detected fragment. Standard IAV turns out to be the total inclusive cross section summed over the fragment's internal states.

- **Reduced basis emulator for elastic scattering in CDCC**
  *Phys. Rev. C* **113**, 044610 (2026) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/n24x-d9gm)
  Proper orthogonal decomposition plus Galerkin projection, 220x faster, sub-0.1% on an 18-parameter problem.

- **Direct boundary matching: a bound-state technique for nuclear scattering**
  *Phys. Rev. C* **113**, 024614 (2026) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/ddcx-cslb)
  Scattering boundary conditions without Bloch operators. Released as SLAM.jl.

- **Exterior complex scaling enables physics-informed neural networks for nuclear reactions**
  *Phys. Rev. C* **113**, 064618 (2026) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/sjz4-pq6p)
  The trick that makes PINNs work here: damp the exterior wave so the optical potential stays on the real axis.

</details>

<details>
<summary><b>Earlier, and still the backbone</b></summary>

<br/>

- **Puzzle of complete fusion suppression in weakly bound nuclei: a Trojan Horse effect?**
  *Phys. Rev. Lett.* **122**, 042503 (2019) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/PhysRevLett.122.042503)

- **Unraveling the reaction mechanisms leading to partial fusion of weakly bound nuclei**
  *Phys. Rev. Lett.* **123**, 232501 (2019) &nbsp;·&nbsp; [doi](https://doi.org/10.1103/PhysRevLett.123.232501)
  First IAV-CDCC calculation. Incomplete fusion is one-step direct capture.

- **Numerical assessment of post-prior equivalence for inclusive breakup reactions**
  *Phys. Rev. C* **92**, 061602(R) (2015), Editor's Suggestion &nbsp;·&nbsp; [doi](https://doi.org/10.1103/PhysRevC.92.061602)
  Closes a thirty-year controversy about the IAV and Udagawa-Tamura formulations.

</details>

Full list on [Google Scholar](https://scholar.google.com/citations?user=ft9l8c8AAAAJ&hl=en) or the [website](https://jinlei.fewbody.com/publications/).

---

## GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinleiphys/jinleiphys/output/profile-card-dark.svg" />
  <img src="https://raw.githubusercontent.com/jinleiphys/jinleiphys/output/profile-card.svg" width="98%" alt="Profile summary" />
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=jinleiphys&hide_border=true&theme=tokyonight&ring=E4A0B7&fire=E4A0B7&currStreakLabel=7FB79B" />
  <img src="https://streak-stats.demolab.com?user=jinleiphys&hide_border=true&theme=graywhite&ring=C77E9B&fire=C77E9B&currStreakLabel=5E9C82" height="165" alt="Streak" />
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=jinleiphys&theme=tokyo-night&hide_border=true&custom_title=Contribution%20activity&line=E4A0B7&point=7FB79B" />
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=jinleiphys&theme=minimal&hide_border=true&custom_title=Contribution%20activity&line=C77E9B&point=5E9C82" width="98%" alt="Activity graph" />
</picture>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/jinleiphys/jinleiphys/output/github-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/jinleiphys/jinleiphys/output/github-snake.svg" width="98%" alt="Contribution snake" />
</picture>

</div>

---

<div align="center">

**Tongji University, Shanghai** &nbsp;·&nbsp; **SCNT / IMP-CAS, Huizhou**

Happy to talk about breakup reactions, optical potentials, emulators, or anything
in the codes above. Students and visitors welcome.

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:E4A0B7,40:9BC4CF,100:7FB79B&height=110&section=footer" width="100%" alt="" />

</div>

<!-- profile -->

<!-- re-register -->
