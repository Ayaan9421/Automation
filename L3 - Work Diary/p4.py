import pyautogui
import os
from PIL import ImageOps

ss = pyautogui.screenshot()
sf = "snb.png"
ss.save(sf)

border_ss = ImageOps.expand(ss, border=20, fill='red')
border_ss.save('sb.png')

