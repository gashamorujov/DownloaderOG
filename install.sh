#!/data/data/com.termux/files/usr/bin/bash
# GASHAM DownloaderOG — Termux quraşdırıcısı
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
PREFIX="${PREFIX:-/data/data/com.termux/files/usr}"
INSTALL_DIR="$PREFIX/opt/downloaderog"
DOWNLOAD_DIR=""

say()  { printf "\033[1;32m[*]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[!]\033[0m %s\n" "$*"; }
err()  { printf "\033[1;31m[x]\033[0m %s\n" "$*" >&2; }

if [ ! -d "$PREFIX" ] || ! command -v pkg >/dev/null 2>&1; then
    err "Bu quraşdırıcı yalnız Termux mühitində işləyir."
    err "Termux quraşdırın və sonra yenidən cəhd edin."
    exit 1
fi

say "GASHAM DownloaderOG quraşdırılması başlayır..."

if command -v termux-setup-storage >/dev/null 2>&1; then
    say "Storage icazəsi yoxlanılır..."
    for d in "/storage/emulated/0/DownloaderOG" "$HOME/storage/shared/DownloaderOG" "$HOME/DownloaderOG"; do
        if mkdir -p "$d" 2>/dev/null && [ -w "$d" ]; then
            DOWNLOAD_DIR="$d"
            break
        fi
    done
    if [ -z "$DOWNLOAD_DIR" ]; then
        warn "Storage icazəsi hələ verilməyib."
        warn "Aşağıdakı əmri işlədin və icazəni təsdiqləyin:"
        warn "    termux-setup-storage"
    else
        say "Yükləmə qovluğu: $DOWNLOAD_DIR"
    fi
fi

say "Paketlər yenilənir (ilk dəfədirsə vaxt apara bilər)..."
pkg update -y >/dev/null 2>&1 || true
say "Lazımi paketlər quraşdırılır: python, ffmpeg, git, termux-api..."
pkg install -y python ffmpeg git termux-api 2>/dev/null || pkg install -y python ffmpeg git

say "Kod $INSTALL_DIR ünvanına kopyalanır..."
mkdir -p "$INSTALL_DIR"
if [ "$SCRIPT_DIR" != "$INSTALL_DIR" ]; then
    cp -r "$SCRIPT_DIR/downloaderog" "$INSTALL_DIR/"
    cp -r "$SCRIPT_DIR/scripts" "$INSTALL_DIR/"
    cp -r "$SCRIPT_DIR/config" "$INSTALL_DIR/"
    cp -r "$SCRIPT_DIR/assets" "$INSTALL_DIR/"
    cp -r "$SCRIPT_DIR/docs" "$INSTALL_DIR/"
    cp "$SCRIPT_DIR/requirements.txt" "$INSTALL_DIR/"
    cp "$SCRIPT_DIR/downloaderog.sh" "$INSTALL_DIR/"
    cp "$SCRIPT_DIR/README.md" "$INSTALL_DIR/" 2>/dev/null || true
    cp "$SCRIPT_DIR/LICENSE" "$INSTALL_DIR/" 2>/dev/null || true
fi
chmod +x "$INSTALL_DIR/downloaderog.sh"

say "Python dependency-ləri quraşdırılır..."
python -m pip install --upgrade pip >/dev/null 2>&1 || true
python -m pip install -r "$INSTALL_DIR/requirements.txt"

say "Konfiqurasiya hazırlanır..."
mkdir -p "$HOME/.config/downloaderog"
if [ ! -f "$HOME/.config/downloaderog/config.json" ]; then
    cp "$INSTALL_DIR/config/config.json" "$HOME/.config/downloaderog/config.json"
fi

say "Əmrlər qeydiyyata alınır: downloaderog, gasham..."
ln -sf "$INSTALL_DIR/downloaderog.sh" "$PREFIX/bin/downloaderog"
ln -sf "$INSTALL_DIR/downloaderog.sh" "$PREFIX/bin/gasham"

say "Android Share inteqrasiyası qurulur (termux-url-opener)..."
mkdir -p "$HOME/.termux"
if [ -f "$HOME/.termux/termux-url-opener" ]; then
    cp "$HOME/.termux/termux-url-opener" "$HOME/.termux/termux-url-opener.bak"
    warn "Köhnə termux-url-opener faylı backup edildi: termux-url-opener.bak"
fi
cat > "$HOME/.termux/termux-url-opener" <<EOF
#!$PREFIX/bin/bash
# GASHAM DownloaderOG — paylaşılan linklər avtomatik qəbul edilir
for url in "\$@"; do
    downloaderog --url "\$url"
done
EOF
chmod +x "$HOME/.termux/termux-url-opener"

say "Termux:Widget qısayolu hazırlanır..."
if mkdir -p "$HOME/.shortcuts" 2>/dev/null; then
    cat > "$HOME/.shortcuts/downloaderog.sh" <<EOF
#!$PREFIX/bin/bash
exec downloaderog
EOF
    chmod +x "$HOME/.shortcuts/downloaderog.sh"
fi

say ""
say "Quraşdırma tamamlandı!"
say "İstifadə:"
say "    downloaderog"
say "    gasham"
say "    downloaderog --url \"https://www.youtube.com/watch?v=...\""
if [ -n "$DOWNLOAD_DIR" ]; then
    say "Yüklənən fayllar: $DOWNLOAD_DIR"
fi
warn "Paylaşma üçün: telefondan video paylaşın → menyudan Termux seçin."
