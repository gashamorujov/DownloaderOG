"""yt-dlp üzərində yükləmə idarəetməsi."""

from __future__ import annotations

import os
import shutil

import yt_dlp

from downloaderog.utils import sanitize_filename, unique_path


class DownloaderError(Exception):
    pass


def friendly_error(exc: Exception) -> str:
    message = str(exc)
    if any(key in message for key in ("Unsupported URL", "UnsupportedError")):
        return "Bu link dəstəklənmir və ya platforma tanınmadı."
    if "Requested format is not available" in message:
        return "Seçilmiş format artıq mövcud deyil. Linki yenidən yoxlayın."
    if "Private video" in message:
        return "Bu video privatdır və yüklənə bilməz."
    if "is not a valid URL" in message or "Invalid URL" in message:
        return "Link düzgün deyil. https:// ilə başlayan tam link daxil edin."
    if "Video unavailable" in message or "HTTP Error" in message:
        return "Video əldə edilə bilmədi (şəbəkə və ya mövcudluq xətası)."
    return message


class DownloadManager:
    def __init__(self, url: str, outdir: str, config: dict, on_progress=None) -> None:
        self.url = url
        self.outdir = outdir
        self.config = config
        self.on_progress = on_progress or (lambda status: None)
        self._finished_seen = False

    def _base_opts(self) -> dict:
        retries = int(self.config.get("retries", 3))
        return {
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "progress_hooks": [self._hook],
            "retries": retries,
            "fragment_retries": retries,
            "concurrent_fragment_downloads": int(self.config.get("concurrent_fragments", 4)),
            "continuedl": True,
            "overwrites": False,
            "noprogress": True,
            "socket_timeout": 20,
        }

    def _hook(self, data: dict) -> None:
        status = {
            "status": data.get("status", ""),
            "downloaded": data.get("downloaded_bytes") or 0,
            "total": data.get("total_bytes") or data.get("total_bytes_estimate"),
            "speed": data.get("speed"),
            "eta": data.get("eta"),
            "final": False,
        }
        if data.get("status") == "finished" and not self._finished_seen:
            self._finished_seen = True
            status["final"] = True
        self.on_progress(status)

    def download(self, selection: dict) -> str:
        tmp_dir = os.path.join(self.outdir, ".downloaderog_tmp")
        os.makedirs(tmp_dir, exist_ok=True)
        tmp_tmpl = os.path.join(tmp_dir, "part-%(id)s.%(ext)s")
        opts = self._base_opts()
        opts["outtmpl"] = tmp_tmpl

        ext = selection.get("ext", "mp4")
        if selection["type"] == "mp4":
            format_spec = selection["format_id"]
            if not selection.get("progressive", True):
                format_spec = f"{format_spec}+bestaudio[ext=m4a]/bestaudio"
            opts["format"] = format_spec
            opts["merge_output_format"] = "mp4"
        else:
            opts["format"] = selection.get("format_id") or "bestaudio/best"
            opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": str(selection["abr"]),
                }
            ]

        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(self.url, download=True)
        except yt_dlp.utils.DownloadError as exc:
            raise DownloaderError(f"Yükləmə xətası: {friendly_error(exc)}") from exc
        except Exception as exc:
            raise DownloaderError(f"Yükləmə zamanı xəta baş verdi: {exc}") from exc

        expected = os.path.join(tmp_dir, f"part-{info.get('id', 'download')}.{ext}")
        if not os.path.isfile(expected):
            candidates = sorted(
                name for name in os.listdir(tmp_dir) if name.startswith("part-")
            )
            if not candidates:
                raise DownloaderError("Yüklənmiş fayl tapılmadı.")
            expected = os.path.join(tmp_dir, candidates[-1])

        safe_title = sanitize_filename(info.get("title") or "download")
        final_path = unique_path(self.outdir, f"{safe_title}.{ext}")
        shutil.move(expected, final_path)
        shutil.rmtree(tmp_dir, ignore_errors=True)
        return final_path
