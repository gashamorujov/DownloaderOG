#!/data/data/com.termux/files/usr/bin/bash

# GASHAM DOWNLOADEROG — Termux quraşdırıcısı
# İşləmə məntiqi: Termux-YTD2.0 üslubu

SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"

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

echo -e "\e[034m[*] termux-api quraşdırılır (MediaScanner / Qalereya üçün)...\e[0m"
pkg install termux-api -y
echo -e "\e[033m[!] Diqqət: F-Droid-dən 'Termux:API' tətbiqini də quraşdırın —\e[0m"
echo -e "\e[033m    media qeydiyyatı (Qalereya/musiqi pleyer) onunla işləyir.\e[0m"
sleep 1

echo -e "\e[034m[*] deno quraşdırılır (YouTube üçün JS mühərriki)...\e[0m"
pkg install deno -y || echo -e "\e[033m[!] deno quraşdırıla bilmədi — YouTube üçün: pkg install deno\e[0m"

echo -e "\e[033m[*] yt-dlp quraşdırılır/yenilənir...\e[0m"
python -m pip install -U yt-dlp

echo -e "\e[033m[*] curl_cffi quraşdırılır (TikTok impersonasiya dəstəyi)...\e[0m"
python -m pip install -U "curl_cffi>=0.10,<0.16" || echo -e "\e[033m[!] curl_cffi quraşdırıla bilmədi — TikTok üçün: python -m pip install 'curl_cffi>=0.10,<0.16'\e[0m"

echo -e "\e[036m[*] Cookies qovluğu yaradılır (Instagram/TikTok üçün)...\e[0m"
mkdir -p "$HOME/.config/downloaderog"

echo -e "\e[036m[*] Download qovluğu yaradılır...\e[0m"
mkdir -p /storage/emulated/0/Download 2>/dev/null || mkdir -p "$HOME/storage/shared/Download"

echo -e "\e[036m[*] DownloaderOG qovluğu yaradılır (son yükləmə yeri)...\e[0m"
mkdir -p /storage/emulated/0/Download/DownloaderOG 2>/dev/null || mkdir -p "$HOME/storage/shared/Download/DownloaderOG"

echo -e "\e[032m[*] ~/bin qovluğu yaradılır...\e[0m"
mkdir -p "$HOME/bin"

echo -e "\e[032m[*] termux-url-opener quraşdırılır (~/bin/)...\e[0m"
if [ -f "$HOME/bin/termux-url-opener" ]; then
  cp "$HOME/bin/termux-url-opener" "$HOME/bin/termux-url-opener.bak"
  echo -e "\e[033m[!] Köhnə ~/bin/termux-url-opener backup edildi: termux-url-opener.bak\e[0m"
fi
cp "$SCRIPT_DIR/termux-url-opener" "$HOME/bin/termux-url-opener"
chmod +x "$HOME/bin/termux-url-opener"

echo -e "\e[032m[*] termux-url-opener yenilənir (~/.termux/, müasir Termux üçün)...\e[0m"
mkdir -p "$HOME/.termux"
if [ -f "$HOME/.termux/termux-url-opener" ]; then
  cp "$HOME/.termux/termux-url-opener" "$HOME/.termux/termux-url-opener.bak"
  echo -e "\e[033m[!] Köhnə ~/.termux/termux-url-opener backup edildi: termux-url-opener.bak\e[0m"
fi
cp "$SCRIPT_DIR/termux-url-opener" "$HOME/.termux/termux-url-opener"
chmod +x "$HOME/.termux/termux-url-opener"

echo -e "\e[032m"
echo -e "\e[032m[*] Quraşdırma tamamlandı! ✅\e[0m"
echo -e "\e[032m[*] İstifadə: videonu paylaşın → Termux seçin → keyfiyyəti seçin\e[0m"
echo -e "\e[032m[*] Fayllar: Download → DownloaderOG (cut/move)\e[0m"
echo -e "\e[033m[!] YouTube Shorts paylaşsanız, avtomatik yüklənir (menyu göstərilmir).\e[0m"
echo -e "\e[033m[!] Instagram/TikTok xəta verirsə: brauzerdə login olun, cookies.txt yaradın\e[0m"
echo -e "\e[033m    və ~/.config/downloaderog/cookies.txt ünvanına kopyalayın.\e[0m"
echo -e "\e[036m[>] Daha çox məlumat: https://github.com/gashamorujov/DownloaderOG\e[0m"
