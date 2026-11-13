import pathlib

p = pathlib.Path(__file__).with_name("make_kit.py")
s = p.read_text(encoding="utf-8")


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)


rep('("NEXT", "Part 3 link (Excel study tracker, when it exists)")]', '("VIDEO3", "Video 3 link (Excel study tracker)")]')
rep('Next, Part 3: save the questions and answers in Excel: {{NEXT}}', 'Next, Part 3: save the questions and answers in Excel: {{VIDEO3}}')
rep('Next: save the answers in Excel: {{NEXT}}', 'Next: save the answers in Excel: {{VIDEO3}}')
rep("End screen (last 15 to 20 s): Part 3 when it exists, otherwise the playlist, plus Subscribe.", "End screen (last 15 to 20 s): Part 3 (the Excel study tracker), plus Subscribe.")

item3 = r'''    dict(id="03", kind="long", video="videos/03_n8n-ai-agent-excel-study-tracker-tagalog.mp4", thumb="thumbnails/03_n8n-ai-agent-excel-study-tracker-tagalog.png",
         chapters="chapters/03_n8n-ai-agent-excel-study-tracker-tagalog.txt", name="Video 3: n8n AI Agent to Excel Study Tracker (Tagalog)",
         title="n8n AI Agent to Excel (Tagalog): Save Every Chat in a Study Tracker, No Google Sheets",
         hook="Learn how to save every question and answer of your n8n AI agent in a CSV file that opens in Excel (Tagalog): Edit Fields, Convert to File and Write File to Disk. Free, local, no Google account.",
         learn=["How to add Edit Fields, Convert to File and Write File to Disk after the AI Agent, and append one row per chat",
                "Why CSV can be appended and XLSX cannot, and how to open the CSV in Excel",
                "Four real mistakes: file path not allowed, expressions saved as plain text, the wrong time zone, and rows glued together without a newline",
                "How to send the agent answer back to the chat, and why you should still check the answers (the small model got 15% of 3200 wrong)"],
         resources=["Not installed yet? Setup guide: {{VIDEO0}}", "The agent from Part 1: {{VIDEO1}}", "Part 2, the web chatbot: {{VIDEO2}}",
                    "Workflow JSON (Study Tracker): https://github.com/JustYuls/n8n-ai-agent-tutorial/tree/main/workflow",
                    "n8n file access setting (N8N_RESTRICT_FILE_ACCESS_TO): https://docs.n8n.io/hosting/configuration/environment-variables/security/",
                    "Playlist: " + SERIES + ": {{PLAYLIST}}"],
         notes=("Independent guide, not affiliated with n8n, Microsoft or Ollama. Tested with n8n 2.47.5 and Microsoft Excel on my Windows 11 PC (7 GB RAM, no graphics card); the n8n screens, the file contents and the Excel window are real captures from that session. "
                "I set N8N_RESTRICT_FILE_ACCESS_TO to my own folder; the default allowed folder is ~/.n8n-files. Answers take about 30 to 45 seconds. The small model can give wrong answers, so check them. "
                "Narration is a synthetic voice (Filipino text-to-speech) and the presenter is a cartoon."),
         hashtags="#n8n #Excel #Tagalog",
         tags=["n8n ai agent excel", "n8n write file to disk", "n8n convert to file csv", "n8n append to csv", "n8n study tracker", "n8n google sheets alternative",
               "n8n ai agent tutorial tagalog", "save chat to excel", "SirYuls TV"],
         pinned="The workflow file is on GitHub, link in the description. Remember: n8n can only write inside the folder you allow, and check the answers of the small model (15% of 3200 is 480, not 2720). "
                "What questions will you log in your tracker? Tell me below. Full playlist: {{PLAYLIST}}",
         settings=["Add to the playlist as video 3", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): the playlist, plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English)", "Push workflow/study-tracker-excel.json to GitHub before release so the description link works",
                   "Set the Related video of each Short to this video"]),
]

PLAYLIST = dict('''
rep("]\n\nPLAYLIST = dict(", item3)
rep("3. n8n AI Agent with Excel: Study Tracker (coming soon)", "3. n8n AI Agent to Excel: Study Tracker (Tagalog)")
p.write_text(s, encoding="utf-8")
print("kit patched")
