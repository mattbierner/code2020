---
layout: post
title: "Extract type refactorings"
youtube_video_id: 9-_GRo4lDko
tags: refactor TypeScript 
thumbnails:
  default: https://i.ytimg.com/vi/9-_GRo4lDko/default.jpg
  medium: https://i.ytimg.com/vi/9-_GRo4lDko/mqdefault.jpg
  high: https://i.ytimg.com/vi/9-_GRo4lDko/hqdefault.jpg
  standard: https://i.ytimg.com/vi/9-_GRo4lDko/sddefault.jpg
  maxres: https://i.ytimg.com/vi/9-_GRo4lDko/maxresdefault.jpg
---

Quickly extract a selected TypeScript type to a new interface or type alias.

This is helpful when cleaning up code or if you want to reuse a type somewhere else in your project

Here's the "extract" keyboard shortcut I use that supports both `extract type` and `extract constant`:

```json
{
  "key": "ctrl+shift+e",
  "command": "editor.action.refactor",
  "args": {
    "kind": "refactor.extract",
    "preferred": true,
    "apply": "first"
  }
}
```