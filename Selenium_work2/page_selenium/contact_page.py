from selenium.webdriver.common.by import By

from test01.pageobject.Selenium_work2.page_selenium.add_department_page import AddDepartment
from test01.pageobject.Selenium_work2.page_selenium.base_page import BasePage


class ContactPage(BasePage):
    def goto_adddepartment(self):
        self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartment(self.driver)
