# Contributing

Thanks for your interest in Dream Worlds. This repository preserves a completed course research project while welcoming focused improvements to documentation, reproducibility, and clearly scoped bug fixes.

## Before opening a change

- Read the [project scope](README.md#scope-and-limitations) and [third-party notices](THIRD_PARTY_NOTICES.md).
- Keep the original experiment definitions and archived results intact unless a proposed behavioral change is discussed first.
- Do not commit pretrained checkpoints, source datasets, generated frame directories, credentials, or machine-specific environment files.
- Open an issue before making a large dependency, algorithm, data-format, or experiment change.

## Local checks

Run the repository validator and whitespace check before opening a pull request:

```bash
python scripts/validate_repository.py
git diff --check
```

Full experiment execution additionally requires the CUDA environment and Ficus checkpoint described in [Reproducibility](docs/REPRODUCIBILITY.md).

## Pull requests

Please explain:

1. What changed and why.
2. Whether notebook behavior or generated outputs changed.
3. Which checks or experiments were run.
4. Whether any new data, images, video, or third-party code was added and under what terms.
