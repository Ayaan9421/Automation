import pyautogui
import os

ss = pyautogui.screenshot()

f = os.listdir(".")

cnt = 0
for d in f:
        if d.startswith("fss_") and d.endswith(".png"):
                cnt += 1

ss.save(f'fss_{cnt+1}.png')
