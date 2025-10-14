import pyautogui
import time
from PIL import ImageDraw, ImageFont


ss = pyautogui.screenshot()

ti = time.strftime("%Y%m%d_%H%M%S")

draw = ImageDraw.Draw(ss)
position = (1400,1000)
color = (255, 0, 0)
f = ImageFont.truetype("times.ttf", 60)
draw.text(position, ti, fill=color, font=f)

ss.save(f'as_{ti}.png')