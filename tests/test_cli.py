from pathlib import Path

from typer.testing import CliRunner

from cinegen.brief import load_brief
from cinegen.cli import app

ROOT = Path(__file__).resolve().parent.parent


def test_version():
    r = CliRunner().invoke(app, ["--version"])
    assert r.exit_code == 0
    assert r.stdout.strip() == "0.0.1"


def test_demo_brief():
    b = load_brief(ROOT / "briefs" / "demo.yaml")
    assert b.title
    assert len(b.shots) == 3
    assert b.characters[0].name == "Knight"
