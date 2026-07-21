#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEMO_DIR="$ROOT/assets/demos"
PREVIEW_DIR="$ROOT/assets/previews"
LAYOUT_SVG="$DEMO_DIR/results-comparison-layout.svg"
LAYOUT_PNG="$DEMO_DIR/results-comparison-layout.png"
OUTPUT_MP4="$DEMO_DIR/results-comparison.mp4"
OUTPUT_GIF="$DEMO_DIR/results-comparison-preview.gif"
OUTPUT_POSTER="$PREVIEW_DIR/results-comparison-poster.png"

require_file() {
  if [[ ! -f "$1" ]]; then
    printf 'Missing required input: %s\n' "$1" >&2
    exit 1
  fi
}

for input in \
  "$LAYOUT_SVG" \
  "$DEMO_DIR/wall_smash.mp4" \
  "$DEMO_DIR/mass_falling.mp4" \
  "$DEMO_DIR/wind_field_low.mp4" \
  "$DEMO_DIR/wind_field.mp4" \
  "$DEMO_DIR/wind_field_high.mp4"; do
  require_file "$input"
done

command -v ffmpeg >/dev/null 2>&1 || {
  printf 'ffmpeg is required to build the comparison media.\n' >&2
  exit 1
}

mkdir -p "$PREVIEW_DIR"

if command -v rsvg-convert >/dev/null 2>&1; then
  rsvg-convert --width 1920 --height 1080 "$LAYOUT_SVG" --output "$LAYOUT_PNG"
elif command -v sips >/dev/null 2>&1; then
  sips --setProperty format png "$LAYOUT_SVG" --out "$LAYOUT_PNG" >/dev/null
else
  require_file "$LAYOUT_PNG"
  printf 'No SVG rasterizer found; using checked-in layout: %s\n' "$LAYOUT_PNG" >&2
fi

ffmpeg -hide_banner -loglevel error \
  -loop 1 -framerate 30 -i "$LAYOUT_PNG" \
  -i "$DEMO_DIR/wall_smash.mp4" \
  -i "$DEMO_DIR/mass_falling.mp4" \
  -i "$DEMO_DIR/wind_field_low.mp4" \
  -i "$DEMO_DIR/wind_field.mp4" \
  -i "$DEMO_DIR/wind_field_high.mp4" \
  -filter_complex "\
    [1:v]fps=30,scale=400:400:flags=lanczos,setsar=1[uniform];\
    [2:v]fps=30,scale=400:400:flags=lanczos,setsar=1[inverse];\
    [3:v]fps=30,scale=400:400:flags=lanczos,setsar=1[low];\
    [4:v]fps=30,scale=400:400:flags=lanczos,setsar=1[medium];\
    [5:v]fps=30,scale=400:400:flags=lanczos,setsar=1[high];\
    [0:v][uniform]overlay=140:118:shortest=1[stage1];\
    [stage1][inverse]overlay=760:118:shortest=1[stage2];\
    [stage2][low]overlay=1380:118:shortest=1[stage3];\
    [stage3][medium]overlay=445:593:shortest=1[stage4];\
    [stage4][high]overlay=1075:593:shortest=1[outv]" \
  -map '[outv]' -t 8 -an -r 30 \
  -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -movflags +faststart \
  -y "$OUTPUT_MP4"

ffmpeg -hide_banner -loglevel error -ss 4 -i "$OUTPUT_MP4" \
  -frames:v 1 -y "$OUTPUT_POSTER"

ffmpeg -hide_banner -loglevel error -i "$OUTPUT_MP4" \
  -filter_complex "fps=12,scale=960:-2:flags=lanczos,split[frames][palette_input];\
    [palette_input]palettegen=max_colors=96:stats_mode=diff[palette];\
    [frames][palette]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle" \
  -loop 0 -y "$OUTPUT_GIF"

printf 'Wrote:\n  %s\n  %s\n  %s\n  %s\n' \
  "$LAYOUT_PNG" "$OUTPUT_MP4" "$OUTPUT_GIF" "$OUTPUT_POSTER"
