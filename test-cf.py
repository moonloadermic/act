import subprocess
import time
from DrissionPage import Chromium, ChromiumOptions
from pyvirtualdisplay import Display

url = 'https://test.aiuuo.com/'
ele_for_check_path = 'x:/html/body/pre'
ele_for_check_text = 'Hello World!'

display = Display(visible=0, size=(1920, 1080))
display.start()

co = ChromiumOptions().auto_port()

arguments = [
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
#    "--window-size=1920,1080",    
]

for argument in arguments:
    co.set_argument(argument)


browser = Chromium(co)

tab = browser.latest_tab

tab.get(url)
tab.wait.load_start()
time.sleep(2)
ele = tab.ele('.:zone-name-title')
print(ele.text)

#返回元素左上角在屏幕中的坐标
loc = ele.rect.screen_location
print(loc)

x=loc[0]+38
y=loc[1]+195

time.sleep(2)

bypass = False

#每隔1秒进行一次点击，最多5次
for i in range(5):
    command = ['xdotool', 'mousemove', str(x), str(y), 'click', '1']
    subprocess.run(command)	        
    try:
        time.sleep(5)
        ele_for_check = tab.ele(ele_for_check_path)
        if ele_for_check.text == ele_for_check_text:
            print(ele_for_check.text)
            print("恭喜！验证通过。")
            bypass = True
            break
    except:
        time.sleep(1)

if not bypass:
    print("很遗憾，验证没有通过。")

time.sleep(5)
browser.quit()
display.stop()

        



