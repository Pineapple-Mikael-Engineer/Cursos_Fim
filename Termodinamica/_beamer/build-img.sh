#!/usr/bin/env bash
# Regenera las imágenes PDF para los beamers a partir de los SVG del vault.
# Los .pdf están gitignoreados (*.pdf); este script los reconstruye.
# Uso:  bash build-img.sh
cd "$(dirname "$0")" || exit 1
mkdir -p img
n=0; ok=0
for svg in ../_media/img_gen/*.svg; do
  [ -e "$svg" ] || continue
  base=$(basename "$svg" .svg)
  n=$((n+1))
  if inkscape "$svg" --export-type=pdf --export-filename="img/$base.pdf" >/dev/null 2>&1; then
    ok=$((ok+1))
  else
    echo "  ERROR: $base"
  fi
done
echo "imágenes PDF generadas: $ok/$n en img/"
