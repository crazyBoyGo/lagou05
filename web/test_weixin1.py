import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestbaidu():
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9999"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)

    def test_testbaidu(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@id='indexTop']/div[2]/aside/a[1]").click()
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()

if __name__ == '__main__':
    pytest.main(['-s'])
