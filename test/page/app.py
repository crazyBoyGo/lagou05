from appium import webdriver

from test.page.base_page import BasePage
from test.page.main import Main


class App(BasePage):
    def start(self):
        _package="com.xueqiu.android"
        _activity=".view.WelcomeActivityAlias"
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "wework"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermission"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package, _activity)
        return self

    def main(self):
        return Main(self._driver)
