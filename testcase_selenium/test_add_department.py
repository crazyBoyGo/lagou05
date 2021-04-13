from test01.pageobject.Selenium_work2.page_selenium.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()

    def test_department(self):

        self.main.goto_contact().goto_adddepartment().add_department()