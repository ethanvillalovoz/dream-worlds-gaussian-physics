#!/usr/bin/env python3
"""Validate the repository's static research artifacts without requiring CUDA."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "gaussian_splatting_physics.ipynb"

REQUIRED_FILES = [
    NOTEBOOK,
    ROOT / "paper" / "dream-worlds-technical-report.pdf",
    ROOT / "assets" / "demos" / "experimental-results.mp4",
    ROOT / "assets" / "demos" / "wall_smash.mp4",
    ROOT / "assets" / "demos" / "mass_falling.mp4",
    ROOT / "assets" / "demos" / "wind_field.mp4",
    ROOT / "assets" / "demos" / "wind_field_low.mp4",
    ROOT / "assets" / "demos" / "wind_field_high.mp4",
]

EXPECTED_EXPERIMENT_MARKERS = [
    "Experiment 1: Uniform Gravity",
    "Experiment 2: Randomized Inverse-Mass Motion",
    "Experiment 3: Wind Field Deformation",
    "Experiment 4: Wind Strength Ablation",
    "wind_scale = 0.1",
    "wind_scale = 4.0",
]

EXPECTED_PREVIEW_COUNTS = {
    "uniform-gravity": 5,
    "inverse-mass": 5,
    "wind-low": 5,
    "wind-medium": 5,
    "wind-high": 5,
}

MARKDOWN_TARGET = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_TARGET = re.compile(r'(?:href|src)="([^"]+)"')


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required_files() -> None:
    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}")
        if path.stat().st_size == 0:
            fail(f"required file is empty: {path.relative_to(ROOT)}")

    report = ROOT / "paper" / "dream-worlds-technical-report.pdf"
    if not report.read_bytes().startswith(b"%PDF-"):
        fail("technical report does not have a PDF header")


def validate_notebook() -> None:
    try:
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot parse notebook: {error}")

    if notebook.get("nbformat") != 4:
        fail("notebook must use nbformat 4")

    cells = notebook.get("cells", [])
    if len(cells) != 24:
        fail(f"expected 24 notebook cells, found {len(cells)}")

    text = "\n".join("".join(cell.get("source", [])) for cell in cells)
    for marker in EXPECTED_EXPERIMENT_MARKERS:
        if marker not in text:
            fail(f"notebook is missing experiment marker: {marker}")

    for index, cell in enumerate(cells, start=1):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("execution_count") is not None:
            fail(f"code cell {index} has a committed execution count")
        if cell.get("outputs", []):
            fail(f"code cell {index} has committed outputs")


def validate_previews() -> None:
    preview_root = ROOT / "assets" / "previews"
    for experiment, expected_count in EXPECTED_PREVIEW_COUNTS.items():
        files = sorted((preview_root / experiment).glob("*.png"))
        if len(files) != expected_count:
            fail(
                f"expected {expected_count} previews for {experiment}, "
                f"found {len(files)}"
            )
        for path in files:
            if path.stat().st_size == 0:
                fail(f"preview is empty: {path.relative_to(ROOT)}")


def validate_markdown_links() -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        content = markdown.read_text(encoding="utf-8")
        targets = MARKDOWN_TARGET.findall(content) + HTML_TARGET.findall(content)
        for target in targets:
            target = target.strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            local_target = target.split("#", 1)[0]
            if not local_target:
                continue
            resolved = (markdown.parent / local_target).resolve()
            if not resolved.exists():
                fail(
                    f"broken local link in {markdown.relative_to(ROOT)}: {target}"
                )


def main() -> None:
    validate_required_files()
    validate_notebook()
    validate_previews()
    validate_markdown_links()
    print("Repository validation passed.")
    print("- notebook: 24 cells, 4 experiment sections, outputs cleared")
    print("- demos: 6 archived MP4 files")
    print("- previews: 25 report-aligned PNG frames")
    print("- paper: valid PDF header")
    print("- Markdown: local links resolve")


if __name__ == "__main__":
    main()
