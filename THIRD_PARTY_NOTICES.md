# Third-party notices and asset provenance

This file distinguishes the project's jointly authored work from external software, data, research figures, templates, and course material. A source being publicly accessible does not by itself grant unrestricted reuse.

## Project-authored artifacts

| Paths | Description | Attribution | Evidence class |
|---|---|---|---|
| `notebooks/gaussian_splatting_physics.ipynb` | Course-project experiment notebook | Michael Walker and Ethan Villalovoz | Original project implementation |
| `assets/demos/experimental-results.mp4`, `assets/demos/wall_smash.mp4`, `assets/demos/mass_falling.mp4`, `assets/demos/wind_field*.mp4` | Original rendered experiment and comparison videos | Original project team; see `AUTHORS.md` | Archived experimental output |
| `assets/demos/results-comparison.*`, `assets/previews/results-comparison-poster.png` | Labeled synchronized composition of the five original experiment videos | Original project team for experiment footage; Ethan Villalovoz fork maintenance for layout and export | Presentation derivative of archived experimental output; no experiment frames regenerated |
| `assets/previews/**/*.png` | Unmodified frames selected from the original rendered sequences | Original project team; selections match the technical report | Archived experimental output |
| `assets/diagrams/*` | Conceptual vector explanation of the implemented pipeline | Ethan Villalovoz fork maintenance | Derived explanation; not experimental evidence |
| `paper/dream-worlds-technical-report.pdf` | Final course technical report | Michael Walker and Ethan Villalovoz | Original project report |

The rendered artifacts depict a pretrained Ficus Gaussian Splatting scene obtained from the external source described below.

## Gaussian Splatting implementation

- **Dependency:** [`yindaheng98/gaussian-splatting`](https://github.com/yindaheng98/gaussian-splatting), a packaged fork of [`graphdeco-inria/gaussian-splatting`](https://github.com/graphdeco-inria/gaussian-splatting)
- **Use:** Loaded as an external Python dependency; its code is not vendored in this repository.
- **License:** [Gaussian-Splatting License](https://github.com/yindaheng98/gaussian-splatting/blob/master/LICENSE.md), which limits use to non-commercial research and evaluation and requires retention of license and attribution notices when covered work is redistributed.
- **Citation:** Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, and George Drettakis, “3D Gaussian Splatting for Real-Time Radiance Field Rendering,” ACM Transactions on Graphics, 2023.

## Pretrained Ficus scene

- **Source used by the course project:** [Pretrained Sources that work](https://drive.google.com/drive/folders/1Bl51dHBoTt08T3RBtslM93UIIk9C_gSB?usp=sharing)
- **Use:** External `cameras.json` and `point_cloud.ply` inputs expected under `output/ficus_whitebg-trained/`.
- **Distribution:** The checkpoint and source images are not included in this repository. Users retrieve them from the linked source and are responsible for following the source's terms.
- **Derived artifacts:** The repository's PNG previews and MP4 demonstrations are rendered outputs produced from this checkpoint.

## Prior research shown in the report

Figure 1 of the technical report contains images adapted from:

- [PhysGaussian: Physics-Integrated 3D Gaussians for Generative Dynamics](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_PhysGaussian_Physics-Integrated_3D_Gaussians_for_Generative_Dynamics_CVPR_2024_paper.html)
- [GASP: Gaussian Splatting for Physic-Based Simulations](https://arxiv.org/abs/2409.05819)

Those images remain attributed in the report caption and bibliography. The source figures are not separately distributed in this repository.

## Paper template

The report was formatted using the [CVPR 2026 author kit](https://github.com/cvpr-org/author-kit). This repository includes only the compiled project report, not the author-kit source files.

## Course context

- **Course:** [CS 8803 CGAI: Computer Graphics in the AI Era](https://cgai-gatech.vercel.app/)
- **Assignment:** [Final Project: Dream World](https://cgai-gatech.vercel.app/assignment/Final_doc)

Course pages are linked for context and are not redistributed here.

## Project-level license status

The original joint repository did not declare a project-level software license. This fork does not add a new license grant on behalf of both original authors. Unless a governing third-party license says otherwise, the absence of a license means no general permission to copy, modify, or redistribute the jointly authored source is implied.
