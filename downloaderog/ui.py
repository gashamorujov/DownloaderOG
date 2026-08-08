"""Terminal interfeysi: ANSI rənglər, animasiyalı banner, progress bar."""

from __future__ import annotations

import os
import shutil
import sys
import time

BLUE = "\033[34m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"
CLEAR_LINE = "\033[2K"

_LETTERS = {
    "G": ["  ____", " / ___|", "| |  _", "| |_| |", " \\____|"],
    "A": ["    _   ", "   / \\  ", "  / _ \\ ", " / ___ \\", "/_/   \\_\\"],
    "S": [" ____", "/ ___|", "\\___ \\", " ___) |", "|____/"],
    "H": [" _   _", "| | | |", "| |_| |", "|  _  |", "|_| |_|"],
    "M": [" __  __", "|  \\/  |", "| |\\/| |", "| |  | |", "|_|  |_|"],
}
_FALLBACK_LETTER = ["####", "####", "####", "####", "####"]


def _banner_rows() -> list[str]:
    banner_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets",
        "banner.txt",
    )
    try:
        with open(banner_path, encoding="utf-8") as fh:
            rows = [line.rstrip("\n") for line in fh if line.strip()]
        if len(rows) >= 5 and max(len(row) for row in rows) >= 6:
            return rows[:5]
    except OSError:
        pass

    letters = [_LETTERS.get(char.upper(), _FALLBACK_LETTER) for char in "GASHAM"]
    width = max(len(line) for letter in letters for line in letter)
    rows = []
    for index in range(5):
        rows.append("  ".join(letter[index].ljust(width) for letter in letters).rstrip())
    return rows


def show_banner(animate: bool = True) -> None:
    rows = _banner_rows()
    frames = 3 if animate and sys.stdout.isatty() else 1
    palettes = [
        [BLUE, GREEN, RED, CYAN, BLUE, GREEN],
        [RED, CYAN, GREEN, BLUE, RED, CYAN],
        [GREEN, BLUE, CYAN, RED, GREEN, BLUE],
    ]
    lines_count = len(rows) + 2
    for frame in range(frames):
        if frame:
            sys.stdout.write(f"\033[{lines_count}A")
        palette = palettes[frame % len(palettes)]
        for index, row in enumerate(rows):
            color = palette[index % len(palette)]
            sys.stdout.write(CLEAR_LINE + BOLD + color + row + RESET + "\n")
        sys.stdout.write(CLEAR_LINE + BOLD + CYAN + "DownloaderOG — Universal Media Downloader" + RESET + "\n")
        sys.stdout.write(CLEAR_LINE + YELLOW + "GASHAM • Termux üçün universal video/audio yükləyici" + RESET + "\n")
        sys.stdout.flush()
        if frame < frames - 1:
            time.sleep(0.35)
    print()


def fmt_size(num: float) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(num) < 1024.0:
            return f"{num:.1f} {unit}"
        num /= 1024.0
    return f"{num:.1f} PB"


def fmt_eta(seconds: float) -> str:
    seconds = max(0, int(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}h{minutes:02d}m"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


def render_progress(status: dict) -> None:
    total = status.get("total")
    downloaded = status.get("downloaded") or 0
    speed = status.get("speed")
    eta = status.get("eta")
    columns = shutil.get_terminal_size((80, 24)).columns
    bar_width = max(10, min(50, columns - 45))
    percent = None
    if total:
        percent = min(100.0, downloaded / total * 100.0)
    bar_len = int(bar_width * (percent or 0) / 100.0) if percent is not None else 0
    bar = "█" * bar_len + "░" * (bar_width - bar_len)

    parts = [f"Downloading {bar}"]
    if percent is not None:
        parts.append(f"{percent:5.1f}%")
    parts.append(fmt_size(downloaded))
    if total:
        parts.append(f"/ {fmt_size(total)}")
    if speed:
        parts.append(f"{fmt_size(speed)}/s")
    if eta:
        parts.append(f"ETA {fmt_eta(eta)}")
    line = " ".join(parts)
    sys.stdout.write("\r" + CLEAR_LINE + GREEN + line + RESET)
    sys.stdout.flush()
