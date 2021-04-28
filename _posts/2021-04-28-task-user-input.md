---
layout: post
title: "Task user input"
youtube_video_id: PZqCLJ4XdrI
tags: tasks
thumbnails:
  default: https://i.ytimg.com/vi/PZqCLJ4XdrI/default.jpg
  medium: https://i.ytimg.com/vi/PZqCLJ4XdrI/mqdefault.jpg
  high: https://i.ytimg.com/vi/PZqCLJ4XdrI/hqdefault.jpg
  standard: https://i.ytimg.com/vi/PZqCLJ4XdrI/sddefault.jpg
  maxres: https://i.ytimg.com/vi/PZqCLJ4XdrI/maxresdefault.jpg
---

Custom tasks in VS Code can prompt a user for input. This input is then inserted into the task execution script.

To start, in the `task` section of the `tasks.json`, use a `${input:myInput}` variable. Then define a new `input` called `myInput` in the `inputs` section of the `tasks.json`.

For example:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "double",
            "type": "shell",
            "command": "echo ${input:myInput} ${input:myInput}",
            "problemMatcher": []
        }
    ],
    "inputs": [
        {
            "id": "myInput",
            "description": "What should I double?",
            "type": "promptString"
        }
    ]
}
```

[More info](https://code.visualstudio.com/docs/editor/variables-reference#_input-variables)