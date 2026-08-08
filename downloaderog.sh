#!/data/data/com.termux/files/usr/bin/bash
# GASHAM DownloaderOG — launcher
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
export PYTHONPATH="$SCRIPT_DIR${PYTHONPATH:+:$PYTHONPATH}"
exec python3 -m downloaderog "$@"
