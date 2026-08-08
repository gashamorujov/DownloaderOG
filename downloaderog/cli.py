"""DownloaderOG əsas giriş nöqtəsi və istifadəçi axını."""

from __future__ import annotations

import argparse
import re
import sys

import yt_dlp

from downloaderog import __version__, ui
from downloaderog.config import load_config
from downloaderog.downloader import DownloadManager, DownloaderError, friendly_error
from downloaderog.formats import select_mp3_options, select_mp4_formats
from downloaderog.utils import format_duration, is_valid_url, resolve_download_dir

URL_RE = re.compile(r"https?://[^\s<>\"']+")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="DownloaderOG",
        description="GASHAM DownloaderOG — Termux üçün universal media yükləyici",
    )
    parser.add_argument("--url", help="Birbaşa yüklənəcək video/audio linki")
    parser.add_argument("--dir", help="Yükləmə qovluğu (standart: avtomatik)")
    parser.add_argument("--config", help="Konfiqurasiya faylının yolu")
    parser.add_argument("--no-anim", action="store_true", help="Banner animasiyasını söndür")
    parser.add_argument("--version", action="version", version=f"DownloaderOG {__version__}")
    return parser


def _extract_first_url(text: str) -> str | None:
    for part in text.split():
        if is_valid_url(part):
            return part
    match = URL_RE.search(text)
    return match.group(0) if match else None


def _pick_video(info) -> dict | None:
    if isinstance(info, dict) and info.get("_type") == "playlist":
        entries = info.get("entries") or []
        return entries[0] if entries else None
    return info


def _fmt_size_label(size_bytes) -> str:
    if not size_bytes:
        return "—"
    mb = size_bytes / (1024 * 1024)
    if mb >= 1024:
        return f"{mb / 1024:.2f} GB"
    return f"{mb:.0f} MB"


def _show_menus(info: dict, config: dict):
    mp4 = select_mp4_formats(info, int(config.get("max_height", 2160)))
    mp3 = select_mp3_options(info, config.get("mp3_bitrates"))
    if not mp4 and not mp3:
        print(ui.RED + "Xəta: Bu media üçün yüklənə bilən format tapılmadı." + ui.RESET)
        sys.exit(1)

    number = 0
    if mp4:
        print("\n" + ui.BOLD + ui.BLUE + "MP4" + ui.RESET)
        for fmt in mp4:
            number += 1
            label = f"{fmt['height']}p"
            if not fmt["progressive"]:
                label += " (yalnız video)"
            print(f"  {number}. {label} — {_fmt_size_label(fmt['size'])}")

    if mp3:
        print("\n" + ui.BOLD + ui.RED + "MP3" + ui.RESET)
        duration = info.get("duration") or 0
        for audio in mp3:
            number += 1
            size = int(duration * audio["abr"] * 1000 / 8) if duration else None
            note = " (orijinal audio)" if audio.get("real") else ""
            print(f"  {number}. MP3 — {audio['abr']} kbps — {_fmt_size_label(size)}{note}")
    return mp4, mp3, number


def _choose(total: int, mp4: list[dict], mp3: list[dict]) -> dict:
    while True:
        try:
            raw = input("\nSeçiminizi daxil edin: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProqramdan çıxılır. Sağ olun!")
            sys.exit(0)
        if raw.lower() in ("q", "quit", "exit", "çıx"):
            print("Proqramdan çıxılır. Sağ olun!")
            sys.exit(0)
        if not raw.isdigit():
            print(ui.RED + f"Xəta: yalnız nömrə daxil edin (1-{total})." + ui.RESET)
            continue
        choice = int(raw)
        if 1 <= choice <= total:
            break
        print(ui.RED + f"Xəta: {choice} düzgün seçim deyil. Düzgün diapazon: 1-{total}." + ui.RESET)

    if choice <= len(mp4):
        return {
            "type": "mp4",
            "format_id": mp4[choice - 1]["format_id"],
            "progressive": mp4[choice - 1]["progressive"],
            "ext": "mp4",
        }
    audio = mp3[choice - len(mp4) - 1]
    return {
        "type": "mp3",
        "format_id": audio.get("format_id"),
        "abr": audio["abr"],
        "ext": "mp3",
    }


def _make_progress_callback():
    def callback(status: dict) -> None:
        if status.get("final"):
            print("\n" + ui.YELLOW + "Yükləndi — fayl emal olunur..." + ui.RESET)
        elif status["status"] == "downloading":
            ui.render_progress(status)

    return callback


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    config = load_config(override={"download_dir": args.dir}, config_path=args.config)
    ui.show_banner(animate=not args.no_anim and config.get("animate_banner", True))

    download_dir = resolve_download_dir(config.get("download_dir"))
    if not download_dir:
        print(ui.RED + "Xəta: DownloaderOG yükləmə qovluğu yaradıla bilmədi." + ui.RESET)
        print("Termux-da storage icazəsini verin və yenidən cəhd edin:")
        print(ui.BOLD + "  termux-setup-storage" + ui.RESET)
        sys.exit(1)
    print(ui.BOLD + ui.GREEN + "Yükləmə qovluğu:" + ui.RESET + f" {download_dir}")

    url = args.url or input("Video/audio linkini daxil edin: ").strip()
    if not url:
        print(ui.RED + "Xəta: Link daxil edilməyib." + ui.RESET)
        sys.exit(1)
    extracted = _extract_first_url(url)
    if not extracted:
        print(ui.RED + "Xəta: Daxil edilən link düzgün deyil." + ui.RESET)
        sys.exit(1)

    extract_opts = {
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "skip_download": True,
        "socket_timeout": 20,
        "retries": int(config.get("retries", 3)),
    }
    try:
        with yt_dlp.YoutubeDL(extract_opts) as ydl:
            raw = ydl.extract_info(extracted, download=False)
    except yt_dlp.utils.UnsupportedError:
        print(ui.RED + "Xəta: Bu link dəstəklənmir və ya platforma tanınmadı." + ui.RESET)
        sys.exit(1)
    except yt_dlp.utils.DownloadError as exc:
        print(ui.RED + f"Xəta: Media məlumatları alına bilmədi. {friendly_error(exc)}" + ui.RESET)
        sys.exit(1)
    except Exception as exc:
        print(ui.RED + f"Xəta: Media analizi zamanı problem yarandı: {exc}" + ui.RESET)
        sys.exit(1)

    info = _pick_video(raw)
    if not info:
        print(ui.RED + "Xəta: Bu linkdən media məlumatı əldə edilə bilmədi." + ui.RESET)
        sys.exit(1)

    title = info.get("title") or "Bilinməyən başlıq"
    uploader = info.get("uploader") or info.get("channel") or "Bilinmir"
    print(ui.BOLD + ui.GREEN + "Başlıq:" + ui.RESET + f" {title}")
    print(ui.BOLD + ui.GREEN + "Kanal:" + ui.RESET + f" {uploader}")
    if info.get("duration"):
        print(ui.BOLD + ui.GREEN + "Müddət:" + ui.RESET + f" {format_duration(info['duration'])}")

    mp4, mp3, total = _show_menus(info, config)
    selection = _choose(total, mp4, mp3)
    manager = DownloadManager(extracted, download_dir, config, _make_progress_callback())
    try:
        final_path = manager.download(selection)
    except DownloaderError as exc:
        print(ui.RED + str(exc) + ui.RESET)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nYükləmə dayandırıldı. Heç bir fayl tamamlanmadı.")
        sys.exit(130)

    print(ui.GREEN + ui.BOLD + "\nDownload completed successfully!" + ui.RESET)
    print(ui.GREEN + "Saved to: " + ui.RESET + final_path)
    sys.exit(0)
