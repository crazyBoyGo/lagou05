# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy
from HogwartsLG5.test_appium.page.addresslist_page import AddressListPage
from HogwartsLG5.test_appium.page.basepage import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return AddressListPage(self.driver)
