---
layout: post
title: "Parameter name inlay hints"
youtube_video_id: wFsiSJcpv60
tags: JavaScript TypeScript
thumbnails:
    default: https://i.ytimg.com/vi/wFsiSJcpv60/default.jpg
    medium: https://i.ytimg.com/vi/wFsiSJcpv60/mqdefault.jpg
    high: https://i.ytimg.com/vi/wFsiSJcpv60/hqdefault.jpg
    standard: https://i.ytimg.com/vi/wFsiSJcpv60/sddefault.jpg
    # maxres: https://i.ytimg.com/vi/wFsiSJcpv60/maxresdefault.jpg
---

Trying to figure out what that 'false' means in a function call? Try enabling parameter name inlay hints for JavaScript / TypeScript. These inline hints show parameter names, which can clear up the meaning of each argument.

You can enable them using: `javascript.inlayHints.parameterNames.enabled`
or `typescript.inlayHints.parameterNames.enabled`. Possible values:

- `none` — Disable parameter name inlay hints.
- `literals` — Only show inlay hints for literal arguments (boolean, number, string)
- `all` — Show hints for all arguments
