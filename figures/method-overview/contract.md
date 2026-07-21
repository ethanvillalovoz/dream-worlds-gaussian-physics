# Method overview figure contract

> This figure should allow a skeptical graphics or robotics reader to conclude **that Dream Worlds animates a pretrained Gaussian Splatting scene by updating only Gaussian centers with simple force rules** because it shows **the external checkpoint and camera inputs, per-Gaussian dynamic and fixed state, the three force families, the shared integration-and-clamp loop, and fixed-camera rendering** under **the original notebook conditions of 200 steps and `dt = 0.02`**.

## Role and destination

- **Role:** Conceptual method overview; not experimental evidence.
- **Destination:** GitHub README at approximately 900-1,000 CSS pixels wide.
- **Formats:** Editable SVG plus a 1,440 x 640 PNG export for raster previews.
- **Reading order:** Left to right, with the repeated update-and-render loop indicated beneath the pipeline.

## Evidence boundary

- Method specification: `notebooks/gaussian_splatting_physics.ipynb`
- Archival method description: `paper/dream-worlds-technical-report.pdf`, Sections 2.1-2.4
- No numerical results, reconstructed output, third-party icons, or generated scientific imagery are used.
- The Gaussian cloud and camera glyphs are conceptual vector marks. They do not depict measured geometry or a reconstructed experimental frame.

## Encodings

- Blue: external pretrained scene and camera inputs.
- Orange: Gaussian centers and velocity state updated during simulation.
- Gray: Gaussian attributes held fixed.
- Purple: experiment-specific force choices.
- Green: rendered frames and MP4 export.

## Claim calibration

The figure explains the implemented data flow only. It does not claim physical accuracy, quantitative coherence, generalization beyond the Ficus scene, or equivalence to a full material-point or continuum simulator.
