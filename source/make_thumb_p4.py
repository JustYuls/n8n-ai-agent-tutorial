"""Thumbnail for Part 4 (1280x720): real crop of the green n8n canvas after the test run + words that complement the title."""
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
d.text((50, 125), "WEBHOOK", font=f(150), fill=WHITE)
d.text((50, 280), "= 1 TAWAG", font=f(100), fill=YELLOW)
d.rounded_rectangle((800, 300, 1230, 380), 40, fill=GREEN)
d.text((835, 312), "28.1 C, TAMA", font=f(46), fill=NAVY)
shot = Image.open(HERE / "shots_part4" / "p08_canvas-success.jpg").convert("RGB").crop((60, 240, 1020, 432))
shot = shot.resize((1000, round(shot.height * 1000 / shot.width)))
d.rounded_rectangle((120, 410, 1160, 410 + shot.height + 30), 26, fill=CARD, outline=YELLOW, width=5)
img.paste(shot, (140, 425))
d.text((50, 660), "Libreng API  |  Walang key", font=f(36), fill="#9DB0D8")
(ROOT / "thumbnails").mkdir(exist_ok=True)
img.save(ROOT / "thumbnails" / "04_n8n-webhook-api-tagalog.png")
print("thumbnail saved")
