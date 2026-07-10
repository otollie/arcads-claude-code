#!/usr/bin/env bash
# Download the fonts used by the carousel templates (Google Fonts, OFL-licensed).
# Run once per environment; fonts/ is gitignored.
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)/fonts"
mkdir -p "$DIR"

curl -sL "https://github.com/google/fonts/raw/main/ofl/archivoblack/ArchivoBlack-Regular.ttf" -o "$DIR/ArchivoBlack.ttf"
curl -sL "https://github.com/google/fonts/raw/main/ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf" -o "$DIR/ArchivoVar.ttf"
curl -sL "https://github.com/google/fonts/raw/main/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf" -o "$DIR/InterVar.ttf"
# Anthropic brand look (tiktok-base.css / Claude-themed decks)
curl -sL "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-SemiBold.ttf" -o "$DIR/Poppins-SemiBold.ttf"
curl -sL "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Medium.ttf" -o "$DIR/Poppins-Medium.ttf"
curl -sL "https://github.com/google/fonts/raw/main/ofl/lora/Lora%5Bwght%5D.ttf" -o "$DIR/Lora[wght].ttf"

echo "Fonts downloaded to $DIR"
