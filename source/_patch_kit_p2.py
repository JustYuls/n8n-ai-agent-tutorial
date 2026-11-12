import pathlib

p = pathlib.Path(__file__).with_name("make_kit.py")
s = p.read_text(encoding="utf-8")


def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)


rep('("NEXT", "Part 2 link (Telegram bot, when it exists)")]', '("VIDEO2", "Video 2 link (web chatbot)"), ("NEXT", "Part 3 link (Excel study tracker, when it exists)")]')
rep('"Next, Part 2: connect the agent to Telegram: {{NEXT}}",', '"Next, Part 2: put the agent on your own web page: {{VIDEO2}}",')
rep("Next: connect it to Telegram: {{NEXT}}\",", "Next: put it on your web page: {{VIDEO2}}\",")
rep("the playlist or Part 2 when it exists, plus Subscribe.", "Part 2 (the web chatbot), plus Subscribe.")

item2 = r'''    dict(id="02", kind="long", video="videos/02_n8n-chatbot-website-tagalog.mp4", thumb="thumbnails/02_n8n-chatbot-website-tagalog.png",
         chapters="chapters/02_n8n-chatbot-website-tagalog.txt", name="Video 2: n8n Chatbot for Your Website (Tagalog)",
         title="n8n Chatbot for Your Website (Tagalog): Embed Your AI Agent, No Telegram Needed",
         hook="Learn how to put your n8n AI agent on a web page (Tagalog): use the hosted chat link, then embed the chat widget in your own HTML page. Free, local, no Telegram.",
         learn=["How to turn on the public chat of the Chat Trigger, and why the workflow must be Published first",
                "Hosted Chat (a chat page served by n8n) versus Embedded Chat (a widget on your own page)",
                "The page code with the @n8n/chat widget (version pinned) and how to open it with a tiny local web server",
                "Two real mistakes: widget color variables with the wrong name, and page CSS that broke the chat window"],
         resources=["Not installed yet? Setup guide: {{VIDEO0}}", "The agent from Part 1: {{VIDEO1}}",
                    "Chat page (index.html) and workflow: https://github.com/JustYuls/n8n-ai-agent-tutorial/tree/main/chat-page",
                    "n8n chat widget: https://www.npmjs.com/package/@n8n/chat", "Playlist: " + SERIES + ": {{PLAYLIST}}", "Next, Part 3: save the questions and answers in Excel: {{NEXT}}"],
         notes=("Independent guide, not affiliated with n8n or Ollama. Tested with n8n 2.47.5 and @n8n/chat 1.46.4 on my Windows 11 PC (7 GB RAM, no graphics card); the screens and results are real captures from that session. "
                "The chat link is localhost, so it only opens on my own computer, and Authentication was set to None for the demo: add Authentication before sharing any chat link. "
                "Telegram is not used in this part because it is not installed on my PC. Answers take about 20 seconds. Narration is a synthetic voice (Filipino and English text-to-speech) and the presenter is a cartoon."),
         hashtags="#n8n #Chatbot #Tagalog",
         tags=["n8n chatbot website", "n8n chat trigger embedded", "add n8n chatbot to website", "n8n chatbot tutorial", "n8n ai agent tutorial tagalog", "n8n embedded chat",
               "n8n chat widget", "free ai chatbot no api key", "SirYuls TV"],
         pinned="The page code (index.html) is on GitHub, link in the description. Remember: the workflow must be Published, and add Authentication before you share a chat link. "
                "Which website or page will you put your chatbot on? Tell me below. Next: save the answers in Excel: {{NEXT}}",
         settings=["Add to the playlist as video 2", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): Part 3 when it exists, otherwise the playlist, plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English)", "Push the chat-page folder to GitHub before release so the description link works",
                   "Set the Related video of each Short to this video"]),
]

PLAYLIST = dict('''
rep("]\n\nPLAYLIST = dict(", item2)
rep("connect them to Telegram and Google Sheets", "put them on your website and save results to Excel")
rep("2. n8n Telegram AI Bot (coming soon)" + chr(92) + "n3. n8n AI Agent with Google Sheets (coming soon)",
    "2. n8n Chatbot for Your Website (Tagalog)" + chr(92) + "n3. n8n AI Agent with Excel: Study Tracker (coming soon)")
p.write_text(s, encoding="utf-8")
print("kit patched")
