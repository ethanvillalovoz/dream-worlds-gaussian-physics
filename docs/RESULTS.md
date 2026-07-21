# Qualitative results

The original project evaluated five rendered motion settings on the pretrained Ficus scene. Each strip below uses the exact simulation steps selected for the technical report. Images are unmodified archived frames from the original experiment runs.

[Download the labeled five-experiment comparison](../assets/demos/results-comparison.mp4?raw=1), or return to the README for the lightweight inline preview.

## Summary

| Experiment | Motion | Coherence | Main effect |
|---|---|---|---|
| Uniform gravity | Medium | Medium | Backward drift |
| Randomized inverse mass | High | Low | Downward smear |
| Low wind | Low | High | Gentle left drift |
| Medium wind | Medium | Medium-high | Leftward drift |
| High wind | High | Medium while visible | Off-screen drift |

## Uniform gravity

The Ficus moves backward into the scene and appears smaller while remaining recognizable for most of the sequence. The pot begins to smear near the end.

| Step 0 | Step 50 | Step 100 | Step 150 | Step 199 |
|:---:|:---:|:---:|:---:|:---:|
| ![Uniform gravity step 0](../assets/previews/uniform-gravity/step-000.png) | ![Uniform gravity step 50](../assets/previews/uniform-gravity/step-050.png) | ![Uniform gravity step 100](../assets/previews/uniform-gravity/step-100.png) | ![Uniform gravity step 150](../assets/previews/uniform-gravity/step-150.png) | ![Uniform gravity step 199](../assets/previews/uniform-gravity/step-199.png) |

[Download the uniform-gravity video](../assets/demos/wall_smash.mp4?raw=1)

## Randomized inverse-mass motion

Per-Gaussian motion variation produces a strong falling effect, but the plant stretches into a vertical trail and loses recognizable structure.

| Step 0 | Step 18 | Step 46 | Step 67 | Step 103 |
|:---:|:---:|:---:|:---:|:---:|
| ![Inverse mass step 0](../assets/previews/inverse-mass/step-000.png) | ![Inverse mass step 18](../assets/previews/inverse-mass/step-018.png) | ![Inverse mass step 46](../assets/previews/inverse-mass/step-046.png) | ![Inverse mass step 67](../assets/previews/inverse-mass/step-067.png) | ![Inverse mass step 103](../assets/previews/inverse-mass/step-103.png) |

[Download the inverse-mass video](../assets/demos/mass_falling.mp4?raw=1)

## Low wind

The plant drifts gently left while the pot, trunk, branches, and leaf clusters remain visually identifiable. This setting offers the best balance of motion and coherence.

| Step 0 | Step 50 | Step 100 | Step 150 | Step 199 |
|:---:|:---:|:---:|:---:|:---:|
| ![Low wind step 0](../assets/previews/wind-low/step-000.png) | ![Low wind step 50](../assets/previews/wind-low/step-050.png) | ![Low wind step 100](../assets/previews/wind-low/step-100.png) | ![Low wind step 150](../assets/previews/wind-low/step-150.png) | ![Low wind step 199](../assets/previews/wind-low/step-199.png) |

[Download the low-wind video](../assets/demos/wind_field_low.mp4?raw=1)

## Medium wind

The baseline wind field produces clearer leftward drift while retaining moderate-to-high coherence. The Ficus eventually moves partially outside the fixed camera view.

| Step 0 | Step 37 | Step 72 | Step 100 | Step 138 |
|:---:|:---:|:---:|:---:|:---:|
| ![Medium wind step 0](../assets/previews/wind-medium/step-000.png) | ![Medium wind step 37](../assets/previews/wind-medium/step-037.png) | ![Medium wind step 72](../assets/previews/wind-medium/step-072.png) | ![Medium wind step 100](../assets/previews/wind-medium/step-100.png) | ![Medium wind step 138](../assets/previews/wind-medium/step-138.png) |

[Download the medium-wind video](../assets/demos/wind_field.mp4?raw=1)

## High wind

The Ficus moves left rapidly and is mostly outside the frame after a short interval. It remains relatively coherent while visible, but the acceleration is too strong for a useful fixed-camera presentation.

| Step 0 | Step 15 | Step 30 | Step 45 | Step 60 |
|:---:|:---:|:---:|:---:|:---:|
| ![High wind step 0](../assets/previews/wind-high/step-000.png) | ![High wind step 15](../assets/previews/wind-high/step-015.png) | ![High wind step 30](../assets/previews/wind-high/step-030.png) | ![High wind step 45](../assets/previews/wind-high/step-045.png) | ![High wind step 60](../assets/previews/wind-high/step-060.png) |

[Download the high-wind video](../assets/demos/wind_field_high.mp4?raw=1)

## Interpretation boundary

These findings are qualitative observations from one pretrained scene and fixed cameras. They do not establish physical accuracy, cross-scene generalization, or quantitative shape preservation. See the [technical report](../paper/dream-worlds-technical-report.pdf) for the complete method and discussion.
