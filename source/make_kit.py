"""Upload kit for "n8n AI Agent Tutorial for Beginners (Tagalog)" (made from series-tools/upload-kit/make_kit_template.py).
Expected project layout: videos/, thumbnails/, chapters/ (one .txt per long video, lines like "0:00 Intro"), upload-kit/ (created).
Generate upload-kit/index.html (copy buttons) and upload-kit/*.txt for the Git and GitHub series.
Run:  python source/make_kit.py      (rerun after rebuilding videos so chapters and durations match)
Edit the ITEMS below to change any title, description, tag or comment.
"""
import json, re, subprocess
from pathlib import Path
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "upload-kit"; KIT.mkdir(exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
SERIES = "AI Automation with n8n (Tagalog)"
NOTES_LONG = ("Independent tutorial, not affiliated with n8n, Ollama or any AI provider. Every screen is a real capture from n8n 2.47.5 running on my computer, "
              "and every result shown (including the mistakes) is the real output of the llama3.2:3b model. Narration is a synthetic voice (Filipino text-to-speech) and the presenter is a cartoon. "
              "The model is small and sometimes confused; use a larger model for more reliable results.")

LINKS = [("PLAYLIST", "Playlist link"), ("VIDEO0", "Video 0 link (installation guide)"), ("VIDEO1", "Video 1 link (AI agent tutorial)"), ("VIDEO2", "Video 2 link (web chatbot)"), ("VIDEO3", "Video 3 link (Excel study tracker)"), ("VIDEO4", "Video 4 link (webhook and API)")]

ITEMS = [
    dict(id="00", kind="long", video="videos/00_n8n-installation-guide-tagalog.mp4", thumb="thumbnails/00_n8n-installation-guide-tagalog.png",
         chapters="chapters/00_n8n-installation-guide-tagalog.txt", name="Video 0: How to Install n8n Locally on Windows 11 (Tagalog)",
         title="How to Install n8n Locally on Windows 11 (Tagalog): Free Setup with Ollama, No Docker",
         hook="Learn how to install n8n on Windows 11 step by step (Tagalog): Node.js, n8n, Ollama and your local account, free and without Docker.",
         learn=["Which Node.js version n8n 2.47.5 needs (24 or newer) and how to check it", "How to install and start n8n with npm, and what to do when it says it is starting up",
                "How to install Ollama and download the llama3.2:3b model (2 GB), with a check that it answers on 127.0.0.1",
                "How to create your local n8n owner account, how to open n8n again later, and what to do if you forget the password"],
         resources=["Node.js: https://nodejs.org/en/download", "Ollama: https://ollama.com/download", "n8n: https://n8n.io",
                    "Playlist: " + SERIES + ": {{PLAYLIST}}", "Next, build the AI agent: {{VIDEO1}}"],
         notes=("Independent guide, not affiliated with n8n, Node.js or Ollama. The download pages and the account form are real captures (the form is shown empty; you create your own account), "
                "and the commands and outputs are the real ones from my Windows 11 PC (7 GB RAM, no graphics card). I tested n8n 2.47.5 on Node.js 24.19.0 and did not test Node.js 26. "
                "Install times and speeds depend on your computer and internet. Narration is a synthetic voice (Filipino text-to-speech) and the presenter is a cartoon."),
         hashtags="#n8n #Ollama #Tagalog",
         tags=["how to install n8n locally on windows 11", "n8n install windows free", "n8n setup tagalog", "install n8n without docker", "how to install ollama on windows 11",
               "n8n installation guide", "n8n tutorial for beginners tagalog", "install node js windows 11", "SirYuls TV"],
         pinned="Commands from the video:\nnode -v   (must be 24 or newer)\nnpm install n8n\nnpx n8n start   (open http://localhost:5678)\nollama pull llama3.2:3b\nOllama address in n8n: http://127.0.0.1:11434\n"
                "Stuck? Tell me which step and what you see. Next: build the AI agent: {{VIDEO1}}",
         settings=["Add to the playlist as video 0 (first)", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): Video 1 (the AI agent tutorial), plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English)", "Set the Related video of each Short to this video"]),
    dict(id="01", kind="long", video="videos/01_n8n-ai-agent-tutorial-tagalog.mp4", thumb="thumbnails/01_n8n-ai-agent-tutorial-tagalog.png",
         chapters="chapters/01_n8n-ai-agent-tutorial-tagalog.txt", name="Video 1: n8n AI Agent Tutorial for Beginners (Tagalog)",
         title="n8n AI Agent Tutorial for Beginners (Tagalog): Build an AI Assistant That Uses Tools",
         hook="Learn how to build an AI agent in n8n step by step (Tagalog): connect a free local AI model, add tools like Calculator and Wikipedia, and give it memory.",
         learn=["The difference between a chatbot, a workflow and an AI agent", "Chat Trigger, AI Agent and Ollama Chat Model nodes, with no API key",
                "Why a vague system message gives a wrong answer (2414.72) and a clear one gives the right one (2250.08)",
                "Simple Memory, so the agent remembers the conversation, and how to read the Executions log"],
         resources=["Not installed yet? Setup guide: {{VIDEO0}}", "Workflow JSON and the system message (copy-paste): https://github.com/JustYuls/n8n-ai-agent-tutorial/tree/main/workflow", "Playlist: " + SERIES + ": {{PLAYLIST}}", "Next, Part 2: put the agent on your own web page: {{VIDEO2}}",
                    "n8n: https://n8n.io    Ollama: https://ollama.com"],
         notes=NOTES_LONG, hashtags="#n8n #AIAgent #Tagalog",
         tags=["n8n ai agent tutorial", "n8n tutorial for beginners tagalog", "ai agent tutorial tagalog", "n8n tutorial", "n8n ai agent", "n8n chat trigger",
               "ai automation tagalog", "free ai agent no api key", "SirYuls TV"],
         pinned="Workflow file and the full system message are in the description. The model is small, so it sometimes gets confused; a larger model is more reliable. "
                "Which tool should I add to the agent next? Tell me below. Not installed yet? Setup guide: {{VIDEO0}}  Next: put it on your web page: {{VIDEO2}}",
         settings=["Add to the playlist as video 1", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): Part 2 (the web chatbot), plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English). The narration is Taglish, so also upload it as the Filipino/English caption track if you prefer",
                   "Put reviewer-buddy.json and the system message on GitHub before release, then paste its link above",
                   "Set the Related video of each Short to this video"]),
    dict(id="02", kind="long", video="videos/02_n8n-chatbot-website-tagalog.mp4", thumb="thumbnails/02_n8n-chatbot-website-tagalog.png",
         chapters="chapters/02_n8n-chatbot-website-tagalog.txt", name="Video 2: n8n Chatbot for Your Website (Tagalog)",
         title="n8n Chatbot for Your Website (Tagalog): Embed Your AI Agent, No Telegram Needed",
         hook="Learn how to put your n8n AI agent on a web page (Tagalog): use the hosted chat link, then embed the chat widget in your own HTML page. Free, local, no Telegram.",
         learn=["How to turn on the public chat of the Chat Trigger, and why the workflow must be Published first",
                "Hosted Chat (a chat page served by n8n) versus Embedded Chat (a widget on your own page)",
                "The page code with the @n8n/chat widget (version pinned) and how to open it with a tiny local web server",
                "Two real mistakes: widget color variables with the wrong name, and page CSS that broke the chat window"],
         resources=["Not installed yet? Setup guide: {{VIDEO0}}", "The agent from Part 1: {{VIDEO1}}",
                    "Chat page (index.html) and workflow: https://github.com/JustYuls/n8n-ai-agent-tutorial/tree/main/chat-page",
                    "n8n chat widget: https://www.npmjs.com/package/@n8n/chat", "Playlist: " + SERIES + ": {{PLAYLIST}}", "Next, Part 3: save the questions and answers in Excel: {{VIDEO3}}"],
         notes=("Independent guide, not affiliated with n8n or Ollama. Tested with n8n 2.47.5 and @n8n/chat 1.46.4 on my Windows 11 PC (7 GB RAM, no graphics card); the screens and results are real captures from that session. "
                "The chat link is localhost, so it only opens on my own computer, and Authentication was set to None for the demo: add Authentication before sharing any chat link. "
                "Telegram is not used in this part because it is not installed on my PC. Answers take about 20 seconds. Narration is a synthetic voice (Filipino and English text-to-speech) and the presenter is a cartoon."),
         hashtags="#n8n #Chatbot #Tagalog",
         tags=["n8n chatbot website", "n8n chat trigger embedded", "add n8n chatbot to website", "n8n chatbot tutorial", "n8n ai agent tutorial tagalog", "n8n embedded chat",
               "n8n chat widget", "free ai chatbot no api key", "SirYuls TV"],
         pinned="The page code (index.html) is on GitHub, link in the description. Remember: the workflow must be Published, and add Authentication before you share a chat link. "
                "Which website or page will you put your chatbot on? Tell me below. Next: save the answers in Excel: {{VIDEO3}}",
         settings=["Add to the playlist as video 2", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): Part 3 (the Excel study tracker), plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English)", "Push the chat-page folder to GitHub before release so the description link works",
                   "Set the Related video of each Short to this video"]),
    dict(id="03", kind="long", video="videos/03_n8n-ai-agent-excel-study-tracker-tagalog.mp4", thumb="thumbnails/03_n8n-ai-agent-excel-study-tracker-tagalog.png",
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
    dict(id="04", kind="long", video="videos/04_n8n-webhook-api-tagalog.mp4", thumb="thumbnails/04_n8n-webhook-api-tagalog.png",
         chapters="chapters/04_n8n-webhook-api-tagalog.txt", name="Video 4: n8n Webhook and API Tutorial (Tagalog)",
         title="n8n Webhook Tutorial for Beginners (Tagalog): Call a Free Weather API with AI Advice",
         hook="Learn how to start an n8n workflow with a webhook call (Tagalog): receive a city name, call the free Open-Meteo API, let a local AI write one line of advice, and send the answer back. No account, no API key.",
         learn=["What a webhook and an API are, and how the Webhook node, two HTTP Request nodes, Edit Fields, an AI node and Respond to Webhook fit together",
                "Test URL versus Production URL: why the second Test URL call gives 404, and why the production URL needs Publish",
                "Real mistakes: listening on the node only (empty answer), an API timeout fixed with Retry On Fail, and broken JSON quotes in PowerShell (422)",
                "How to answer a wrong city name with a 404 branch, and how to check the numbers against the API (28.1 degrees and 68 percent matched)"],
         resources=["Not installed yet? Setup guide: {{VIDEO0}}", "The agent from Part 1: {{VIDEO1}}", "Part 3, the Excel tracker: {{VIDEO3}}",
                    "Workflow JSON (Weather Webhook): https://github.com/JustYuls/n8n-ai-agent-tutorial/tree/main/workflow",
                    "Open-Meteo (free weather API): https://open-meteo.com", "Playlist: " + SERIES + ": {{PLAYLIST}}"],
         notes=("Independent guide, not affiliated with n8n, Open-Meteo or Ollama. Tested with n8n 2.47.5 on my Windows 11 PC (7 GB RAM, no graphics card); the n8n screens and every terminal output are real, including the mistakes. "
                "Weather data from Open-Meteo.com (CC BY 4.0). The geocoding API was slow while I recorded, and that timeout is real. The advice line comes from a small local model (llama3.2:3b) and can be wrong: it mentioned rain that was not in the data. "
                "Import the workflow file and pick your own Ollama account in the Ollama Chat Model node. Narration is a synthetic voice (Filipino text-to-speech) and the presenter is a cartoon."),
         hashtags="#n8n #Webhook #Tagalog",
         tags=["n8n webhook tutorial", "n8n webhook tagalog", "n8n http request tutorial", "n8n respond to webhook", "n8n test url vs production url", "n8n weather api",
               "open-meteo n8n", "n8n tutorial for beginners tagalog", "n8n retry on fail", "SirYuls TV"],
         pinned="The workflow file is on GitHub, link in the description. Remember: the Test URL works once after Execute workflow, and the Production URL needs Publish. "
                "In PowerShell, put a backslash before each quote inside the JSON. Which API will you connect next? Tell me below. Full playlist: {{PLAYLIST}}",
         settings=["Add to the playlist as video 4", "Not made for kids", "Altered or synthetic content: yes (synthetic voice, cartoon presenter)",
                   "End screen (last 15 to 20 s): the playlist, plus Subscribe. The right half of the last slide is clear",
                   "Upload the thumbnail and captions/ .srt (Subtitles, English)", "Push workflow/weather-webhook.json to GitHub before release so the description link works",
                   "Set the Related video of each Short to this video"]),
]

PLAYLIST = dict(
    title=SERIES,
    description=("Learn n8n step by step in Tagalog: build AI agents, put them on your website and save results to Excel, and automate your study or work.\n\n"
                 "Watch in order:\n0. How to Install n8n Locally on Windows 11 (Tagalog)\n1. n8n AI Agent Tutorial for Beginners (Tagalog)\n2. n8n Chatbot for Your Website (Tagalog)\n3. n8n AI Agent to Excel: Study Tracker (Tagalog)\n4. n8n Webhook Tutorial: Call a Free Weather API (Tagalog)\n\n" + NOTES_LONG),
)


def duration(path):
    r = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", r.stderr)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3]) if m else 0.0


def secs(t):
    p = [int(x) for x in t.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]


def fmt(s): return f"{int(s // 60)}:{int(s % 60):02d}"


warnings = []
for it in ITEMS:
    vp = ROOT / it["video"]
    it["duration"] = duration(vp) if vp.exists() else 0
    it["duration_text"] = fmt(it["duration"])
    it["tags_text"] = ", ".join(it["tags"])
    if it["kind"] == "long":
        ch = (ROOT / it["chapters"]).read_text(encoding="utf-8").strip()
        it["chapters_text"] = ch
        times = [secs(l.split()[0]) for l in ch.splitlines()]
        ends = times[1:] + [it["duration"]]
        if times[0] != 0 or len(times) < 3 or any(e - s < 10 for s, e in zip(times, ends)):
            warnings.append(f"{it['id']}: chapters break YouTube rules")
        it["description"] = "\n\n".join([it["hook"], "What you'll learn:\n" + "\n".join("- " + x for x in it["learn"]), ch, "\n".join(it["resources"]), it["notes"], it["hashtags"]])
    else:
        it["chapters_text"] = ""
        it["description"] = it["desc_short"] + "\n\n" + it["hashtags"]
    for label, val in (("title", it["title"]), ("description", it["description"]), ("tags", it["tags_text"])):
        if "<" in val or ">" in val: warnings.append(f"{it['id']}: '<' or '>' in {label} (YouTube rejects it)")
    if len(it["title"]) > 100: warnings.append(f"{it['id']}: title over 100 characters")
    if len(it["tags_text"]) > 500: warnings.append(f"{it['id']}: tags over 500 characters")
    if len(it["description"]) > 5000: warnings.append(f"{it['id']}: description over 5000 characters")

# plain-text files
for it in ITEMS:
    parts = [f"{it['name']}  ({it['duration_text']})", f"Video: {it['video']}", f"Thumbnail: {it['thumb'] or 'none (Shorts)'}", "",
             "=== TITLE ===", it["title"], "", "=== DESCRIPTION ===", it["description"], "", "=== TAGS ===", it["tags_text"], "", "=== PINNED COMMENT ===", it["pinned"], "",
             "=== SETTINGS ==="] + ["- " + s for s in it["settings"]]
    slug = Path(it["video"]).stem
    (KIT / f"{slug}.txt").write_text("\n".join(parts) + "\n", encoding="utf-8")
(KIT / "playlist.txt").write_text(f"=== PLAYLIST TITLE ===\n{PLAYLIST['title']}\n\n=== PLAYLIST DESCRIPTION ===\n{PLAYLIST['description']}\n", encoding="utf-8")

DATA = dict(items=ITEMS, playlist=PLAYLIST, links=LINKS)
HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>n8n AI Agent Tutorial: upload kit</title>
<style>
:root{--bg:#f4f6fb;--card:#fff;--ink:#0b1f4b;--mut:#5b6b8c;--line:#d8def0;--acc:#ffd21f;--accink:#0b1f4b;--ok:#1a7f37;--warn:#b54708;--field:#f8f9fd}
@media (prefers-color-scheme:dark){:root{--bg:#07122e;--card:#0f2150;--ink:#eef2ff;--mut:#9db0d8;--line:#23356b;--field:#0a1840;--ok:#7ee787;--warn:#ffb86b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,Segoe UI,Arial,sans-serif}
.wrap{max-width:980px;margin:0 auto;padding:24px 16px 80px}h1{margin:0 0 4px;font-size:28px}h2{margin:0;font-size:22px}
.sub{color:var(--mut);margin:0 0 20px}.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px;margin:16px 0}
.links{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}.links label{font-size:13px;color:var(--mut);display:block}
input[type=text]{width:100%;padding:8px 10px;border-radius:10px;border:1px solid var(--line);background:var(--field);color:var(--ink);font:inherit}
.head{display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap;margin-bottom:8px}.head img{width:240px;max-width:100%;border-radius:10px;border:1px solid var(--line)}
.meta{color:var(--mut);font-size:14px}.meta code{background:var(--field);padding:1px 6px;border-radius:6px}
.tag{display:inline-block;background:var(--acc);color:var(--accink);font-weight:700;border-radius:999px;padding:2px 12px;font-size:13px;margin-right:6px}
.field{margin:12px 0}.field .row{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:4px}
.field label{font-weight:700}.cnt{color:var(--mut);font-size:13px;margin-left:8px;font-weight:400}.miss{color:var(--warn);font-size:13px;margin-left:8px;font-weight:600}
textarea{width:100%;border:1px solid var(--line);border-radius:10px;background:var(--field);color:var(--ink);padding:10px;font:14px/1.45 ui-monospace,Consolas,monospace;resize:vertical}
button{border:0;background:var(--acc);color:var(--accink);font-weight:700;border-radius:10px;padding:8px 16px;cursor:pointer;font:inherit;font-weight:700}
button:hover{filter:brightness(.95)}button.done{background:var(--ok);color:#fff}
ul.set{margin:6px 0 0 18px;padding:0;color:var(--mut);font-size:14px}.steps{margin:0;padding-left:20px;color:var(--mut)}
</style></head><body><div class="wrap">
<h1>n8n AI Agent Tutorial (Tagalog): upload kit</h1>
<p class="sub">Upload the video, then use each Copy button and paste into YouTube Studio. Paste your video links in the box below after you upload, and every field fills in.</p>
<div class="card"><ol class="steps"><li>Upload the video, then use each Copy button.</li><li>For each video: Copy title, description, tags, then upload the thumbnail file.</li><li>After a video is live, paste its link below. The next descriptions update automatically.</li><li>Create the playlist first or last, and paste its link too.</li></ol></div>
<div class="card"><h2>Links (fill in as you go)</h2><div class="links" id="links"></div></div>
<div id="items"></div>
<div class="card"><h2>Playlist</h2><div id="playlist"></div></div>
</div>
<script>
const DATA=__DATA__;
const links={};try{Object.assign(links,JSON.parse(localStorage.getItem("n8nkit-links")||"{}"))}catch(e){}
const fields=[];
function fill(t){return t.replace(/\{\{(\w+)\}\}/g,(m,k)=>links[k]||m)}
function missing(t){return (fill(t).match(/\{\{\w+\}\}/g)||[]).length}
function mkField(parent,label,text,rows,limit){
  const d=document.createElement("div");d.className="field";
  d.innerHTML='<div class="row"><div><label></label><span class="cnt"></span><span class="miss"></span></div><button type="button">Copy</button></div><textarea readonly></textarea>';
  d.querySelector("label").textContent=label;const ta=d.querySelector("textarea");ta.rows=rows;
  const btn=d.querySelector("button"),cnt=d.querySelector(".cnt"),miss=d.querySelector(".miss");
  function upd(){const v=fill(text);ta.value=v;ta.style.height="auto";ta.style.height=(ta.scrollHeight+6)+"px";cnt.textContent=v.length+(limit?" / "+limit:"")+" characters";const m=missing(text);miss.textContent=m?m+" link(s) still to paste":""}
  btn.onclick=async()=>{const v=ta.value;try{await navigator.clipboard.writeText(v)}catch(e){ta.select();document.execCommand("copy")}
    btn.textContent="Copied";btn.classList.add("done");setTimeout(()=>{btn.textContent="Copy";btn.classList.remove("done")},1500)};
  ta.onfocus=()=>ta.select();upd();fields.push(upd);parent.appendChild(d)}
const L=document.getElementById("links");
DATA.links.forEach(([k,label])=>{const w=document.createElement("div");w.innerHTML='<label></label><input type="text" placeholder="https://youtu.be/...">';
  w.querySelector("label").textContent=label;const i=w.querySelector("input");i.value=links[k]||"";
  i.oninput=()=>{links[k]=i.value.trim();try{localStorage.setItem("n8nkit-links",JSON.stringify(links))}catch(e){}fields.forEach(f=>f())};L.appendChild(w)});
const box=document.getElementById("items");
DATA.items.forEach(it=>{const c=document.createElement("div");c.className="card";
  const head=document.createElement("div");head.className="head";
  head.innerHTML=(it.thumb?'<a download href="../'+it.thumb+'"><img src="../'+it.thumb+'" alt="thumbnail"></a>':"")+'<div><span class="tag"></span><h2></h2><div class="meta"></div></div>';
  head.querySelector(".tag").textContent=it.kind==="short"?"SHORT "+it.id:"VIDEO "+it.id;head.querySelector("h2").textContent=it.name;
  head.querySelector(".meta").innerHTML='Length '+it.duration_text+'<br>Video file: <code></code>'+(it.thumb?'<br>Thumbnail: <code class="t"></code> (click the image to download)':'<br>Shorts use a frame from the video')+'<ul class="set"></ul>';
  head.querySelector("code").textContent=it.video;if(it.thumb)head.querySelector(".t").textContent=it.thumb;
  it.settings.forEach(s=>{const li=document.createElement("li");li.textContent=s;head.querySelector(".set").appendChild(li)});
  c.appendChild(head);
  mkField(c,"Title",it.title,2,100);
  mkField(c,"Description",it.description,it.kind==="short"?7:20,5000);
  if(it.chapters_text)mkField(c,"Chapters only",it.chapters_text,Math.min(10,it.chapters_text.split("\n").length+1));
  mkField(c,"Tags",it.tags_text,3,500);
  mkField(c,"Pinned comment",it.pinned,3);
  box.appendChild(c)});
const P=document.getElementById("playlist");mkField(P,"Playlist title",DATA.playlist.title,2);mkField(P,"Playlist description",DATA.playlist.description,10);
const n=document.createElement("p");n.className="meta";n.textContent="YouTube has no playlist cover upload. The playlist shows the thumbnail of its first video.";P.appendChild(n);
fields.forEach(f=>f());window.addEventListener("resize",()=>fields.forEach(f=>f()));
</script></body></html>"""
(KIT / "index.html").write_text(HTML.replace("__DATA__", json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")), encoding="utf-8")
print("kit written;", "warnings:" if warnings else "no warnings", *warnings, sep="\n  ")
for it in ITEMS: print(it["id"], it["duration_text"], len(it["title"]), "title chars,", len(it["tags_text"]), "tag chars,", len(it["description"]), "desc chars")
