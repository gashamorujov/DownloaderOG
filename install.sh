#!/data/data/com.termux/files/usr/bin/bash

# GASHAM DOWNLOADEROG — Termux quraşdırıcısı
# İşləmə məntiqi: Termux-YTD2.0 üslubu

echo -e "\e[035m[*] Paketlər yenilənir...\e[0m"
apt update -y && apt upgrade -y

echo -e "\e[032m[*] Storage icazəsi istənilir...\e[0m"
echo -e "\e[032m[!] Açılan pəncərədə icazəni təsdiqləyin!\e[0m"
termux-setup-storage || echo -e "\e[033m[!] İcazə verilməyibsə: termux-setup-storage əmrini əl ilə işlədin.\e[0m"
sleep 2

echo -e "\e[034m[*] Python quraşdırılır...\e[0m"
pkg install python -y

echo -e "\e[034m[*] ffmpeg quraşdırılır (MP3 çevrilməsi üçün)...\e[0m"
pkg install ffmpeg -y

echo -e "\e[033m[*] yt-dlp quraşdırılır/yenilənir...\e[0m"
python -m pip install -U yt-dlp

echo -e "\e[036m[*] DownloaderOG qovluğu yaradılır...\e[0m"
mkdir -p /storage/emulated/0/DownloaderOG 2>/dev/null || mkdir -p "$HOME/storage/shared/DownloaderOG"

echo -e "\e[032m[*] termux-url-opener quraşdırılır...\e[0m"
mkdir -p "$HOME/.termux"
if [ -f "$HOME/.termux/termux-url-opener" ]; then
  cp "$HOME/.termux/termux-url-opener" "$HOME/.termux/termux-url-opener.bak"
  echo -e "\e[033m[!] Köhnə termux-url-opener backup edildi: termux-url-opener.bak\e[0m"
fi
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
cp "$SCRIPT_DIR/termux-url-opener" "$HOME/.termux/termux-url-opener"
chmod +x "$HOME/.termux/termux-url-opener"

echo -e "\e[032m"
echo -e "\e[032m[*] Quraşdırma tamamlandı! ✅\e[0m"
echo -e "\e[032m[*] İstifadə: videonu paylaşın → Termux seçin → keyfiyyəti seçin\e[0m"
echo -e "\e[033m[!] YouTube Shorts paylaşsanız, avtomatik yüklənir (menyu göstərilmir).\e[0m"
echo -e "\e[036m[>] Daha çox məlumat: https://github.com/gashamorujov/DownloaderOG\e[0m"
