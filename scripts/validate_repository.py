#!/usr/bin/env python3
"""Validate the repository's static research artifacts without requiring CUDA."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "gaussian_splatting_physics.ipynb"
METHOD_DIAGRAM = ROOT / "assets" / "diagrams" / "dream-worlds-method.svg"
METHOD_DIAGRAM_PNG = ROOT / "assets" / "diagrams" / "dream-worlds-method.png"
FIGURE_MANIFEST = ROOT / "figures" / "method-overview" / "manifest.json"

REQUIRED_FILES = [
    NOTEBOOK,
    METHOD_DIAGRAM,
    METHOD_DIAGRAM_PNG,
    FIGURE_MANIFEST,
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


def validate_method_diagram() -> None:
    try:
        diagram = ET.parse(METHOD_DIAGRAM).getroot()
    except (OSError, ET.ParseError) as error:
        fail(f"cannot parse method diagram SVG: {error}")

    if not diagram.tag.endswith("svg"):
        fail("method diagram root element is not SVG")

    children = list(diagram)
    if not any(child.tag.endswith("title") for child in children):
        fail("method diagram is missing an accessible title")
    if not any(child.tag.endswith("desc") for child in children):
        fail("method diagram is missing an accessible description")

    try:
        manifest = json.loads(FIGURE_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot parse method figure manifest: {error}")

    if manifest.get("figure_id") != "method-overview":
        fail("method figure manifest has an unexpected figure_id")

    for artifact in manifest.get("inputs", []) + manifest.get("outputs", []):
        path = ROOT / artifact.get("path", "")
        if not path.is_file():
            fail(f"figure manifest references a missing artifact: {path}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != artifact.get("sha256"):
            fail(
                "figure manifest hash mismatch: "
                f"{path.relative_to(ROOT)}"
            )


def validate_environment_contract() -> None:
    environment = (ROOT / "environment.yml").read_text(encoding="utf-8")
    for dependency in ("ffmpeg", "gdown", "ipykernel", "jupyterlab"):
        if not re.search(rf"^\s*-\s*{dependency}\s*$", environment, re.MULTILINE):
            fail(f"environment.yml is missing documented tool: {dependency}")


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
    validate_method_diagram()
    validate_environment_contract()
    validate_markdown_links()
    print("Repository validation passed.")
    print("- notebook: 24 cells, 4 experiment sections, outputs cleared")
    print("- demos: 6 archived MP4 files")
    print("- previews: 25 report-aligned PNG frames")
    print("- method diagram: valid accessible SVG with provenance manifest")
    print("- environment: notebook, download, and export tools declared")
    print("- paper: valid PDF header")
    print("- Markdown: local links resolve")


if __name__ == "__main__":
    main()
