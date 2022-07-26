from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By


class Test_GetBaidu:
    def test_GetBaidu(self):
        #获得chrome浏览器驱动
        driverChrome = webdriver.Chrome( )
        #打开百度网站
        driverChrome.get("http://www.baidu.com")
        time.sleep(1)
        #浏览器最大化
        driverChrome.maximize_window()
        time.sleep(1)
        #设置浏览器大小
        #driverChrome.set_window_size(800,600)
        #time.sleep(1)
        #刷新浏览器

        #使用超链接text内容定位
        driverChrome.refresh()
        time.sleep(2)
        link_textElement = driverChrome.find_element(By.LINK_TEXT, "新闻").click()
        time.sleep(3)
        driverChrome.quit()
        assert "ok"=="ok"