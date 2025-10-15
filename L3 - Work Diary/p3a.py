import pyautogui
from PIL import Image


ss = pyautogui.screenshot()
logo = Image.open('k.png')
logo = logo.resize((100,100))


position = (1800, 960)

ss.paste(logo, position, logo)

ss.save("ssl.png")