from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000/home/')

    def tearDown(self):
        self.browser = webdriver.Firefox()
        self.browser.quit()

    def test_page_contains_both_h1(self):
        self.browser = webdriver.Firefox()
        menu = self.browser.find_elements_by_class_name('menu')

        assert 'Home' in menu
