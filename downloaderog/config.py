"""Konfiqurasiya yükləmə məntiqi."""

from __future__ import annotations

import json
import os

DEFAULTS = {
    "download_dir": "auto",
    "max_height": 2160,
    "mp3_bitrates": [64, 96, 128, 160, 192, 256, 320],
    "concurrent_fragments": 4,
    "retries": 3,
    "animate_banner": True,
}


def _config_paths(override: str | None) -> list[str]:
    paths: list[str] = []
    if override:
        paths.append(os.path.expanduser(override))
    paths.append(os.path.expanduser("~/.config/downloaderog/config.json"))
    repo_config = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config",
        "config.json",
    )
    paths.append(repo_config)
    return paths


def load_config(override: dict | None = None, config_path: str | None = None) -> dict:
    config = dict(DEFAULTS)
    for path in _config_paths(config_path):
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                user = json.load(fh)
            config.update({key: value for key, value in user.items() if key in DEFAULTS})
        except (OSError, ValueError):
            continue
    if override:
        config.update({key: value for key, value in override.items() if value is not None})
    return config
