# 搜索 id ： com.tencent.mm:id/m7   zhonganzu
# 搜索结果： id  com.tencenet.mm:id/aqw 返回的是个列表，是第3个菜单，所以要用复数
# find_elements_by_xpath


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

driver.find_element_by_id("com.tencent.mm:id/r_").click() # 点击搜索图标
driver.find_element_by_id("com.tencent.mm:id/m7").send_keys("zhonganzu") # 键入搜索内容
sleep(3)


