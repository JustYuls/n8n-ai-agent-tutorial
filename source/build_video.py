"""Build "n8n AI Agent Tutorial for Beginners (Tagalog)" (1920x1080).
Real n8n screenshots (source/shots) + highlight boxes + Filipino narration (edge-tts fil-PH-AngeloNeural, synthetic) + try-it-yourself pauses
+ original music, then the Sir Yuls presenter. Subtitle bar on every frame. Keep x <= 1540 below y 740 (presenter sits lower right).
Usage: python build_video.py            -> videos/01_n8n-ai-agent-tutorial-tagalog.mp4, chapters/, captions/, thumbnails/
"""
import asyncio
import hashlib
import importlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import edge_tts
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, "D:/MIT/SirYulsTV")
sys.path.insert(0, str(HERE))
import make_long as ml  # noqa: E402  (relaxing music bed + mixer)
import make_short as ms  # noqa: E402  (fonts, wrap, colors)
_mod = importlib.import_module(os.environ.get('SCENES', 'scenes'))  # scenes (video 1) or scenes_install (video 0)
SCENES, SYSTEM_MESSAGE = _mod.SCENES, _mod.SYSTEM_MESSAGE

W, H, FPS = 1920, 1080, 30
NAVY, YELLOW, WHITE, GREEN, CARD = ms.NAVY, ms.YELLOW, ms.WHITE, ms.GREEN, ms.CARD
MUTED, RED, PINK = "#9DB0D8", "#FF6B6B", "#FF8FB1"
VOICE = "fil-PH-AngeloNeural"
SHOTS = HERE / "shots"
SHOTS_INSTALL = HERE / "shots_install"
SHOTS_PART2 = HERE / "shots_part2"
SHOTS_PART3 = HERE / "shots_part3"
SHOTS_PART4 = HERE / "shots_part4"
TTS = HERE / "_tts"
TTS.mkdir(exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
NAME = getattr(_mod, "NAME", "01_n8n-ai-agent-tutorial-tagalog")
PRESENTER = Path("D:/MIT/series-tools/efcore/presenter.py")
f = ms.font
MONO = "C:/Windows/Fonts/consolab.ttf"
S = 1500 / 1440
X0, Y0 = 40, 118


def fm(size):
    return ImageFont.truetype(MONO, size)


def m(x, y):
    return X0 + x * S, Y0 + y * S


# ---------------------------------------------------------------- voice
EN_VOICE = "en-US-AndrewNeural"
MIXED = bool(getattr(_mod, "MIXED", False))
EN_TERMS = list(getattr(_mod, "EN_TERMS", []))
EN_RE = re.compile("(?<![A-Za-z])(" + "|".join(sorted((t if t.startswith("(?") else re.escape(t) for t in EN_TERMS), key=len, reverse=True)) + ")(?![A-Za-z])", re.I) if EN_TERMS else None


def _synth(text, voice):
    key = hashlib.sha1(f"{voice}|{text}".encode()).hexdigest()[:16]
    wav = TTS / f"{key}.wav"
    if wav.exists():
        return wav
    mp3 = TTS / f"{key}.mp3"
    for attempt in range(4):
        try:
            asyncio.run(edge_tts.Communicate(text, voice, rate="-4%").save(str(mp3)))
            break
        except Exception as e:  # network hiccup: retry
            if attempt == 3:
                raise
            print("tts retry", attempt, type(e).__name__)
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(mp3), "-ac", "1", "-ar", "24000", str(wav)], check=True)
    mp3.unlink()
    return wav


def tts(text):
    if not (MIXED and EN_RE):
        return _synth(text, VOICE)
    # mixed voice: English technical terms are spoken by an English voice, the rest by the Filipino voice
    key = hashlib.sha1(f"mixed|{VOICE}|{EN_VOICE}|{text}".encode()).hexdigest()[:16]
    out = TTS / f"{key}.wav"
    if out.exists():
        return out
    parts = [(seg, bool(EN_RE.fullmatch(seg))) for seg in EN_RE.split(text) if seg and seg.strip()]
    frames, params = [], None
    for seg, is_en in parts:
        seg = seg.strip().rstrip('-').strip()
        if not re.search(r"\w", seg):
            continue
        w = _synth(seg, EN_VOICE if is_en else VOICE)
        with wave.open(str(w)) as wf:
            params = wf.getparams()
            frames.append(wf.readframes(wf.getnframes()))
    with wave.open(str(out), "wb") as wo:
        wo.setparams(params)
        for fr in frames:
            wo.writeframes(fr)
    return out


def wav_len(p):
    with wave.open(str(p)) as w:
        return w.getnframes() / w.getframerate()


# ---------------------------------------------------------------- drawing helpers
def canvas():
    img = Image.new("RGB", (W, H), NAVY)
    return img, ImageDraw.Draw(img)


def chip(d, text, x, y, size=34, fill=YELLOW, ink=NAVY):
    w = d.textlength(text, font=f(size)) + 50
    d.rounded_rectangle((x, y, x + w, y + size + 26), (size + 26) // 2, fill=fill)
    d.text((x + 25, y + 10), text, font=f(size), fill=ink)
    return x + w


def wrap_draw(d, text, x, y, size, fill, max_w, gap=0.22, mono=False):
    fnt = fm(size) if mono else f(size)
    for line in ms.wrap(d, text, fnt, max_w):
        d.text((x, y), line, font=fnt, fill=fill)
        y += int(size * (1 + gap))
    return y


def frame_base(step):
    img, d = canvas()
    red = "MISTAKE" in step or "MALI" in step
    chip(d, step, 40, 36, fill=RED if red else YELLOW)
    d.text((40, H - 46), "SirYuls TV  |  n8n AI Agent Tutorial (Tagalog)", font=f(26), fill=MUTED)
    return img, d


def subtitle(d, text):
    if not text:
        return
    d.rounded_rectangle((40, 838, 1540, 1010), 28, fill=CARD)
    size = 40 if len(text) < 110 else 34
    wrap_draw(d, text, 70, 858, size, WHITE, 1440, 0.2)


def badge(d, n, cx, cy):
    d.ellipse((cx - 17, cy - 17, cx + 17, cy + 17), fill=YELLOW)
    t = str(n)
    d.text((cx - d.textlength(t, font=f(24)) / 2, cy - 15), t, font=f(24), fill=NAVY)


def notes_card(d, notes, nhl):
    d.rounded_rectangle((1565, 118, 1880, 736), 28, fill=CARD)
    y = 140
    for i, n in enumerate(notes):
        if i < nhl:
            badge(d, i + 1, 1595, y + 20)
            ty = wrap_draw(d, n, 1625, y, 28, WHITE, 240, 0.18)
        else:
            ty = wrap_draw(d, n, 1585, y, 28, YELLOW, 270, 0.18)
        y = max(ty, y + 44) + 22


def draw_hl(d, rects, conv):
    for i, r in enumerate(rects):
        x0, y0 = conv(r[0], r[1])
        x1, y1 = conv(r[2], r[3])
        d.rounded_rectangle((x0 - 4, y0 - 4, x1 + 4, y1 + 4), 12, outline=YELLOW, width=5)
        badge(d, i + 1, x0 - 4, y0 - 4)


def shot_img(name):
    for base in (SHOTS_PART4, SHOTS_PART3, SHOTS_PART2, SHOTS_INSTALL, SHOTS):
        if (base / f"{name}.jpg").exists():
            return Image.open(base / f"{name}.jpg").convert("RGB")
    raise FileNotFoundError(name)


def frame_shot(sc, sub=""):
    img, d = frame_base(sc["step"])
    src = shot_img(sc["img"])
    k = min(1500 / src.width, 703 / src.height)
    pw, ph = round(src.width * k), round(src.height * k)
    ox, oy = X0 + (1500 - pw) // 2, Y0
    img.paste(src.resize((pw, ph), Image.LANCZOS), (ox, oy))
    d.rectangle((ox - 2, oy - 2, ox + pw + 1, oy + ph + 1), outline="#3B4F8A", width=2)
    draw_hl(d, sc.get("hl", []), lambda x, y: (ox + x * k, oy + y * k))
    notes_card(d, sc.get("note", []), len(sc.get("hl", [])))
    subtitle(d, sub)
    return img


def frame_zoom(sc, sub=""):
    img, d = frame_base(sc["step"])
    x0, y0, x1, y1 = sc["crop"]
    cw, ch = x1 - x0, y1 - y0
    zs = 1500 / cw
    pic = shot_img(sc["img"]).crop((x0, y0, x1, y1)).resize((1500, round(ch * zs)), Image.LANCZOS)
    img.paste(pic, (X0, 130))
    d.rectangle((X0 - 2, 128, X0 + 1501, 130 + pic.height + 1), outline="#3B4F8A", width=2)
    draw_hl(d, sc["hl"], lambda x, y: (X0 + (x - x0) * zs, 130 + (y - y0) * zs))
    yy = 130 + pic.height + 30
    yy = wrap_draw(d, sc["caption"], 40, yy, 44, YELLOW, 1500, 0.2, mono=False)
    wrap_draw(d, sc["sub"], 40, yy + 8, 38, WHITE, 1500, 0.2)
    subtitle(d, sub)
    return img


def frame_terminal(sc, sub=""):
    img, d = frame_base(sc["step"])
    lines = sc["lines"]
    lh = 60
    h = 110 + lh * len(lines)
    top = 130
    d.rounded_rectangle((40, top, 1520, top + h), 22, fill="#0A1636", outline="#3B4F8A", width=3)
    d.rounded_rectangle((40, top, 1520, top + 64), 22, fill="#12214A")
    for i, c in enumerate(["#F87171", "#FACC15", "#4ADE80"]):
        d.ellipse((70 + i * 40, top + 20, 90 + i * 40, top + 40), fill=c)
    d.text((220, top + 14), sc.get("title", "Windows PowerShell"), font=f(28), fill=MUTED)
    y = top + 90
    for kind, text in lines:
        if kind == "cmd":
            d.text((70, y), "PS>", font=fm(36), fill="#38BDF8")
            d.text((70 + d.textlength("PS> ", font=fm(36)), y), text, font=fm(36), fill="#FFFFFF")
        elif kind == "ok":
            d.text((70, y), text, font=fm(36), fill=GREEN)
        elif kind == "note":
            d.text((70, y), text, font=fm(32), fill="#7B8DB5")
        else:
            d.text((70, y), text, font=fm(36), fill="#CBD5E1")
        y += lh
    if sc.get("note"):
        nw = d.textlength(sc["note"], font=f(30)) + 50
        chip(d, sc["note"], 1520 - nw - 20, top + 10, size=30, fill=CARD, ink=YELLOW)
    subtitle(d, sub)
    return img


def slide_hook_checks():
    img, d = frame_base("RESULTA")
    d.text((40, 110), "Pagkatapos ng video na ito", font=f(76), fill=WHITE)
    rows = [("Node.js 24 o mas bago", "node -v  =  v24.19.0"), ("n8n sa computer mo", "http://localhost:5678"), ("Ollama + llama3.2:3b", "ollama list  =  llama3.2:3b"),
            ("Sarili mong n8n account", "local, nasa computer mo")]
    y = 230
    for a, b in rows:
        d.rounded_rectangle((40, y, 1520, y + 130), 28, fill=CARD)
        d.rounded_rectangle((70, y + 35, 130, y + 95), 14, fill=GREEN)
        d.text((82, y + 40), "OK", font=f(34), fill=NAVY)
        d.text((165, y + 22), a, font=f(46), fill=WHITE)
        d.text((165, y + 82), b, font=fm(28), fill=GREEN)
        y += 150
    return img, d


def slide_requirements():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang kailangan mo", font=f(76), fill=WHITE)
    rows = [("Windows 10 o 11", "at internet para sa mga download"), ("RAM", "7 GB ang sa akin (walang GPU): gumagana, pero mabagal"), ("Espasyo", "Ang AI model lang ay 2 GB; maglaan ng ilang GB"),
            ("Node.js 24 o mas bago", "kailangan ng n8n 2.47.5")]
    y = 230
    for a, b in rows:
        d.rounded_rectangle((40, y, 1520, y + 120), 26, fill=CARD)
        d.text((70, y + 14), a, font=f(42), fill=YELLOW)
        d.text((70, y + 70), b, font=f(32), fill=WHITE)
        y += 135
    d.text((40, 780), "1 Node.js   2 n8n   3 Ollama at model   4 Account", font=f(38), fill=YELLOW)
    return img, d


def slide_account_tips():
    img, d = frame_base("BAGO KA MAG-SUBMIT")
    d.text((40, 110), "3 paalala sa account", font=f(76), fill=WHITE)
    rows = [("1", "Ikaw mismo ang mag-type ng password", "Gumamit ng maaalala mo. Huwag ibigay sa iba."), ("2", "Local ang account", "Nasa computer mo ito, hindi sa cloud."),
            ("3", "Huwag i-expose ang port 5678", "Sa computer mo lang buksan, sa localhost.")]
    y = 250
    for n, a, b in rows:
        d.rounded_rectangle((40, y, 1520, y + 190), 30, fill=CARD)
        d.ellipse((75, y + 55, 155, y + 135), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 65), n, font=f(52), fill=NAVY)
        d.text((190, y + 30), a, font=f(46), fill=WHITE)
        d.text((190, y + 105), b, font=f(34), fill=MUTED)
        y += 215
    return img, d


def slide_ready():
    img, d = canvas()
    d.text((100, 190), "Kumpleto na ang setup", font=f(60), fill=MUTED)
    d.text((100, 270), "Handa ka na", font=f(130), fill=YELLOW)
    wrap_draw(d, "Node.js, n8n, Ollama + model, at ang local na account mo", 100, 440, 48, WHITE, 1100, 0.2)
    d.rounded_rectangle((100, 620, 1100, 770), 36, fill=CARD, outline=YELLOW, width=4)
    d.text((140, 642), "Susunod: gumawa ng AI agent", font=f(46), fill=WHITE)
    d.text((140, 710), "n8n AI Agent Tutorial (Tagalog)", font=f(34), fill=MUTED)
    return img, d  # right half and bottom stay clear for the end-screen element


def slide_agent_vs():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Chatbot, Workflow o AI Agent?", font=f(76), fill=WHITE)
    cols = [("CHATBOT", "Sumasagot lang", "Walang tools", False), ("WORKFLOW", "Sumusunod sa fixed na hakbang", "Ikaw ang nagdidisenyo ng bawat step", False),
            ("AI AGENT", "Siya ang nagpapasya kung anong tool ang gagamitin", "Calculator, Wikipedia, at iba pa", True)]
    for i, (a, b, c, hot) in enumerate(cols):
        x = 40 + i * 500
        d.rounded_rectangle((x, 260, x + 470, 700), 36, fill=CARD, outline=YELLOW if hot else None, width=6)
        d.text((x + 36, 290), a, font=f(46), fill=YELLOW if hot else MUTED)
        wrap_draw(d, b, x + 36, 380, 38, WHITE, 400, 0.2)
        wrap_draw(d, c, x + 36, 560, 30, GREEN if hot else MUTED, 400, 0.2)
    return img, d


def slide_needs():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang kailangan mo (libre lahat)", font=f(72), fill=WHITE)
    rows = [("1", "n8n  (version 2.47.5 ang gamit ko)", "npm install n8n", "npx n8n start"), ("2", "Ollama + local na AI model", "ollama pull llama3.2:3b", ""),
            ("3", "Walang API key. Walang bayad.", "", "")]
    y = 215
    for n, a, c1, c2 in rows:
        d.rounded_rectangle((40, y, 1520, y + 175), 30, fill=CARD)
        d.ellipse((75, y + 48, 155, y + 128), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 58), n, font=f(52), fill=NAVY)
        d.text((190, y + 20), a, font=f(44), fill=WHITE)
        if c1:
            d.rounded_rectangle((190, y + 92, 190 + (700 if c2 else 760), y + 152), 14, fill="#0A1636")
            d.text((210, y + 103), c1, font=fm(32), fill=GREEN)
        if c2:
            d.rounded_rectangle((920, y + 92, 1470, y + 152), 14, fill="#0A1636")
            d.text((940, y + 103), c2, font=fm(32), fill=GREEN)
        y += 195
    d.text((40, 790), "Parte A: model at unang reply   |   B: tools   |   C: memory", font=f(34), fill=YELLOW)
    return img, d


def slide_system():
    img, d = frame_base("SYSTEM MESSAGE")
    d.text((40, 110), "Ang system message (kopyahin ito)", font=f(66), fill=WHITE)
    d.rounded_rectangle((40, 220, 1520, 780), 30, fill="#0A1636", outline="#3B4F8A", width=3)
    wrap_draw(d, SYSTEM_MESSAGE, 70, 250, 33, "#D7E2FF", 1420, 0.25, mono=True)
    d.text((40, 800), "Nasa description din ang buong text.", font=f(34), fill=MUTED)
    return img, d


def slide_results():
    img, d = frame_base("BUOD NG TEST")
    d.text((40, 110), "Mga totoong resulta", font=f(72), fill=WHITE)
    rows = [("Walang malinaw na instruction", "2414.72", "MALI", False), ("Malinaw na system message", "2250.08", "TAMA", True),
            ("Walang memory: Ano ang pangalan ko?", "Reviewer Buddy", "MALI", False), ("May Simple Memory", "Ana", "TAMA", True)]
    y = 230
    for a, b, c, ok in rows:
        d.rounded_rectangle((40, y, 1520, y + 120), 26, fill=CARD)
        d.text((70, y + 34), a, font=f(38), fill=WHITE)
        d.text((830, y + 30), b, font=f(44), fill=YELLOW)
        d.rounded_rectangle((1280, y + 24, 1480, y + 96), 36, fill=GREEN if ok else RED)
        d.text((1380 - d.textlength(c, font=f(38)) / 2, y + 35), c, font=f(38), fill=NAVY)
        y += 140
    wrap_draw(d, "Maliit na model (llama3.2:3b): minsan nalilito. Mas malaking model, mas maaasahan.", 40, 815, 34, MUTED, 1480, 0.2)
    return img, d


def slide_next():
    img, d = canvas()
    d.text((100, 200), "Susunod", font=f(60), fill=MUTED)
    d.text((100, 280), "Part 2", font=f(140), fill=YELLOW)
    wrap_draw(d, "I-connect ang agent sa Telegram: gumawa ng sarili mong AI bot", 100, 450, 54, WHITE, 1000, 0.2)
    d.rounded_rectangle((100, 640, 1100, 790), 36, fill=CARD, outline=YELLOW, width=4)
    d.text((140, 662), "Workflow file at system message", font=f(44), fill=WHITE)
    d.text((140, 725), "Nasa description", font=f(36), fill=MUTED)
    return img, d  # right half and bottom stay clear for the end-screen element


def slide_p2_needs():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang kailangan mo (libre lahat)", font=f(72), fill=WHITE)
    rows = [("1", "Ang workflow mula sa Part 1", "Reviewer Buddy: AI Agent, Ollama, Calculator, Wikipedia, memory"), ("2", "n8n at Ollama na tumatakbo", "http://localhost:5678  at  http://127.0.0.1:11434"),
            ("3", "Chrome at Python (para sa maliit na web server)", "Walang Telegram, walang bagong account")]
    y = 230
    for n, a, c in rows:
        d.rounded_rectangle((40, y, 1520, y + 150), 30, fill=CARD)
        d.ellipse((75, y + 35, 155, y + 115), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 45), n, font=f(52), fill=NAVY)
        d.text((190, y + 20), a, font=f(42), fill=WHITE)
        d.text((190, y + 88), c, font=f(32), fill=MUTED)
        y += 168
    d.text((40, 750), "Parte A: Hosted Chat   |   B: Embedded Chat sa sarili mong page", font=f(34), fill=YELLOW)
    return img, d


def slide_chat_options():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Dalawang paraan ng chat sa n8n", font=f(72), fill=WHITE)
    cols = [("HOSTED CHAT", "May chat page na galing mismo sa n8n", "Walang code. Pinakamadali.", "Parte A", False),
            ("EMBEDDED CHAT", "Ikaw ang gagawa ng page, at ilalagay ang chat widget", "Sarili mong itsura at kulay.", "Parte B", True)]
    for i, (a, b, c, p, hot) in enumerate(cols):
        x = 40 + i * 750
        d.rounded_rectangle((x, 260, x + 720, 700), 36, fill=CARD, outline=YELLOW if hot else None, width=6)
        d.text((x + 40, 290), a, font=f(52), fill=YELLOW if hot else WHITE)
        wrap_draw(d, b, x + 40, 400, 40, WHITE, 640, 0.2)
        wrap_draw(d, c, x + 40, 560, 34, GREEN, 640, 0.2)
        d.rounded_rectangle((x + 40, 630, x + 220, 680), 25, fill=YELLOW)
        d.text((x + 130 - d.textlength(p, font=f(30)) / 2, 637), p, font=f(30), fill=NAVY)
    return img, d


def slide_embed_code():
    img, d = frame_base("PHASE B")
    d.text((40, 110), "Ang buong code ng page (ang bahagi ng chat)", font=f(60), fill=WHITE)
    d.rounded_rectangle((40, 210, 1520, 755), 30, fill="#0A1636", outline="#3B4F8A", width=3)
    lines = [("#7B8DB5", "<!-- sa <head>: stylesheet, naka-pin ang version -->"),
             ("#CBD5E1", "<link href=\".../npm/@n8n/chat@1.46.4/dist/style.css\" rel=\"stylesheet\">"),
             ("#7B8DB5", ""),
             ("#7B8DB5", "<!-- bago mag-</body> -->"),
             ("#CBD5E1", "<script type=\"module\">"),
             ("#CBD5E1", "  import { createChat } from '.../@n8n/chat@1.46.4/dist/chat.bundle.es.js';"),
             ("#CBD5E1", "  createChat({"),
             (YELLOW, "    webhookUrl: 'http://localhost:5678/webhook/<id>/chat',"),
             (GREEN, "    mode: 'window',"),
             ("#CBD5E1", "    initialMessages: ['Kumusta! Ako si Reviewer Buddy.'],"),
             ("#CBD5E1", "  });"),
             ("#CBD5E1", "</script>")]
    y = 228
    for col, t in lines:
        d.text((70, y), t, font=fm(27), fill=col)
        y += 42
    d.text((40, 772), "Ang buong HTML file ay nasa GitHub (link sa description).", font=f(34), fill=MUTED)
    return img, d


def slide_p2_rules():
    img, d = frame_base("BAGO MO I-SHARE")
    d.text((40, 110), "3 paalala bago mo i-share", font=f(76), fill=WHITE)
    rows = [("1", "I-publish muna ang workflow", "Hindi gagana ang chat link kapag hindi pa Published."),
            ("2", "Localhost ang link: sa computer mo lang", "Hindi ito bubukas sa ibang computer o phone."),
            ("3", "Authentication: None = bukas sa sinumang may link", "Gumamit ng Authentication bago mag-share. Computer mo ang gagamit ng lakas.")]
    y = 250
    for n, a, b in rows:
        d.rounded_rectangle((40, y, 1520, y + 190), 30, fill=CARD)
        d.ellipse((75, y + 55, 155, y + 135), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 65), n, font=f(52), fill=NAVY)
        d.text((190, y + 30), a, font=f(44), fill=WHITE)
        d.text((190, y + 105), b, font=f(32), fill=MUTED)
        y += 215
    return img, d


def slide_p2_results():
    img, d = frame_base("BUOD NG TEST")
    d.text((40, 110), "Mga totoong resulta", font=f(72), fill=WHITE)
    rows = [("Hosted Chat (galing sa n8n)", "2250.08", "TAMA", True), ("Embedded widget sa sarili kong page", "2250.08", "TAMA", True),
            ("Unang bersyon ng page ko", "sira ang layout", "MALI", False), ("Pagkatapos ayusin ang CSS", "buo ang chat", "TAMA", True)]
    y = 230
    for a, b, c, ok in rows:
        d.rounded_rectangle((40, y, 1520, y + 120), 26, fill=CARD)
        d.text((70, y + 34), a, font=f(38), fill=WHITE)
        d.text((830, y + 30), b, font=f(44), fill=YELLOW)
        d.rounded_rectangle((1280, y + 24, 1480, y + 96), 36, fill=GREEN if ok else RED)
        d.text((1380 - d.textlength(c, font=f(38)) / 2, y + 35), c, font=f(38), fill=NAVY)
        y += 140
    wrap_draw(d, "Nasa computer ko ang lahat: n8n, Ollama at ang model. Mga 20 segundo ang sagot.", 40, 788, 34, MUTED, 1480, 0.2)
    return img, d


def slide_p2_next():
    img, d = canvas()
    d.text((100, 200), "Susunod", font=f(60), fill=MUTED)
    d.text((100, 280), "Part 3", font=f(140), fill=YELLOW)
    wrap_draw(d, "I-save sa Excel ang mga tanong at sagot: sarili mong study tracker", 100, 450, 54, WHITE, 1000, 0.2)
    d.rounded_rectangle((100, 640, 1100, 790), 36, fill=CARD, outline=YELLOW, width=4)
    d.text((140, 662), "Workflow file at chat page", font=f(44), fill=WHITE)
    d.text((140, 725), "Nasa description", font=f(36), fill=MUTED)
    return img, d  # right half and bottom stay clear for the end-screen element


def slide_p3_needs():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang kailangan mo (libre lahat)", font=f(72), fill=WHITE)
    rows = [("1", "Ang workflow mula sa Part 1", "Reviewer Buddy, na may Ollama, Calculator, Wikipedia at memory"), ("2", "n8n at Ollama na tumatakbo", "http://localhost:5678  at  http://127.0.0.1:11434"),
            ("3", "Excel (o kahit anong spreadsheet)", "Bubuksan nito ang CSV file. Walang Google account.")]
    y = 230
    for n, a, c in rows:
        d.rounded_rectangle((40, y, 1520, y + 150), 30, fill=CARD)
        d.ellipse((75, y + 35, 155, y + 115), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 45), n, font=f(52), fill=NAVY)
        d.text((190, y + 20), a, font=f(42), fill=WHITE)
        d.text((190, y + 88), c, font=f(32), fill=MUTED)
        y += 168
    d.text((40, 750), "CSV: madaling dagdagan ng bagong linya.   XLSX: hindi.", font=f(34), fill=YELLOW)
    return img, d


def slide_p3_plan():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang plano: 4 na node pagkatapos ng AI Agent", font=f(64), fill=WHITE)
    boxes = [("AI Agent", "sumasagot", False), ("Edit Fields", "bumubuo ng 1 linya", True), ("Convert to File", "text file", True), ("Write File to Disk", "nagdadagdag (Append)", True), ("Edit Fields", "sagot para sa chat", True)]
    x = 40
    for i, (a, b, new) in enumerate(boxes):
        d.rounded_rectangle((x, 290, x + 270, 520), 28, fill=CARD, outline=YELLOW if new else None, width=5)
        wrap_draw(d, a, x + 18, 320, 34, YELLOW if new else WHITE, 240, 0.15)
        wrap_draw(d, b, x + 18, 430, 28, MUTED, 240, 0.15)
        if i < len(boxes) - 1:
            d.polygon([(x + 280, 395), (x + 308, 380), (x + 308, 410)], fill=YELLOW)
        x += 310
    d.text((40, 600), "Dilaw = mga bagong node.   Ang file: study-log.csv", font=f(36), fill=MUTED)
    return img, d


def slide_p3_folder():
    img, d = frame_base("AYOS")
    d.text((40, 110), "Isang folder lang ang pinapayagan", font=f(72), fill=WHITE)
    d.rounded_rectangle((40, 230, 1520, 410), 30, fill=CARD)
    d.text((70, 250), "Default", font=f(40), fill=YELLOW)
    d.text((70, 315), "~/.n8n-files   (nasa user folder mo)", font=fm(36), fill=GREEN)
    d.rounded_rectangle((40, 440, 1520, 700), 30, fill=CARD, outline=YELLOW, width=4)
    d.text((70, 460), "Pwede mong palitan (sa akin)", font=f(40), fill=YELLOW)
    d.text((70, 525), "N8N_RESTRICT_FILE_ACCESS_TO=<folder mo>", font=fm(34), fill=GREEN)
    d.text((70, 595), "Pagkatapos: i-restart ang n8n", font=f(36), fill=WHITE)
    d.text((70, 645), "study-log.csv:  date,question,answer   (header, 1 linya)", font=fm(30), fill=MUTED)
    return img, d


def slide_p3_rules():
    img, d = frame_base("BAGO MO GAMITIN")
    d.text((40, 110), "3 paalala", font=f(76), fill=WHITE)
    rows = [("1", "I-check ang mga sagot ng AI", "Mali ang 15% ng 3200: 2720 ang sagot, 480 ang tama."),
            ("2", "Isang folder lang ang masusulatan ng n8n", "Ang mga ibang path ay: Access to the file is not allowed."),
            ("3", "CSV para madagdagan, XLSX para sa ganda", "Buksan ang CSV sa Excel, at i-save bilang XLSX kung kailangan.")]
    y = 250
    for n, a, b in rows:
        d.rounded_rectangle((40, y, 1520, y + 190), 30, fill=CARD)
        d.ellipse((75, y + 55, 155, y + 135), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + 65), n, font=f(52), fill=NAVY)
        d.text((190, y + 30), a, font=f(44), fill=WHITE)
        d.text((190, y + 105), b, font=f(32), fill=MUTED)
        y += 215
    return img, d


def slide_p3_results():
    img, d = frame_base("BUOD NG TEST")
    d.text((40, 110), "Mga totoong problema at ayos", font=f(72), fill=WHITE)
    rows = [("Path sa labas ng pinapayagang folder", "Access not allowed", "MALI", False), ("Expression na tinype lang", "literal na text", "MALI", False),
            ("Default na timezone", "Nov 12, 18:07", "MALI", False), ("Convert to CSV + Append", "magkadikit na linya", "MALI", False),
            ("Lahat ng ayos, buksan sa Excel", "header + 2 row", "TAMA", True)]
    y = 230
    for a, b, c, ok in rows:
        d.rounded_rectangle((40, y, 1520, y + 105), 26, fill=CARD)
        d.text((70, y + 28), a, font=f(36), fill=WHITE)
        d.text((830, y + 26), b, font=f(40), fill=YELLOW)
        d.rounded_rectangle((1280, y + 18, 1480, y + 86), 34, fill=GREEN if ok else RED)
        d.text((1380 - d.textlength(c, font=f(36)) / 2, y + 28), c, font=f(36), fill=NAVY)
        y += 120
    return img, d


def slide_p3_next():
    img, d = canvas()
    d.text((100, 200), "Kumpleto na ang serye", font=f(60), fill=MUTED)
    d.text((100, 280), "Playlist", font=f(140), fill=YELLOW)
    wrap_draw(d, "0 Setup   1 AI agent   2 Chatbot sa web page   3 Study tracker sa Excel", 100, 450, 48, WHITE, 1000, 0.2)
    d.rounded_rectangle((100, 640, 1100, 790), 36, fill=CARD, outline=YELLOW, width=4)
    d.text((140, 662), "Workflow file at chat page", font=f(44), fill=WHITE)
    d.text((140, 725), "Nasa description", font=f(36), fill=MUTED)
    return img, d  # right half and bottom stay clear for the end-screen element


def _p4_cards(d, rows, y0, step, h, size_a=42, size_c=32):
    y = y0
    for n, a, c in rows:
        d.rounded_rectangle((40, y, 1520, y + h), 30, fill=CARD)
        d.ellipse((75, y + (h - 80) // 2, 155, y + (h - 80) // 2 + 80), fill=YELLOW)
        d.text((115 - d.textlength(n, font=f(52)) / 2, y + (h - 80) // 2 + 10), n, font=f(52), fill=NAVY)
        d.text((190, y + 20), a, font=f(size_a), fill=WHITE)
        d.text((190, y + 20 + size_a + 26), c, font=f(size_c), fill=MUTED)
        y += step


def slide_p4_idea():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Webhook at API: ano ang pagkakaiba?", font=f(68), fill=WHITE)
    d.rounded_rectangle((40, 250, 740, 700), 30, fill=CARD, outline=YELLOW, width=5)
    d.text((70, 275), "Webhook", font=f(60), fill=YELLOW)
    wrap_draw(d, "Isang address na naghihintay ng tawag. Kapag may tumawag, tatakbo ang workflow mo.", 70, 370, 36, WHITE, 640, 0.2)
    d.text((70, 610), "Parang doorbell", font=f(40), fill=MUTED)
    d.rounded_rectangle((780, 250, 1520, 700), 30, fill=CARD)
    d.text((810, 275), "API", font=f(60), fill=YELLOW)
    wrap_draw(d, "Bintana ng ibang serbisyo. Ikaw ang tatawag, at sasagot sila ng data.", 810, 370, 36, WHITE, 680, 0.2)
    d.text((810, 610), "Open-Meteo: libre, walang key", font=f(40), fill=MUTED)
    return img, d


def slide_p4_needs():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang kailangan mo (libre lahat)", font=f(72), fill=WHITE)
    _p4_cards(d, [("1", "n8n at Ollama na tumatakbo", "Galing sa Part 1: http://localhost:5678 at http://127.0.0.1:11434"),
                  ("2", "PowerShell sa Windows 11", "May kasamang curl.exe. Hindi kailangang mag-install ng iba."),
                  ("3", "Open-Meteo (weather API)", "Libre. Walang account, walang API key.")], 230, 168, 150)
    d.text((40, 750), "Ang workflow file: weather-webhook.json (nasa description)", font=f(34), fill=YELLOW)
    return img, d


def slide_p4_plan():
    img, d = frame_base("SETUP")
    d.text((40, 110), "Ang plano: 5 na hakbang", font=f(68), fill=WHITE)
    boxes = [("Webhook", "tumatanggap ng city"), ("Find city", "HTTP Request: hanapin ang lungsod"), ("Get weather", "HTTP Request: temp at humidity"), ("Advice", "AI (Ollama): isang payo"), ("Reply", "Respond to Webhook")]
    x = 40
    for i, (a, b) in enumerate(boxes):
        d.rounded_rectangle((x, 290, x + 270, 520), 28, fill=CARD, outline=YELLOW, width=5)
        wrap_draw(d, a, x + 18, 320, 36, YELLOW, 240, 0.15)
        wrap_draw(d, b, x + 18, 400, 28, MUTED, 240, 0.15)
        if i < len(boxes) - 1:
            d.polygon([(x + 280, 395), (x + 308, 380), (x + 308, 410)], fill=YELLOW)
        x += 310
    d.text((40, 590), "May isa pang daan: kapag walang nahanap na lungsod, 404 ang isasagot.", font=f(36), fill=MUTED)
    return img, d


def slide_p4_rules():
    img, d = frame_base("BAGO MO GAMITIN")
    d.text((40, 110), "3 paalala", font=f(76), fill=WHITE)
    _p4_cards(d, [("1", "Test URL: isang tawag. Production URL: kailangan ng Publish", "Execute workflow ulit para sa bawat test. I-Publish bago tumawag sa production."),
                  ("2", "Pwedeng mabagal ang API", "Retry On Fail (3 tries) at isang daan para sa maling lungsod."),
                  ("3", "Ibigay sa AI ang totoong numero", "Pero i-check ang payo: nag-imbento ito ng ulan na wala sa datos.")], 235, 190, 165, size_a=40)
    return img, d


def slide_p4_results():
    img, d = frame_base("BUOD NG TEST")
    d.text((40, 110), "Mga totoong problema at ayos", font=f(72), fill=WHITE)
    rows = [("Listen sa mismong Webhook node", "walang laman na sagot", "MALI", False), ("Test URL, pangalawang tawag", "404 not registered", "MALI", False),
            ("Geocoding API", "timeout, 21.7 s", "MALI", False), ("Production URL bago mag-Publish", "404", "MALI", False),
            ("JSON sa PowerShell", "422 parse error", "MALI", False), ("Lahat ng ayos: Manila", "28.1 C, 68%", "TAMA", True)]
    y = 205
    for a, b, c, ok in rows:
        d.rounded_rectangle((40, y, 1520, y + 88), 24, fill=CARD)
        d.text((70, y + 22), a, font=f(36), fill=WHITE)
        d.text((830, y + 20), b, font=f(40), fill=YELLOW)
        d.rounded_rectangle((1280, y + 12, 1480, y + 76), 32, fill=GREEN if ok else RED)
        d.text((1380 - d.textlength(c, font=f(36)) / 2, y + 22), c, font=f(36), fill=NAVY)
        y += 100
    return img, d


def slide_p4_next():
    img, d = canvas()
    d.text((100, 200), "Hindi pa tapos ang serye", font=f(60), fill=MUTED)
    d.text((100, 280), "Part 5", font=f(140), fill=YELLOW)
    wrap_draw(d, "Error handling: ayusin nang tama kapag pumalya ang workflow", 100, 450, 48, WHITE, 1000, 0.2)
    d.rounded_rectangle((100, 640, 1100, 790), 36, fill=CARD, outline=YELLOW, width=4)
    d.text((140, 662), "Workflow file: weather-webhook.json", font=f(44), fill=WHITE)
    d.text((140, 725), "Nasa description", font=f(36), fill=MUTED)
    return img, d  # right half and bottom stay clear for the end-screen element


SLIDES = {"p4_idea": slide_p4_idea, "p4_needs": slide_p4_needs, "p4_plan": slide_p4_plan, "p4_rules": slide_p4_rules, "p4_results": slide_p4_results, "p4_next": slide_p4_next, "p3_needs": slide_p3_needs, "p3_plan": slide_p3_plan, "p3_folder": slide_p3_folder, "p3_rules": slide_p3_rules, "p3_results": slide_p3_results, "p3_next": slide_p3_next, "p2_needs": slide_p2_needs, "chat_options": slide_chat_options, "embed_code": slide_embed_code, "p2_rules": slide_p2_rules, "p2_results": slide_p2_results, "p2_next": slide_p2_next, "hook_checks": slide_hook_checks, "requirements": slide_requirements, "account_tips": slide_account_tips, "ready": slide_ready, "agent_vs": slide_agent_vs, "needs": slide_needs, "system_message": slide_system, "results": slide_results, "next": slide_next}


def frame_slide(sc, sub=""):
    img, d = SLIDES[sc["slide"]]()
    if sc["slide"] not in ("next", "ready", "p2_next", "p3_next", "p4_next"):
        subtitle(d, sub)
    return img


def frame_pause(sc, sub="", count=None, reveal=False):
    img, d = frame_base("PAUSE AND TRY")
    d.text((40, 120), "Pause and try!", font=f(86), fill=YELLOW)
    yy = wrap_draw(d, sc["pause_q"], 40, 250, 56, WHITE, 1450, 0.2)
    if reveal:
        for i, a in enumerate(sc["pause_a"]):
            d.rounded_rectangle((40, yy + 40 + i * 110, 1500, yy + 130 + i * 110), 26, fill=GREEN)
            d.text((70, yy + 58 + i * 110), a, font=fm(42), fill=NAVY)
    elif count is not None:
        cx, cy, r = 800, 600, 170
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=CARD, outline=YELLOW, width=12)
        d.text((cx - d.textlength(str(count), font=f(230)) / 2, cy - 150), str(count), font=f(230), fill=WHITE)
    subtitle(d, sub)
    return img


def frame_comment(sc, sub=""):
    img, d = frame_base("COMMENT")
    d.rounded_rectangle((40, 200, 1500, 700), 40, fill=CARD, outline=YELLOW, width=6)
    wrap_draw(d, sc["comment_q"], 90, 260, 70, WHITE, 1360, 0.2)
    d.text((90, 560), sc["comment_sub"], font=f(60), fill=YELLOW)
    subtitle(d, sub)
    return img


def sentences(text):
    parts = [s.strip().replace("․", ".") for s in re.findall(r"[^.?!]+[.?!]+|[^.?!]+$", re.sub(r"(?<=\d)\.(?=\d)", "․", text)) if s.strip()]
    return parts or [text]


# ---------------------------------------------------------------- assemble
def build():
    tmp = Path(tempfile.mkdtemp())
    segs, clips, ticks, chimes, chapters, cues = [], [], [], [], [], []
    t = 0.0
    for idx, sc in enumerate(SCENES):
        wav = tts(sc["say"])
        vlen = wav_len(wav)
        delay, tail = 0.35, 0.5
        clips.append((t + delay, wav))
        if sc.get("chapter"):
            chapters.append((sc["chapter"], t))
        sents = sentences(sc["say"])
        total_chars = sum(len(s) for s in sents)
        # frame per sentence so the subtitle bar follows the voice
        cur = t
        for k, s in enumerate(sents):
            d_s = vlen * len(s) / total_chars
            lead = delay if k == 0 else 0
            end = tail if k == len(sents) - 1 else 0
            dur = d_s + lead + end
            kind = sc["kind"]
            if kind == "shot":
                img = frame_shot(sc, s)
            elif kind == "zoom":
                img = frame_zoom(sc, s)
            elif kind == "terminal":
                img = frame_terminal(sc, s)
            elif kind == "slide":
                img = frame_slide(sc, s)
            elif kind == "pause":
                img = frame_pause(sc, s)
            else:
                img = frame_comment(sc, s)
            segs.append((img, dur))
            cues.append((cur + (delay if k == 0 else 0), cur + dur - end, s))
            cur += dur
        t = cur
        if sc["kind"] == "pause":
            for n in range(sc["seconds"], 0, -1):
                segs.append((frame_pause(sc, "", count=n), 1.0))
                ticks.append(t)
                t += 1.0
            chimes.append(t)
            segs.append((frame_pause(sc, "", reveal=True), 4.0))
            t += 4.0
        if sc["kind"] == "comment":
            segs.append((frame_comment(sc, ""), float(sc["seconds"])))
            t += sc["seconds"]
    total = t
    lines = []
    for i, (img, dur) in enumerate(segs):
        p = tmp / f"f{i:04d}.png"
        img.save(p)
        lines += [f"file '{p.as_posix()}'", f"duration {dur:.4f}"]
    lines.append(f"file '{(tmp / f'f{len(segs) - 1:04d}.png').as_posix()}'")
    (tmp / "list.txt").write_text("\n".join(lines))
    audio = tmp / "mix.wav"
    ml.mix_audio(clips, total, ticks, chimes, audio)
    raw = tmp / "raw.mp4"
    subprocess.run([FF, "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(audio), "-c:a", "aac", "-b:a", "192k",
                    "-vf", f"fps={FPS},format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-movflags", "+faststart", "-t", f"{total:.3f}", str(raw)],
                   check=True, stderr=subprocess.DEVNULL)
    final_tmp = tmp / "final.mp4"
    subprocess.run([sys.executable, str(PRESENTER), str(raw), str(final_tmp)], check=True)
    chk = subprocess.run([FF, "-v", "error", "-i", str(final_tmp), "-f", "null", "-"], capture_output=True, text=True)
    if chk.returncode or chk.stderr.strip():
        sys.exit("decode check failed: " + chk.stderr[:300])
    (ROOT / "videos").mkdir(exist_ok=True)
    out = ROOT / "videos" / f"{NAME}.mp4"
    shutil.move(str(final_tmp), str(out))

    def stamp(x):
        return f"{int(x // 60)}:{int(x % 60):02d}"

    (ROOT / "chapters").mkdir(exist_ok=True)
    (ROOT / "chapters" / f"{NAME}.txt").write_text("\n".join(f"{stamp(s)} {n}" for n, s in chapters) + "\n", encoding="utf-8")

    def ts(x):
        ms_ = int(round(x * 1000))
        return "%02d:%02d:%02d,%03d" % (ms_ // 3600000, ms_ // 60000 % 60, ms_ // 1000 % 60, ms_ % 1000)

    (ROOT / "captions").mkdir(exist_ok=True)
    with open(ROOT / "captions" / f"{NAME}.srt", "w", encoding="utf-8") as fh:
        for k, (a, b, s) in enumerate(cues, 1):
            fh.write(f"{k}\n{ts(a)} --> {ts(b)}\n{s}\n\n")
    print(out, f"{total:.0f}s", stamp(total))
    print((ROOT / "chapters" / f"{NAME}.txt").read_text())


if __name__ == "__main__":
    if "--frames" in sys.argv:
        out_path = sys.argv[sys.argv.index("--frames") + 1]
        pick = [i for i in [0, 2, 3, 7, 8, 12, 17, 19, 20, 22, 25, 26, 27, 28, 30] if i < len(SCENES)] if not os.environ.get('SCENES') else list(range(len(SCENES)))
        ims = []
        for i in pick:
            sc = SCENES[i]
            sub = sentences(sc["say"])[0]
            k = sc["kind"]
            ims.append(frame_shot(sc, sub) if k == "shot" else frame_zoom(sc, sub) if k == "zoom" else frame_terminal(sc, sub) if k == "terminal" else frame_slide(sc, sub) if k == "slide"
                       else frame_pause(sc, sub, reveal=True) if k == "pause" else frame_comment(sc, sub))
        cols, tw, th = 4, 480, 270
        rows = (len(ims) + cols - 1) // cols
        sheet = Image.new("RGB", (tw * cols, th * rows))
        for k, im in enumerate(ims):
            sheet.paste(im.resize((tw, th)), ((k % cols) * tw, (k // cols) * th))
        sheet.save(out_path)
    else:
        build()
