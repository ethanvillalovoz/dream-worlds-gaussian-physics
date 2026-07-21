# Reproducibility guide

This guide documents the original execution path without expanding the experimental scope. Full rendering requires an NVIDIA CUDA environment and the external pretrained Ficus checkpoint.

## Expected environment

| Component | Project setting |
|---|---|
| Operating system | Linux or WSL recommended |
| Python | 3.10 |
| CUDA toolkit | 12.8 in `environment.yml` |
| Compiler | GCC 13.4 in `environment.yml` |
| Renderer | Packaged Python fork of 3D Gaussian Splatting |
| Video encoder | FFmpeg with `libx264` |
| Notebook kernel | `gaussian_splatting` |

The renderer builds CUDA extensions during installation. PyTorch must therefore be installed before `requirements.txt`, and its CUDA build must match the local toolkit and driver.

## Installation

```bash
conda env create --file environment.yml -y
conda activate gaussian_splatting

pip install --upgrade wheel setuptools
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
pip install --requirement requirements.txt --no-build-isolation
```

For RTX 50-series / SM 12.0 GPUs:

```bash
export TORCH_CUDA_ARCH_LIST="12.0"
```

Leave this variable unset on other architectures so PyTorch targets the local GPU.

## Pretrained input

Download the external Ficus archive:

```bash
python -m pip install gdown
mkdir -p output
gdown --folder "https://drive.google.com/drive/folders/1Bl51dHBoTt08T3RBtslM93UIIk9C_gSB?usp=sharing" -O output
unzip output/ficus_whitebg-trained.zip -d output
```

Expected minimum layout:

```text
output/ficus_whitebg-trained/
├── cameras.json
└── point_cloud/
    └── iteration_30000/
        └── point_cloud.ply
```

The checkpoint is not committed. See [third-party notices](../THIRD_PARTY_NOTICES.md) for provenance and redistribution boundaries.

## Running experiments

1. Start Jupyter from the repository root.
2. Open `notebooks/gaussian_splatting_physics.ipynb`.
3. Select the `gaussian_splatting` kernel.
4. Run cells from top to bottom.

The simulation cells produce 200 PNG frames per setting. The FFmpeg cells encode each sequence at 60 frames per second into an 8-second MP4.

| Experiment | Frame directory | Video |
|---|---|---|
| Uniform gravity | `wall_smash/` | `wall_smash.mp4` |
| Randomized inverse mass | `mass_falling/` | `mass_falling.mp4` |
| Medium wind | `wind_field/` | `wind_field.mp4` |
| Low wind | `wind_field_low/` | `wind_field_low.mp4` |
| High wind | `wind_field_high/` | `wind_field_high.mp4` |

All frame directories live under `assets/images/ficus_whitebg-trained/images/`. They are ignored by Git because they can be regenerated.

## Static repository validation

The public CI does not claim to reproduce CUDA renders. It performs deterministic checks that are meaningful without the external data or GPU:

```bash
python scripts/validate_repository.py
```

The validator confirms that:

- The notebook is valid JSON with the expected experiment sections.
- Archived notebook outputs and execution counts remain cleared.
- Required MP4s, curated frames, and report files are present and non-empty.
- Local Markdown links resolve to tracked files.

## Reproducibility limitations

- The randomized inverse-mass experiment draws from `torch.rand` without a fixed seed, so rerenders need not exactly match the archived sequence.
- The external checkpoint source is linked rather than versioned in this repository.
- CUDA, PyTorch, compiler, and GPU-generation compatibility can affect installation.
- The project records qualitative results rather than numerical regression targets.
- The combined comparison video is an archived post-processing artifact; the notebook exports the five individual experiment videos.
