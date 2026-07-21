# Demonstration media

The files in this directory are archived outputs from the original course project or presentation-only derivatives made from those outputs. They are qualitative evidence from one pretrained Ficus scene, not a claim of physical accuracy or cross-scene generalization.

## Labeled results comparison

`results-comparison.mp4` synchronizes the five original eight-second experiment videos in a labeled three-over-two layout. `results-comparison-preview.gif` is a 12 fps, half-resolution README preview of the same full sequence, and `../previews/results-comparison-poster.png` is the four-second poster frame. The composition changes only layout, scale, frame rate, and labels; it does not regenerate, interpolate, reorder, or selectively omit experiment frames.

| Field | Value |
|---|---|
| Destination | GitHub README |
| Viewer | Researchers, engineers, and portfolio reviewers |
| Proof | The five force settings produce visibly different motion and coherence outcomes over the same 200-step interval. |
| Evidence class | Presentation derivative of archived experimental output |
| Source owners | Original project team: Michael Walker and Ethan Villalovoz |
| Source clips | `wall_smash.mp4`, `mass_falling.mp4`, `wind_field_low.mp4`, `wind_field.mp4`, `wind_field_high.mp4` |
| Layout source | `results-comparison-layout.svg` |
| Full export | H.264 MP4, 1920×1080, 30 fps, 8 seconds, no audio |
| Inline preview | Animated GIF, 960×540, 12 fps, complete 8-second sequence |
| Poster | PNG frame sampled at four seconds |

The source-to-label mapping follows the notebook and `docs/REPRODUCIBILITY.md`:

| Label | Source clip |
|---|---|
| Uniform gravity | `wall_smash.mp4` |
| Randomized inverse mass | `mass_falling.mp4` |
| Low wind | `wind_field_low.mp4` |
| Medium wind | `wind_field.mp4` |
| High wind | `wind_field_high.mp4` |

Rebuild all three derivatives from the checked-in source clips:

```bash
bash scripts/build_results_comparison.sh
```

The script requires FFmpeg plus either `rsvg-convert` or macOS `sips` for rasterizing the editable SVG layout.
