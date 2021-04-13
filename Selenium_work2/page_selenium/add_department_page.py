from selenium.webdriver.common.by import By

from test01.pageobject.Selenium_work2.page_selenium.base_page import BasePage


class AddDepartment(BasePage):
    def add_department(self):
        self.driver.find_element(By.NAME, "name").send_keys("研发部")
        self.driver.find_element(By.CSS_SELECTOR, ".js_parent_party_name").click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688853140036157_anchor']").click()
        self.driver.find_element(By.XPATH, "//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()
