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
tab.get('https://www.baidu.com/')

ele = tab.ele('x://*[@id="s-top-left"]/a[2]')
print(ele.text)

tab2 = ele.click.for_new_tab()  # 点击获取新tab对象
print(tab2.title)

ele_for_check = tab2.ele('x://*[@id="govsite-top"]/a[1]')
if ele_for_check.text == 'hao123推荐':
    print(ele_for_check.text)
    print("找到")

browser.quit()
display.stop()
