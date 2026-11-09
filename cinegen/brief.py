"""brief.yaml schema."""

from __future__ import annotations

from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class ShotType(str, Enum):
    dolly = "dolly"
    orbit = "orbit"
    crane = "crane"
    handheld = "handheld"
    static = "static"


class World(BaseModel):
    biome: str
    time_of_day: str = "noon"
    weather: str = "clear"


class Character(BaseModel):
    name: str
    prompt: str
    animations: list[str] = Field(default_factory=list)


class Shot(BaseModel):
    type: ShotType
    duration: float = Field(gt=0, description="seconds")
    subject: str = ""
    notes: str = ""


class Brief(BaseModel):
    title: str
    style: str = ""
    world: World
    characters: list[Character] = Field(default_factory=list)
    shots: list[Shot] = Field(default_factory=list)


def load_brief(path: str | Path) -> Brief:
    """Parse and validate a brief.yaml file."""
    data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return Brief.model_validate(data)
