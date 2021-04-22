---
layout: post
title: "The --wait command line flag"
youtube_video_id: -8zYNkI2jEA
tags: clid
thumbnails:
  default: https://i.ytimg.com/vi/-8zYNkI2jEA/default.jpg
  medium: https://i.ytimg.com/vi/-8zYNkI2jEA/mqdefault.jpg
  high: https://i.ytimg.com/vi/-8zYNkI2jEA/hqdefault.jpg
  standard: https://i.ytimg.com/vi/-8zYNkI2jEA/sddefault.jpg
  maxres: https://i.ytimg.com/vi/-8zYNkI2jEA/maxresdefault.jpg
---

With the `--wait` command line flag, the 'code' command will only return when the user closes the launched VS Code window.

This lets you integrate VS Code with command line pipelines and scripts. For example:

```bash
$ code --wait myfile ; cat myfile
```