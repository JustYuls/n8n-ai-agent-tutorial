"""Thumbnail for Part 3 (1280x720): real crop of the Excel window with the logged rows + words that complement the title."""
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
d.text((50, 140), "AUTO-SAVE", font=f(140), fill=WHITE)
d.text((50, 295), "EVERY CHAT", font=f(100), fill=YELLOW)
d.rounded_rectangle((800, 330, 1230, 410), 40, fill=GREEN)
d.text((835, 342), "2 ROWS, TAMA", font=f(46), fill=NAVY)
shot = Image.open(HERE / "shots_part3" / "x03.jpg").convert("RGB").crop((50, 560, 1215, 708))
d.rounded_rectangle((40, 450, 1240, 450 + shot.height + 30), 26, fill=CARD, outline=YELLOW, width=5)
img.paste(shot, (62, 465))
d.text((50, 650), "Walang Google account  |  Libre", font=f(40), fill="#9DB0D8")
(ROOT / "thumbnails").mkdir(exist_ok=True)
img.save(ROOT / "thumbnails" / "03_n8n-ai-agent-excel-study-tracker-tagalog.png")
print("thumbnail saved")
