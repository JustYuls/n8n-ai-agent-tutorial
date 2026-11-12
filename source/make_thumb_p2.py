"""Thumbnail for Part 2 (1280x720): real crop of the chat widget on the author's own page + words that complement the title."""
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
d.text((50, 150), "ADD A", font=f(150), fill=WHITE)
d.text((50, 315), "CHAT BUBBLE", font=f(100), fill=YELLOW)
shot = Image.open(HERE / "shots_part2" / "p14.jpg").convert("RGB").crop((600, 6, 1037, 560))
h = 560
shot = shot.resize((round(shot.width * h / shot.height), h), Image.LANCZOS)
x0 = 1240 - shot.width - 10
d.rounded_rectangle((x0 - 10, 130, 1240, 130 + h + 20), 26, fill=CARD, outline=YELLOW, width=5)
img.paste(shot, (x0, 140))
d.rounded_rectangle((50, 470, 520, 560), 45, fill=GREEN)
d.text((90, 485), "2250.08  TAMA", font=f(52), fill=NAVY)
d.text((50, 600), "Walang Telegram  |  Libre", font=f(40), fill="#9DB0D8")
(ROOT / "thumbnails").mkdir(exist_ok=True)
img.save(ROOT / "thumbnails" / "02_n8n-chatbot-website-tagalog.png")
print("thumbnail saved")
