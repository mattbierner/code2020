---
layout: post
title: "Editor: Semantic Token Color Customizations"
youtube_video_id: vthJRp8jPkw
tags: settings theme
thumbnails:
  default: https://i.ytimg.com/vi/vthJRp8jPkw/default.jpg
  medium: https://i.ytimg.com/vi/vthJRp8jPkw/mqdefault.jpg
  high: https://i.ytimg.com/vi/vthJRp8jPkw/hqdefault.jpg
  standard: https://i.ytimg.com/vi/vthJRp8jPkw/sddefault.jpg
  maxres: https://i.ytimg.com/vi/vthJRp8jPkw/maxresdefault.jpg
---

Customize code colors based on semantic meaning. This is useful for understanding what code does at a glance.

The following settings for example makes all methods hotpink, all readonly properties green, and all enum values italic:

```json
"editor.semanticTokenColorCustomizations": {
    "rules": {
        "method": "#ff00ff",
        "property.readonly": "#00ff0f",
        "enumMember": {
            "italic": true
        }
    }
}
```

Not all languages support semantic highlighting but it is supported out of the box for JavaScript and TypeScript.

[More Info](https://code.visualstudio.com/docs/getstarted/themes#_editor-semantic-highlighting)
