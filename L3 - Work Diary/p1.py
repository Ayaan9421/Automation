import pyautogui
import os

css = pyautogui.screenshot()
cf = "css.png"
css.save(cf)
css_size = os.path.getsize(cf)

bss = css.convert('L')
bf = "bss.png"
bss.save(bf)
bss_size = os.path.getsize(bf)


diff = css_size - bss_size

print("Colored size: ", round(css_size / 1024, 2), " kb")
print("B/w size: ", round(bss_size / 1024, 2), " kb")
print("Size Diff: ", round(diff / 1024, 2), " kb")
