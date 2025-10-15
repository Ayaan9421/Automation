import pyautogui
from PIL import Image


ss = pyautogui.screenshot()
logo = Image.open('k.png')
logo = logo.resize((100,100))


position = (10, 10)

ss.paste(logo, position, logo)

ss.save("ssl.png")