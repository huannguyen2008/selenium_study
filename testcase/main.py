import os
import unittest
from selenium import webdriver
import page

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
WEBDRIVER = 'chromedriver'
path = os.path.join(ROOT_DIR, WEBDRIVER)


class PythonOrgSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(path)
        self.driver.get('http://www.python.org')

    def test_title(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = 'pycon'
        main_page.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
