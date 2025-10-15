import pyautogui
import os
from PIL import Image

ss = pyautogui.screenshot()
ssw, ssh  = ss.width, ss.height
print(ssw, ssh)

sf = "sf.png"
ss.save(sf)

ss_size = os.path.getsize(sf)

rss = ss.resize((1280, 768))
rf = "rss.png"
rss.save(rf)
rss_size = os.path.getsize(rf)

diff = ss_size - rss_size

print("Full size: ", round(ss_size/1024, 2), " kb")
print("Resized size: ", round(rss_size/1024, 2), " kb")
print("Diff: ", round(diff/1024, 2), " kb")

