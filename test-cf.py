import subprocess
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

# 使用该配置对象创建页面
browser = Chromium(co)

tab = browser.latest_tab


bypass = False

for i in range(2):
    try:
        print(f"正在开始第{i+1}次尝试")
        tab.get('https://test.aiuuo.com/')
        tab.wait.load_start()
        ele = tab.ele("@name=cf-turnstile-response").parent()
        #ele = tab.ele("@name=cf-turnstile-response")
        checkbox = ele.sr('t:iframe')('t:body').sr('t:input')
        ele2 = checkbox.next(2)
        print(ele2.text)
        loc = ele2.rect.screen_midpoint
        print(loc)
        x = loc[0]
        y = loc[1]
        print(x,y)	
        time.sleep(2)
        command = ['xdotool', 'mousemove', str(x), str(y), 'click', '1']
        subprocess.run(command)		
        try:
            time.sleep(5)
            ele_for_check = tab.ele('x:/html/body/pre')
            if ele_for_check.text == 'Hello World!':
                print(ele_for_check.text)
                print(f"恭喜！第{i+1}次尝试验证通过。")
                bypass = True
                break
        except:
            time.sleep(1)

    except:
        print(f"第{i+1}次尝试，复选框未找到")

if not bypass:
    print("很遗憾，两次验证没有通过。")

time.sleep(5)
browser.quit()
display.stop()
