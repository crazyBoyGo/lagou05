from selenium.webdriver.common.by import By
from test01.pageobject.work.page_selenium.base_page import BasePage
from test01.pageobject.work.page_selenium.contact_page import ContactPage


class MainPage(BasePage):
    def goto_contact(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']/span").click()
        return ContactPage(self.driver)



