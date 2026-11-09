---
name: blender-headless
description: Run Blender 5.1 in background mode with Python scripts for asset cleanup.
---
# Blender headless

```
blender -b [file.blend] --python script.py -- args
```

Arguments after `--` are available in the script via `sys.argv[sys.argv.index("--") + 1:]`.
BLENDER_EXE comes from .env (default C:/Program Files/Blender Foundation/Blender 5.1/blender.exe).
