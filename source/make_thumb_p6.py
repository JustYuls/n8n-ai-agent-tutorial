"""Thumbnail for Part 6 (1280x720): real crop of the n8n canvas after a manual run of the scheduled workflow + words that complement the title."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, "D:/MIT/SirYulsTV")
import make_short as ms  # noqa: E402

NAVY, YELLOW, WHITE, GREEN, CARD = ms.NAVY, ms.YELLOW, ms.WHITE, ms.GREEN, ms.CARD
f = ms.font

img = Image.new("RGB", (1280, 720), NAVY)
d = ImageDraw.Draw(img)
d.rectangle((0, 0, 1280, 14), fill=YELLOW)
d.rounded_rectangle((50, 46, 420, 112), 33, fill=YELLOW)
d.text((82, 58), "n8n  |  TAGALOG", font=f(38), fill=NAVY)
d.text((50, 125), "SCHEDULE", font=f(135), fill=WHITE)
d.text((50, 280), "= WALANG CLICK", font=f(100), fill=YELLOW)
d.rounded_rectangle((760, 40, 1230, 116), 38, fill=GREEN)
d.text((800, 52), "7:00 AM DAILY", font=f(44), fill=NAVY)
shot = Image.open(HERE / "shots_part6" / "h02_manual-run.jpg").convert("RGB").crop((120, 230, 1340, 480))
shot = shot.resize((1000, round(shot.height * 1000 / shot.width)))
d.rounded_rectangle((120, 410, 1160, 410 + shot.height + 30), 26, fill=CARD, outline=YELLOW, width=5)
img.paste(shot, (140, 425))
d.text((50, 660), "Kusang tumatakbo  |  Libre", font=f(36), fill="#9DB0D8")
(ROOT / "thumbnails").mkdir(exist_ok=True)
img.save(ROOT / "thumbnails" / "06_n8n-schedule-trigger-tagalog.png")
print("thumbnail saved")
