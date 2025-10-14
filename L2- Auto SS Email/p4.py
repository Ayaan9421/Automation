import pyautogui
import time


ss = pyautogui.screenshot()

ti = time.strftime("%Y%m%d_%H%M%S")
ss.save(f'as_{ti}.png')