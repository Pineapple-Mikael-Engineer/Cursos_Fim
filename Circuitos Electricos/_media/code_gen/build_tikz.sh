#!/usr/bin/env bash
# Compila .tex de TikZ a SVG en ../img_gen/  (relativo al code_gen/ del curso).
# Copia este script al code_gen/ del curso, junto a una carpeta tikz/ con los .tex.
# Uso:  ./build_tikz.sh                      (compila todos los tikz/*.tex)
#       ./build_tikz.sh tikz/rc_serie.tex    (solo los indicados)
cd "$(dirname "$0")" || exit 1
mkdir -p ../img_gen
TMP=/tmp/tikzbuild; mkdir -p "$TMP"
files=("$@"); [ ${#files[@]} -eq 0 ] && files=(tikz/*.tex)
for f in "${files[@]}"; do
  base=$(basename "$f" .tex)
  if pdflatex -interaction=nonstopmode -halt-on-error -output-directory="$TMP" "$f" >/dev/null 2>&1; then
    pdf2svg "$TMP/$base.pdf" "../img_gen/$base.svg" && echo "  -> $base.svg"
  else
    echo "  ERROR: $base  (log: $TMP/$base.log)"
  fi
done
