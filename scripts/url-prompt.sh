#!/data/data/com.termux/files/usr/bin/bash
# GASHAM DownloaderOG — əl ilə link daxil etmək üçün köməkçi
set -euo pipefail

read -r -p "Video/audio linkini daxil edin: " url
exec downloaderog --url "$url"
