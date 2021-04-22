---
layout: post
title: "Add missing imports on save for JavaScript and TypeScript"
youtube_video_id: Hd8yMapJCAw
tags:
thumbnails:
  default: https://i.ytimg.com/vi/Hd8yMapJCAw/default.jpg
  medium: https://i.ytimg.com/vi/Hd8yMapJCAw/mqdefault.jpg
  high: https://i.ytimg.com/vi/Hd8yMapJCAw/hqdefault.jpg
  standard: https://i.ytimg.com/vi/Hd8yMapJCAw/sddefault.jpg
---

Use the `editor.codeActionsOnSave` setting to add all missing imports to a TypeScript or JavaScript file whenever you save it.

To enable, just set:

```json
"editor.codeActionsOnSave": [
  "source.addMissingImports"
]
```
