from datetime import datetime
import pyautogui 
from PIL import Image, ImageOps
import ema
import time

print("monitoring Started  ", datetime.now())
try:
        while True:
                ss = pyautogui.screenshot()
                
                # color to bw
                ss = ss.convert('L')

                # resize
                ss.resize((800, 400))

                # logo
                logo = Image.open('k.png')
                logo = logo.resize((100, 100))
                position = (10, 10)
                ss.paste(logo, position, logo)

                ss = ImageOps.expand(ss, border=20, fill='red')

                ss.save("wda_ss.png")
                print("SS taken")
                ema.send_email("wda_ss.png")

                for i in range(20, 0, -1):
                        print("Next SS after ", i , " seconds \r", end="", flush=True)
                        time.sleep(1)

except KeyboardInterrupt:
        print("monitoring over  ", datetime.now())