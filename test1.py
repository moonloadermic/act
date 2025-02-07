import time
from DrissionPage import Chromium, ChromiumOptions
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()

co = ChromiumOptions().auto_port()

arguments = [
    "--disable-gpu",
    "--no-sandbox",
#    "--window-size=1920,1080",
    "--disable-dev-shm-usage",
]

for argument in arguments:
    co.set_argument(argument)

browser = Chromium(co)

tab = browser.latest_tab

# 访问网页
tab.get('https://github.com/trending')
print(tab.title)

ele = tab.ele('x:/html/body/div[1]/div[4]/main/div[1]/nav/div/a[1]')
print(ele.text)

ele.click()

print(tab.title)


browser.quit()
display.stop()
