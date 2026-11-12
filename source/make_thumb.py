"""Thumbnail (1280x720): real n8n canvas crop + 4 words that complement the title. Run: python make_thumb.py"""
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
# chip
d.rounded_rectangle((50, 46, 420, 112), 33, fill=YELLOW)
d.text((82, 58), "n8n  |  TAGALOG", font=f(38), fill=NAVY)
# headline: 4 words, does not repeat the title
d.text((50, 150), "AI THAT", font=f(150), fill=WHITE)
d.text((50, 315), "USES TOOLS", font=f(100), fill=YELLOW)
# real canvas crop
shot = Image.open(HERE / "shots" / "s32_final-canvas.jpg").convert("RGB").crop((415, 185, 1050, 535))
shot = shot.resize((520, round(350 * 520 / 635)), Image.LANCZOS)
d.rounded_rectangle((700, 405, 1240, 405 + shot.height + 20), 28, fill=CARD, outline=YELLOW, width=5)
img.paste(shot, (710, 415))
# result pill
d.rounded_rectangle((50, 500, 470, 590), 45, fill=GREEN)
d.text((85, 515), "2250.08  TAMA", font=f(48), fill=NAVY)
d.text((50, 630), "Libre. Walang API key.", font=f(40), fill="#9DB0D8")
(ROOT / "thumbnails").mkdir(exist_ok=True)
img.save(ROOT / "thumbnails" / "01_n8n-ai-agent-tutorial-tagalog.png")
print("thumbnail saved")
