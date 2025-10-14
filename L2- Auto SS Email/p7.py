import pyautogui
import time
from PIL import ImageDraw, ImageFont
from ema import send_email

def auto_ss(interval, total):
        for i in range(total):
                for j in range(interval):
                        print(f"Next SS in {j+1}\r", end="", flush=True)
                        time.sleep(1)
                ss = pyautogui.screenshot()
                ti = time.strftime("%Y%m%d_%H%M%S")
                draw = ImageDraw.Draw(ss)
                position = (1400,1000)
                color = (255, 0, 0)
                f = ImageFont.truetype("times.ttf", 60)
                draw.text(position, ti, fill=color, font=f)
                filename = f'as_{ti}.png'
                ss.save(filename)
                send_email(filename)

interval = int(input("Enter interval: "))
tot = int(input("Enter no of ss: "))

auto_ss(interval, tot)

