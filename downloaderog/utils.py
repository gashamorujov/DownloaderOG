"""Köməkçi funksiyalar: fayl adları, URL yoxlaması, qovluq seçimi."""

from __future__ import annotations

import os
import re
import sys
import unicodedata
import urllib.parse

_ILLEGAL_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def sanitize_filename(name: str, max_len: int = 150) -> str:
    name = unicodedata.normalize("NFKC", name or "")
    name = _ILLEGAL_CHARS.sub("_", name)
    name = re.sub(r"\s+", " ", name).strip(" .")
    if not name:
        name = "download"
    if len(name) > max_len:
        cut = name[:max_len].rsplit(" ", 1)[0].rstrip(" .")
        name = cut if cut else name[:max_len].rstrip(" .")
    return name


def unique_path(directory: str, filename: str) -> str:
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(directory, filename)
    counter = 1
    while os.path.exists(candidate):
        candidate = os.path.join(directory, f"{base} ({counter}){ext}")
        counter += 1
    return candidate


def is_valid_url(text: str) -> bool:
    if not text:
        return False
    parsed = urllib.parse.urlparse(text.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def resolve_download_dir(configured: str) -> str | None:
    if configured and configured != "auto":
        path = os.path.expanduser(configured)
        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            return None
        return path if os.access(path, os.W_OK) else None

    if os.environ.get("TERMUX_VERSION"):
        candidates = [
            "/storage/emulated/0/DownloaderOG",
            os.path.expanduser("~/storage/shared/DownloaderOG"),
            os.path.expanduser("~/DownloaderOG"),
        ]
    else:
        candidates = [os.path.expanduser("~/DownloaderOG")]

    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            continue
        if os.access(path, os.W_OK):
            return path
    return None


def format_duration(seconds: int) -> str:
    seconds = max(0, int(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"
