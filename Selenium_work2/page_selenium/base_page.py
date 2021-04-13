import json

from selenium import webdriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self._cookie()
        else:
            self.driver = base_driver

    def _cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        with open("../testcase_selenium/cookie.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")