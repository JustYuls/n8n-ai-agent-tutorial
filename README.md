# n8n AI Agent Tutorial for Beginners (Tagalog)

Video 1 of "AI Automation with n8n (Tagalog)". Real n8n 2.47.5 screens (local install), Filipino text-to-speech narration (fil-PH-AngeloNeural, synthetic), try-it-yourself pauses, Sir Yuls presenter.

## Upload (start here)
Open `upload-kit/index.html`: Copy buttons for title, description, chapters, tags and pinned comment. Paste the GitHub link of `workflow/` into the Links box.

## Folders
| Folder | Contents |
|---|---|
| `videos/` | `01_n8n-ai-agent-tutorial-tagalog.mp4` (8:38) |
| `thumbnails/`, `chapters/`, `captions/` | Thumbnail, chapter list, Taglish subtitles (`.srt`) |
| `workflow/` | `reviewer-buddy.json` (import into n8n; credentials removed) and `system-message.txt` |
| `upload-kit/` | `index.html`, `.txt` copies, `playlist.txt` |
| `source/` | `scenes.py` (script), `build_video.py`, `make_thumb.py`, `make_kit.py`, `shots/` (35 real screenshots) |
| `docs/` | `VIDEO_OUTLINE.md`, `SCRIPT_TAGLISH.md` (first draft), `SERIES_PLAN.md` |
| `runtime/` | Local n8n + Ollama data used for the captures (git-ignored; can be deleted, about 1 GB) |

## Rebuild
```
python source/build_video.py     # needs internet for the voice (edge-tts); first run synthesizes the narration
python source/make_thumb.py
python source/make_kit.py
```
To re-capture screens: `npx n8n start` in `runtime/`, `ollama serve`, `ollama pull llama3.2:3b`, then follow `source/scenes.py`. Create the n8n owner account yourself.

## Notes
- The narration was not listened to by the builder. The model is a small 3B model; the video shows its real mistakes.
- Keep a larger model in mind for the next videos; the Telegram part is the planned Part 2.
