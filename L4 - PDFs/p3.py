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

time.sleep(3)

ss3 = pyautogui.screenshot()
print(ss3.mode)
ss3.save("ss3.png")
print("ss3 saved")


pss1 = Image.open('ss1.png').convert('RGB')
pss2 = Image.open('ss2.png').convert('RGB')
pss3 = Image.open('ss3.png').convert('RGB')

pss1.save('p3.pdf', save_all = True, append_images = [pss2, pss3])
print('pdf saved')
