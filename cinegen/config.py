"""Settings loaded from environment / .env."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


@dataclass
class Settings:
    tripo_api_key: str = ""
    ue_root: Path = Path("C:/Program Files/Epic Games/UE_5.8")
    blender_exe: Path = Path("C:/Program Files/Blender Foundation/Blender 5.1/blender.exe")
    out_dir: Path = field(default_factory=lambda: Path("./out"))


def load_settings() -> Settings:
    """Read settings from .env and the environment."""
    load_dotenv()
    d = Settings()
    return Settings(
        tripo_api_key=os.getenv("TRIPO_API_KEY", d.tripo_api_key),
        ue_root=Path(os.getenv("UE_ROOT", str(d.ue_root))),
        blender_exe=Path(os.getenv("BLENDER_EXE", str(d.blender_exe))),
        out_dir=Path(os.getenv("OUT_DIR", str(d.out_dir))),
    )
