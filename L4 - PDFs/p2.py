import time
import pyautogui
from PIL import Image

ss1 = pyautogui.screenshot()
print(ss1.mode)
ss1.save("ss1.png")
print("ss1 saved")

time.sleep(3)

ss2 = pyautogui.screenshot()
print(ss2.mode)
ss2.save("ss2.png")
print("ss2 saved")

pss1 = Image.open('ss1.png').convert('RGB')
pss2 = Image.open('ss2.png').convert('RGB')

pss1.save('p2.pdf', save_all = True, append_images = [pss2])
print('pdf saved')
