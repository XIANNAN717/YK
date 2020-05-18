# com.tencent.mm:id/m7
# 小程序下拉选择顺丰： find_elements_by_id(com.tencenet.mm:id/ka")[0].click() 返回的是个列表，是第3个菜单，所以要用复数


from appium import webdriver
from time import sleep

ServerUrl= "http://127.0.0.1:4723/wd/hub"
desired_caps = {"platform":"Android",
                "platformVersion":"9",
                "devicesName" : "XXXXXX",
                "appPakage":"",
                "appActivity":"",
                "unicodeKeyboard": True,
                "resetKeyBoard"  : True,
                "chromeOption" : {"androidProcess" : "com.tencent.mm:tools"}
}

driver = webdriver.Remote(ServerUrl, desired_caps)

print(driver.context)

# 向下滑动
def swipe_down(driver, t=500, n=1):
    s = driver.get_window_size()
    print(s)
    x1 = s['width'] * 0.5  # x坐标
    y1 = s['height'] * 0.25  # 起点y坐标
    y2 = s['height'] * 0.75  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

swipe_down(driver)


driver.find_element_by_id("com.tencent.mm:id/r_").click() # 点击搜索图标
driver.find_element_by_id("com.tencent.mm:id/m7").send_keys("zhonganzu") # 键入搜索内容
sleep(3)


