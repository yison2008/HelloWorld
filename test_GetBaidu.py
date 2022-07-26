import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_GetBaidu():
    def setup_method(self, method):
        self.driverChrome = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driverChrome.quit()

    def test_GetBaidu(self):
        self.driverChrome.get("http://www.baidu.com")
        time.sleep(1)
        # 浏览器最大化
        self.driverChrome.maximize_window()
        time.sleep(1)

        # 使用超链接text内容定位
        self.driverChrome.refresh()
        time.sleep(1)
        self.driverChrome.find_element(By.LINK_TEXT, "新闻").click()
        time.sleep(2)
