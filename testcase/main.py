import unittest
from selenium import webdriver
import page


class pythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print("setup")
        # avoid tbscerticate
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--ignore-certificate-errors')
        # #

        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()  
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self) -> None:
        print("teardowns")
        self.driver.close()


if __name__ == "__main__":
    unittest.main()