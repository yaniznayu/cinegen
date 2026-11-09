# CineGen

Autonomous pipeline that turns a text brief into rigged characters (Tripo API), an Unreal Engine 5.8
world, a Sequencer cinematic rendered with Movie Render Queue, and a packaged playable Windows build.
Blender 5.1 runs headless for asset cleanup.

**Status: pre-alpha, build in public.**

## Architecture

```
brief.yaml
   |
   v
assets    --(Tripo API)--> raw rigged mesh --(Blender headless)--> clean FBX
   |
   v
world     --(UnrealEditor-Cmd + Python + PCG)--> level
   |
   v
cinematic --(Sequencer + Movie Render Queue)--> frames
   |
   v
post      --(ffmpeg)--> final video
   |
   v
publish   --(UAT BuildCookRun)--> playable Windows build
```

## Quick start

```
uv sync
copy .env.example .env     # add TRIPO_API_KEY
uv run cinegen --version
uv run cinegen run briefs/demo.yaml
uv run pytest
```

## Credits

- [Tripo](https://www.tripo3d.ai/) - text-to-3D and rigging
- [Unreal Engine](https://www.unrealengine.com/) - world, Sequencer, Movie Render Queue
- [Blender](https://www.blender.org/) - asset cleanup
- [ffmpeg](https://ffmpeg.org/) - post
- typer, pydantic, uv, ruff

## License

MIT
