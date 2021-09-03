---
layout: post
title: "Removing keyboard shortcuts"
youtube_video_id: lpsBrzPyFeQ
tags: keybindings
thumbnails:
    default: https://i.ytimg.com/vi/lpsBrzPyFeQ/default.jpg
    medium: https://i.ytimg.com/vi/lpsBrzPyFeQ/mqdefault.jpg
    high: https://i.ytimg.com/vi/lpsBrzPyFeQ/hqdefault.jpg
    standard: https://i.ytimg.com/vi/lpsBrzPyFeQ/sddefault.jpg
    # maxres: https://i.ytimg.com/vi/lpsBrzPyFeQ/maxresdefault.jpg
---

To remove a keyboard shortcut in VS Code :

1. Open keyboard shortcuts editor using `Open keyboard shortcuts` in the command palette.
1. Find the shortcut you wish to remove by searching for the command name or the shortcut itself.
1. Right click on the shortcut and select 'Remove Keybinding'.

This is especially helpful when multiple extensions contribute conflicting shortcuts.

You can also edit the `keybindings.json` file to remove a shortcut. Simply prefix the command you wish to unbind with `-`:

```json
{
	"key": "cmd+\\",
	"command": "-workbench.action.splitEditor"
}
```
