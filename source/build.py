"""Render a Git + GitHub tutorial (1920x1080) from CONTENT.STEPS.
Piper voice, lo-fi bed, real git output, word-by-word highlighted captions (key terms in yellow),
and the Sir Yuls cartoon presenter (lower right, lip-synced to the narration only).

usage: CONTENT=content_p2 OUTNAME=part2-... python build.py
Layout rule: nothing important below y 760 right of x 1500 (presenter sits at x 1570, y 766, 300 px).
"""
import importlib, os, re, subprocess, sys, wave
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

sys.path.insert(0, "D:/MIT/ict-proficiency-reels/tools")
import voice, study_music

content = importlib.import_module(os.environ.get("CONTENT", "content"))
OUTNAME = os.environ.get("OUTNAME", "00-overview-git-and-github-for-beginners")
PRESENTER = "D:/MIT/series-tools/efcore/presenter.py"

HERE = Path(__file__).parent          # source/
ROOT = HERE.parent
(ROOT / "videos").mkdir(exist_ok=True); (ROOT / "chapters").mkdir(exist_ok=True)
TMP = HERE / f"_tmp_{OUTNAME}"; TMP.mkdir(exist_ok=True)
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 1920, 1080
NAVY, YELLOW, WHITE, GREEN, CARD, TERM = "#0B1F4B", "#FFD21F", "#FFFFFF", "#7EE787", "#16306B", "#07122E"
GREY, DIM, CAPBG = "#B8C4E0", "#8CA0C8", "#050D24"
SCALE, PAD = 1.25, 0.4
CAP_L, CAP_R, CAP_B = 60, 1500, 1044
RIGHT = 1500   # right edge for cards below y 700

KEY = set("""git github commit commits push pull clone branch branches main origin merge remote repository repositories staging fetch stash switch add init
status log conflict conflicts readme gitignore ignore env token tokens password passwords secret secrets key keys never always rejected unrelated histories
cached rm rebase stash vs code terminal pull request requests reviewed review four three two one dash""".split())


def f(s, mono=False): return ImageFont.truetype("C:/Windows/Fonts/%s.ttf" % ("consola" if mono else "arialbd"), s)


def wrap(d, text, fn, mw):
    L, c = [], ""
    for w in text.split():
        t = f"{c} {w}".strip()
        if d.textlength(t, font=fn) <= mw: c = t
        else: L.append(c); c = w
    return L + [c]


_MEAS = ImageDraw.Draw(Image.new("RGB", (10, 10)))
CF = f(31)
CAP_LH = 42


def cap_layout(say):
    """Return (lines as lists of word indexes, box top)."""
    words = say.split(); lines, cur, curw = [], [], ""
    for i, w in enumerate(words):
        t = f"{curw} {w}".strip()
        if _MEAS.textlength(t, font=CF) <= (CAP_R - CAP_L) - 70 or not cur: cur.append(i); curw = t
        else: lines.append(cur); cur = [i]; curw = w
    lines.append(cur)
    lines = lines[:5]
    return lines, CAP_B - (len(lines) * CAP_LH + 34)


def word_times(say, dur):
    words = say.split(); wt = []
    for w in words:
        base = len(re.sub(r"\W", "", w)) + 2
        if w.endswith((".", "?", "!", ":")): base += 6
        elif w.endswith((",", ";")): base += 3
        wt.append(base)
    tot = sum(wt); t = 0.0; starts = []
    for x in wt: starts.append(t); t += dur * x / tot
    return starts


def draw_caption(img, say, cur):
    d = ImageDraw.Draw(img); words = say.split(); lines, top = cap_layout(say)
    d.rounded_rectangle((CAP_L, top, CAP_R, CAP_B), 26, fill=CAPBG)
    cx = (CAP_L + CAP_R) / 2; y = top + 17; sp = _MEAS.textlength(" ", font=CF)
    for ln in lines:
        total = sum(_MEAS.textlength(words[i], font=CF) for i in ln) + sp * (len(ln) - 1)
        x = cx - total / 2
        for i in ln:
            w = words[i]; ww = _MEAS.textlength(w, font=CF); key = re.sub(r"\W", "", w).lower() in KEY
            if i == cur:
                d.rounded_rectangle((x - 8, y - 3, x + ww + 8, y + CAP_LH - 8), 12, fill=YELLOW); col = NAVY
            elif i < cur: col = YELLOW if key else WHITE
            else: col = YELLOW if key else DIM
            d.text((x, y), w, font=CF, fill=col); x += ww + sp
        y += CAP_LH


def base(step, idx, total):
    img = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 10), fill=CARD); d.rectangle((0, 0, int(W * (idx + 1) / total), 10), fill=YELLOW)
    if step["kind"] not in ("title", "end"):
        tag = step["section"].upper(); tf = f(26); tw = d.textlength(tag, font=tf) + 44
        d.rounded_rectangle((80, 36, 80 + tw, 84), 24, fill=YELLOW); d.text((102, 44), tag, font=tf, fill=NAVY)
        d.text((80, 100), step["head"], font=f(58), fill=WHITE)
    return img, d


def r_title(step, idx, total):
    img, d = base(step, idx, total)
    d.text((W / 2, 300), "Git & GitHub", font=ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", 170), fill=YELLOW, anchor="mm")
    d.text((W / 2, 490), "Set up a repository and collaborate with a team", font=f(56), fill=WHITE, anchor="mm")
    for i, t in enumerate(["git init", "git push", "pull request"]):
        x = W / 2 + (i - 1) * 420; d.rounded_rectangle((x - 190, 600, x + 190, 680), 36, fill=CARD)
        d.text((x, 640), t, font=f(40, True), fill=GREEN, anchor="mm")
    return img


def r_end(step, idx, total):
    img, d = base(step, idx, total)
    d.text((W / 2, 330), step.get("title", "Thanks for watching"), font=f(100), fill=YELLOW, anchor="mm")
    d.text((W / 2, 490), step.get("sub", "Practice: make a repo, push it, open a pull request"), font=f(52), fill=WHITE, anchor="mm")
    d.text((W / 2, 580), "Synthetic voice and cartoon presenter. Names in commands are examples.", font=f(32), fill=GREY, anchor="mm")
    return img


def r_concept(step, idx, total):
    img, d = base(step, idx, total)
    items, hi = step["items"], step.get("hi", -1)
    y = 190; size = 46
    while size > 28 and max(_MEAS.textlength(t, font=f(size)) for t in items) > RIGHT - 250 - 40: size -= 2
    fn = f(size)
    for i, it in enumerate(items):
        on = (i == hi) or (hi == -1)
        d.rounded_rectangle((140, y, RIGHT, y + 88), 28, fill=CARD, outline=YELLOW if i == hi else None, width=5)
        if step["kind"] == "steps":
            d.ellipse((170, y + 16, 226, y + 72), fill=YELLOW if on else "#245099"); d.text((198, y + 44), str(i + 1), font=f(36), fill=NAVY, anchor="mm"); tx = 250
        else:
            d.ellipse((176, y + 32, 200, y + 56), fill=YELLOW if on else "#245099"); tx = 232
        d.text((tx, y + 44), it, font=fn, fill=WHITE if on else GREY, anchor="lm"); y += 100
    return img


def r_flow(step, idx, total):
    img, d = base(step, idx, total)
    boxes, labels, hi = step["boxes"], step["labels"], step["hi"]
    n = len(boxes); gap = 150 if n <= 4 else 80
    bw = (W - 200 - (n - 1) * gap) / n; y0, bh = 300, 190
    for i, b in enumerate(boxes):
        x = 100 + i * (bw + gap); on = i in hi
        d.rounded_rectangle((x, y0, x + bw, y0 + bh), 34, fill=YELLOW if on else CARD)
        fn = f(44 if n <= 4 else 36); ls = wrap(d, b, fn, bw - 30); ty = y0 + bh / 2 - len(ls) * 26
        for ln in ls:
            d.text((x + bw / 2, ty + 26), ln, font=fn, fill=NAVY if on else WHITE, anchor="mm"); ty += 52
        if i < n - 1:
            ax = x + bw + 12; ay = y0 + bh / 2
            d.line((ax, ay, ax + gap - 24, ay), fill=WHITE, width=8)
            d.polygon([(ax + gap - 24, ay - 18), (ax + gap - 24, ay + 18), (ax + gap - 2, ay)], fill=WHITE)
            if labels[i]: d.text((ax + (gap - 24) / 2, ay - 40), labels[i], font=f(34, True), fill=GREEN, anchor="mm")
    if step.get("ret"):
        t = step["ret"]; tw = d.textlength(t, font=f(40, True)) + 80
        d.rounded_rectangle((W / 2 - tw / 2, 580, W / 2 + tw / 2, 660), 40, fill="#05250F", outline=GREEN, width=4)
        d.text((W / 2, 620), "\u2190  " + t, font=f(40, True), fill=GREEN, anchor="mm")
    return img


def r_term(step, idx, total):
    img, d = base(step, idx, total)
    top, bot = 190, 740
    d.rounded_rectangle((100, top, W - 100, bot), 28, fill=TERM, outline=CARD, width=4)
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]): d.ellipse((130 + i * 40, top + 18, 152 + i * 40, top + 40), fill=c)
    d.text((W / 2, top + 30), "Terminal", font=f(26), fill=GREY, anchor="mm")
    lines = []
    for cmd, out in step["blocks"]:
        for c in cmd.split("\n"): lines.append(("cmd", c))
        for o in (out.split("\n") if out.strip() else []): lines.append(("out", o.replace("\t", "    ")))
    fn = f(31, True); lh = 40; lines = lines[-((bot - top - 80) // lh):]; y = top + 62
    for kind, t in lines:
        t = t[:100]
        if kind == "cmd": d.text((140, y), "$", font=fn, fill=YELLOW); d.text((175, y), t, font=fn, fill=WHITE)
        else:
            col = GREY
            if t.startswith(("<<<<<<<", ">>>>>>>", "=======")) or "CONFLICT" in t or t.startswith("error") or "rejected" in t: col = "#FF7B72"
            elif t.startswith(("*", "|")) or "Fast-forward" in t: col = GREEN
            d.text((140, y), t, font=fn, fill=col)
        y += lh
    return img


CROPS = {"repo.png": (0, 0, 1600, 600), "pulls.png": (0, 60, 1600, 640), "pr.png": (0, 60, 1450, 640)}


def r_shot(step, idx, total):
    img, d = base(step, idx, total)
    shot = Image.open(HERE / "shots" / step["img"]).convert("RGB")
    shot = shot.crop(CROPS.get(step["img"], (0, 0, shot.width, shot.height)))
    avail_h = 740 - 190; avail_w = W - 260
    sc = min(avail_w / shot.width, avail_h / shot.height)
    s2 = shot.resize((int(shot.width * sc), int(shot.height * sc)), Image.LANCZOS)
    x, y = (W - s2.width) // 2, 190 + (avail_h - s2.height) // 2
    d.rounded_rectangle((x - 10, y - 10, x + s2.width + 10, y + s2.height + 10), 14, fill=YELLOW)
    img.paste(s2, (x, y))
    if step.get("note"): d.text((CAP_R, 60), step["note"], font=f(26), fill=GREY, anchor="rm")
    return img


R = dict(title=r_title, end=r_end, concept=r_concept, steps=r_concept, flow=r_flow, term=r_term, shot=r_shot)

steps = content.STEPS
durs, segs = [], []
for n, st in enumerate(steps):
    mp4 = TMP / f"s{n:03d}.mp4"
    wav = voice.say(st["say"], scale=SCALE); adur = voice.wav_len(wav)
    base_img = R[st["kind"]](st, n, len(steps))
    starts = word_times(st["say"], adur); nw = len(starts)
    lines = []
    for k in range(nw):
        fr = base_img.copy(); draw_caption(fr, st["say"], k)
        p = TMP / f"s{n:03d}_{k:03d}.png"; fr.save(p, compress_level=1)
        d_k = (starts[k + 1] if k + 1 < nw else adur) - starts[k] + (PAD if k + 1 == nw else 0)
        lines.append(f"file '{p.as_posix()}'\nduration {max(d_k, 0.04):.3f}\n")
    lines.append(f"file '{(TMP / f's{n:03d}_{nw - 1:03d}.png').as_posix()}'\n")
    lst = TMP / f"s{n:03d}.txt"; lst.write_text("".join(lines))
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(wav), "-af", f"apad=pad_dur={PAD}",
                    "-t", f"{adur + PAD:.3f}", "-r", "30", "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-ar", "44100", "-ac", "1", str(mp4)], check=True)
    segs.append(mp4); durs.append(adur + PAD)
    for p in TMP.glob(f"s{n:03d}_*.png"): p.unlink()

lst = TMP / "list.txt"; lst.write_text("".join(f"file '{s.as_posix()}'\n" for s in segs))
raw = TMP / "raw.mp4"
subprocess.run([FF, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(raw)], check=True)

# presenter (lip-synced to the narration only, before the music is mixed in)
pres = TMP / "pres.mp4"
subprocess.run([sys.executable, PRESENTER, str(raw), str(pres)], check=True)

vw = TMP / "voice.wav"
subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(raw), "-ac", "1", "-ar", "44100", str(vw)], check=True)
with wave.open(str(vw)) as wv:
    v = np.frombuffer(wv.readframes(wv.getnframes()), dtype=np.int16).astype(np.float32) / 32768
bed = np.asarray(study_music.bed(len(v) / 44100), dtype=np.float32)
m = min(len(v), len(bed)); mix = v[:m] + bed[:m] * 0.4
mix /= max(1.0, np.abs(mix).max() * 1.05)
mw = TMP / "mix.wav"
with wave.open(str(mw), "wb") as wv:
    wv.setnchannels(1); wv.setsampwidth(2); wv.setframerate(44100); wv.writeframes((mix * 32767).astype(np.int16).tobytes())
tmp_final = ROOT / "videos" / (OUTNAME + ".tmp.mp4")
subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(pres), "-i", str(mw), "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", str(tmp_final)], check=True)
chk = subprocess.run([FF, "-v", "error", "-i", str(tmp_final), "-f", "null", "-"], capture_output=True, text=True)
if chk.stderr.strip():
    raise SystemExit("decode errors, not replacing final: " + chk.stderr[:300])
final = ROOT / "videos" / (OUTNAME + ".mp4")
os.replace(tmp_final, final)

t, chap, seen = 0.0, [], set()
for st, du in zip(steps, durs):
    if st["section"] not in seen:
        seen.add(st["section"]); chap.append((t, st["section"]))
    t += du
fmt = lambda x: f"{int(x // 60)}:{int(x % 60):02d}"
(ROOT / "chapters" / (OUTNAME + ".txt")).write_text("\n".join(f"{fmt(a)} {b}" for a, b in chap) + "\n", encoding="utf-8")
print(final, "total", fmt(t), round(t))
