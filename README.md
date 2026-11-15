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
- Part 4 starts a workflow from a webhook call: Webhook, two HTTP Request nodes (Open-Meteo geocoding and forecast, free, no key), Edit Fields, an Ollama AI node and Respond to Webhook (workflow/weather-webhook.json: pick your own Ollama credential, then Execute workflow for the Test URL or Publish for the Production URL). Real terminal outputs and n8n screens are in source/shots_part4. In Windows PowerShell put a backslash before each quote inside the JSON body of curl.exe.
- Part 5 handles errors: workflow/weather-webhook-safe.json (the Advice node has On Error: Continue (using error output) and a Fallback advice node) and workflow/error-logger.json (Error Trigger, Edit Fields, Convert to File, Write File to Disk appending to errors-log.csv). Pick your own Ollama credential, put the log path inside your allowed folder (see Part 3), then set Error Workflow to Error logger in the settings of the main workflow. The error workflow ran only for production calls in my test, not for Execute workflow. Real outputs and screens are in source/shots_part5. source/make_p5_workflows.py rebuilds both files.
- Part 6 runs a workflow by itself with a Schedule Trigger: workflow/daily-weather-report.json (daily 7:00 AM, workflow timezone Asia/Manila; Open-Meteo daily max, min and rain chance, an Ollama advice line with the Part 5 fallback, one CSV line appended to daily-weather.csv). Pick your own Ollama credential, put the path inside your allowed folder, set Error Workflow to Error logger, then Publish: a schedule does nothing until the workflow is published, and the default workflow timezone (America/New_York in my n8n) must be changed. Real outputs and screens are in source/shots_part6. source/make_p6_workflow.py rebuilds the file.
