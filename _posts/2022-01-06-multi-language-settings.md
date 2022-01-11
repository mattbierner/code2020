---
layout: post
title: "Multi-language settings"
youtube_video_id: 6PnXWXtJycM
tags: settings
thumbnails:
    default: https://i.ytimg.com/vi/6PnXWXtJycM/default.jpg
    medium: https://i.ytimg.com/vi/6PnXWXtJycM/mqdefault.jpg
    high: https://i.ytimg.com/vi/6PnXWXtJycM/hqdefault.jpg
    standard: https://i.ytimg.com/vi/6PnXWXtJycM/sddefault.jpg
    maxres: https://i.ytimg.com/vi/6PnXWXtJycM/maxresdefault.jpg
---

Apply a setting to multiple languages using "[langId1][langId2]" in your `settings.json`.

For example:

```json
"[javascript][typescript]": {
    "editor.rulers": [80]
}
```

Adds a ruler just in JavaScript and TypeScript files.