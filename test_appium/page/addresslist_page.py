# 点击添加成员
from HogwartsLG5.test_appium.page.basepage import BasePage
from HogwartsLG5.test_appium.page.memberinvit_page import MemberInvitePage


class AddressListPage(BasePage):
    def add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)
