"""CineGen command line interface."""

from __future__ import annotations

from pathlib import Path

import typer

from cinegen import __version__
from cinegen.brief import load_brief

app = typer.Typer(help="CineGen: autonomous UE5 cinematic + playable world generator.")


def _version(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False, "--version", callback=_version, is_eager=True, help="Show version and exit."
    ),
) -> None:
    """CineGen root command."""


@app.command()
def run(brief: Path) -> None:
    """Run the full pipeline for a brief.yaml."""
    b = load_brief(brief)
    typer.echo(f"Loaded brief: {b.title}")
    typer.echo("TODO: assets -> world -> cinematic -> post -> publish")


@app.command()
def assets(prompt: str) -> None:
    """Generate a rigged character from a prompt (Tripo + Blender cleanup)."""
    typer.echo(f"TODO: generate asset for: {prompt}")


@app.command()
def world() -> None:
    """Build the Unreal Engine world."""
    typer.echo("TODO: world")


@app.command()
def cinematic() -> None:
    """Build the Sequencer cinematic and render with Movie Render Queue."""
    typer.echo("TODO: cinematic")


@app.command()
def post() -> None:
    """Post-process rendered frames with ffmpeg."""
    typer.echo("TODO: post")


@app.command()
def publish() -> None:
    """Package the playable Windows build and publish outputs."""
    typer.echo("TODO: publish")
