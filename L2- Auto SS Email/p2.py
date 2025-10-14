import pyautogui

ss = pyautogui.screenshot(region=(0,0,500,200))
ss.save("spss.png")