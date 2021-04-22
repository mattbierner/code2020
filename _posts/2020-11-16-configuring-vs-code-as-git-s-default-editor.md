---
layout: post
title: "Configuring VS Code as git's default editor"
youtube_video_id: 23Hamqyx-E0
tags: cli git
thumbnails:
  default: https://i.ytimg.com/vi/23Hamqyx-E0/default.jpg
  medium: https://i.ytimg.com/vi/23Hamqyx-E0/mqdefault.jpg
  high: https://i.ytimg.com/vi/23Hamqyx-E0/hqdefault.jpg
  standard: https://i.ytimg.com/vi/23Hamqyx-E0/sddefault.jpg
  maxres: https://i.ytimg.com/vi/23Hamqyx-E0/maxresdefault.jpg
---

To configure VS Code as git's default editor, in a terminal run:

```bash
git config --global core.editor "code --wait"
```

Now git will use VS Code to edit commit messages. You can also configure VS Code as git's default diff tool.

[More info](https://code.visualstudio.com/docs/editor/versioncontrol#_vs-code-as-git-editor)
