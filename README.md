# AI Automation with n8n (Tagalog)

- **Video 0:** How to Install n8n Locally on Windows 11 (Tagalog): Node.js, n8n, Ollama and the local account (7:22)
- **Video 1:** n8n AI Agent Tutorial for Beginners (Tagalog): tools and memory (8:38)
- **Workflow to import:** [`workflow/reviewer-buddy.json`](workflow/reviewer-buddy.json) and [`workflow/system-message.txt`](workflow/system-message.txt)

About the builds: Real n8n 2.47.5 screens (local install), Filipino text-to-speech narration (fil-PH-AngeloNeural, synthetic), try-it-yourself pauses, Sir Yuls presenter.

## Upload (start here)
Open `upload-kit/index.html`: Copy buttons for title, description, chapters, tags and pinned comment. Paste the GitHub link of `workflow/` into the Links box.

## Folders
| Folder | Contents |
|---|---|
| `videos/` | `00_n8n-installation-guide-tagalog.mp4` (7:22), `01_n8n-ai-agent-tutorial-tagalog.mp4` (8:38). Not in git (large) |
| `thumbnails/`, `chapters/`, `captions/` | Thumbnail, chapter list, Taglish subtitles (`.srt`) |
| `workflow/` | `reviewer-buddy.json` (import into n8n; credentials removed) and `system-message.txt` |
| `upload-kit/` | `index.html`, `.txt` copies, `playlist.txt` |
| `source/` | `scenes.py` and `scenes_install.py` (scripts), `build_video.py`, `make_thumb.py`, `make_thumb_install.py`, `make_kit.py`, `shots/` and `shots_install/` (40 real screenshots) |
| `docs/` | `VIDEO_OUTLINE.md`, `SCRIPT_TAGLISH.md` (first draft), `SERIES_PLAN.md` |
| `runtime/` | Local n8n + Ollama data used for the captures (git-ignored; can be deleted, about 1 GB) |

## Rebuild
```
python source/build_video.py                       # video 1; needs internet for the voice (edge-tts)
SCENES=scenes_install python source/build_video.py   # video 0 (PowerShell: $env:SCENES='scenes_install'; python source/build_video.py)
python source/make_thumb.py
python source/make_kit.py
```
To re-capture screens: `npx n8n start` in `runtime/`, `ollama serve`, `ollama pull llama3.2:3b`, then follow `source/scenes.py`. Create the n8n owner account yourself.

## Notes
- The narration was not listened to by the builder. The model is a small 3B model; the video shows its real mistakes.
- Keep a larger model in mind for the next videos; Part 2 puts the same agent on a web page (hosted chat + embedded widget, see chat-page/); Part 3 logs every chat to a CSV that opens in Excel (workflow/study-tracker-excel.json: pick your own Ollama credential, set the file path inside your allowed folder, create study-log.csv from workflow/study-log-header.csv).
