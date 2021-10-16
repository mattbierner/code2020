---
layout: post
title: "Language Specific Settings"
youtube_video_id: CU3Tss6lnEQ
tags: settings
thumbnails:
  default: https://i.ytimg.com/vi/CU3Tss6lnEQ/default.jpg
  medium: https://i.ytimg.com/vi/CU3Tss6lnEQ/mqdefault.jpg
  high: https://i.ytimg.com/vi/CU3Tss6lnEQ/hqdefault.jpg
  standard: https://i.ytimg.com/vi/CU3Tss6lnEQ/sddefault.jpg
  maxres: https://i.ytimg.com/vi/CU3Tss6lnEQ/maxresdefault.jpg
---

You can configure many VS Code settings related to editing on a per-language basis. Just add a `"[LANGUAGE]": {}` section to your settings.json that contains the setting specific to that language. For example:

```json
"[javascript]": {
  "editor.renderWhitespace": "all"
}
```

[More info](https://code.visualstudio.com/docs/getstarted/settings#_language-specific-editor-settings)