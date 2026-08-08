#!/data/data/com.termux/files/usr/bin/bash
# GASHAM DownloaderOG — Android Share inteqrasiyasını qurur/berpa edir
set -euo pipefail

PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"

say()  { printf "\033[1;32m[*]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[!]\033[0m %s\n" "$*"; }

if ! command -v downloaderog >/dev/null 2>&1; then
    warn "downloaderog əmri tapılmadı. Əvvəlcə quraşdırın: bash install.sh"
    exit 1
fi

mkdir -p "$HOME/.termux"
if [ -f "$HOME/.termux/termux-url-opener" ]; then
    cp "$HOME/.termux/termux-url-opener" "$HOME/.termux/termux-url-opener.bak"
fi
cat > "$HOME/.termux/termux-url-opener" <<EOF
#!$PREFIX/bin/bash
# GASHAM DownloaderOG — paylaşılan linklər avtomatik qəbul edilir
for url in "\$@"; do
    downloaderog --url "\$url"
done
EOF
chmod +x "$HOME/.termux/termux-url-opener"

if mkdir -p "$HOME/.shortcuts" 2>/dev/null; then
    cat > "$HOME/.shortcuts/downloaderog.sh" <<EOF
#!$PREFIX/bin/bash
exec downloaderog
EOF
    chmod +x "$HOME/.shortcuts/downloaderog.sh"
fi

say "Android Share inteqrasiyası hazırdır!"
say ""
say "İstifadə:"
say "  1. YouTube/TikTok/Instagram-da videonu açın"
say "  2. Paylaş (Share) düyməsini basın"
say "  3. Menyudan Termux seçin"
say "  4. DownloaderOG avtomatik başlayacaq"
say ""
say "Alternativ: proqramı əl ilə açın → linki yapışdırın → Enter"
