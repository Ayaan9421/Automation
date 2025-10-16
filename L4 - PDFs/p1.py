import pyautogui
from PIL import Image

ss = pyautogui.screenshot()
print(ss.mode)
ss.save("ss.png")
print("ss saved")

pss = Image.open('ss.png').convert('RGB')
pss.save('p1.pdf')
print('pdf saved ')
