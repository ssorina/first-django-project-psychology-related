from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_menu_element_on_homepage(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        menu = self.browser.find_element_by_class_name('menu').text
        self.assertIn('Home', menu)

    def test_message_form_on_page(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        subject = self.browser.find_element_by_name('subject')
        subject.send_keys('Post')

        message = self.browser.find_element_by_name('message')
        message.send_keys('My message is good')

        sender = self.browser.find_element_by_name('sender')
        sender.send_keys('test@test.com')

        self.assertEqual(subject, 'Post')

if __name__ == "__main__":
    unittest.main()
