---
name: ue-python
description: Run Unreal Engine 5.8 headless with Python scripts and render with Movie Render Queue.
---
# UE Python (headless)

Run a script in the editor:

```
"<UE_ROOT>/Engine/Binaries/Win64/UnrealEditor-Cmd.exe" <project.uproject> -run=pythonscript -script=<file> -unattended -nop4 -nosplash -stdout -FullStdOutLogOutput
```

Render with Movie Render Queue:

```
UnrealEditor-Cmd.exe <project.uproject> <map> -game -MovieRenderPipeline -LevelSequence=<path> -MoviePipelineConfig=<path> -unattended -nosplash -stdout
```

Notes: UE_ROOT comes from .env (default C:/Program Files/Epic Games/UE_5.8). Enable Python Editor Script Plugin and Movie Render Queue in the project.
