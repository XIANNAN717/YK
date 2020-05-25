# com.tencent.mm:id/m7
# 小程序下拉
# 选择顺丰： find_elements_by_id("com.tencenet.mm:id/ka")[0].click() 返回的是个列表，是第3个菜单，所以要用复数


from appium import webdriver
from time import sleep
from public.common.desired_caps import desired
from public.po.base_view import BaseView

des = desired()
b = BaseView(des)

b.swipe_down()





