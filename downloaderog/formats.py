"""Formatların seçilməsi və keyfiyyət siyahılarının qurulması."""

from __future__ import annotations


def select_mp4_formats(info: dict, max_height: int = 2160) -> list[dict]:
    best: dict[int, dict] = {}
    for fmt in info.get("formats") or []:
        height = fmt.get("height")
        if not height or (fmt.get("vcodec") or "none") == "none":
            continue
        if height > max_height:
            continue
        entry = {
            "format_id": fmt.get("format_id"),
            "height": height,
            "ext": fmt.get("ext") or "mp4",
            "progressive": (fmt.get("acodec") or "none") != "none",
            "size": fmt.get("filesize") or fmt.get("filesize_approx"),
            "tbr": fmt.get("tbr"),
        }
        if entry["size"] is None and entry["tbr"] and info.get("duration"):
            entry["size"] = int(entry["tbr"] * 1000 * info["duration"] / 8)
        current = best.get(height)
        if current is None:
            best[height] = entry
            continue

        def is_better(a: dict, b: dict) -> bool:
            if a["progressive"] != b["progressive"]:
                return b["progressive"]
            if a["ext"] != b["ext"]:
                return b["ext"] == "mp4"
            if (a["size"] or 0) != (b["size"] or 0):
                return (b["size"] or 0) > (a["size"] or 0)
            return (b["tbr"] or 0) > (a["tbr"] or 0)

        if is_better(current, entry):
            best[height] = entry
    return [best[height] for height in sorted(best)]


def select_mp3_options(info: dict, bitrates) -> list[dict]:
    bitrate_list = [int(item) for item in (bitrates or [])]
    real: dict[int, str] = {}
    for fmt in info.get("formats") or []:
        if (fmt.get("vcodec") or "none") != "none":
            continue
        abr = fmt.get("abr")
        if not abr:
            continue
        key = int(round(abr))
        real.setdefault(key, fmt.get("format_id"))

    options: list[dict] = []
    for abr in bitrate_list:
        options.append(
            {
                "abr": abr,
                "format_id": real.get(abr),
                "real": abr in real,
            }
        )
    for abr in sorted(set(real) - set(bitrate_list)):
        options.append({"abr": abr, "format_id": real[abr], "real": True})
    options.sort(key=lambda item: item["abr"])
    return options
