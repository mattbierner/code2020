---
layout: post
title: "Configuring the terminal's title"
youtube_video_id: miLXfQSphw0
tags: terminal settings
thumbnails:
    default: https://i.ytimg.com/vi/miLXfQSphw0/default.jpg
    medium: https://i.ytimg.com/vi/miLXfQSphw0/mqdefault.jpg
    high: https://i.ytimg.com/vi/miLXfQSphw0/hqdefault.jpg
    standard: https://i.ytimg.com/vi/miLXfQSphw0/sddefault.jpg
    maxres: https://i.ytimg.com/vi/miLXfQSphw0/maxresdefault.jpg
---

Use the `terminal.integrated.tabs.title` setting to configure the title shown for integrated terminals in VS Code.

Some useful variables you can use in the title:

- `${process}` — Current process name.
- `${cwd}` — Current working directory .
- `${workspaceFolder}` — The workspace the terminal was launched from.
- `${local}` — Indicates local terminals in remote workspaces.