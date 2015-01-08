from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

#from django.test import LiveServerTestCase
import unittest


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_titles_are_on_page(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        title = self.browser.find_elements_by_tag_name('h1')
        self.assertEqual(title[0].text, 'Mental health issues explained:')
        self.assertEqual(title[1].text, 'Our registered psychologists:')

    def test_menu_element_on_homepage(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        menu = self.browser.find_element_by_class_name('menu').text
        self.assertIn('Home', menu)

    def test_message_form_on_page(self):
        #open up homepage
        response = self.browser.get('http://127.0.0.1:8000/home/')
        #find subject field in the form on page and enter input
        subject = self.browser.find_element_by_name('subject')
        subject.send_keys('Post')
        #find message field and enter input
        message = self.browser.find_element_by_name('message')
        message.send_keys('My message is good')
        #find sender field and enter email address
        sender = self.browser.find_element_by_name('sender')
        sender.send_keys('test@test.com')
        #after input was entered, click on the submit button
        send = self.browser.find_element_by_xpath(
            '/html/body/form/input[2]')
        send.send_keys(Keys.ENTER)

        self.assertRedirects(response, 'http://127.0.0.1:8000/home/')


    def test_form_sender_accepts_email_format_only(self):
        self.browser.get('http://127.0.0.1:8000/home/')
        #put invalid email format in sender field
        sender = self.browser.find_element_by_name('sender')
        sender.send_keys('asdf')
        send = self.browser.find_element_by_xpath(
            '/html/body/form/input[2]')
        send.send_keys(Keys.ENTER)
        #generate the expected alert and verify text
        alert = self.browser.switch_to_alert()
        alert_text = Alert.text

        self.assertEqual(alert_text, 'Please enter an email address.')

    def test_redirected_to_correct_post(self):
        response = self.browser.get('http://127.0.0.1:8000/home/')
        post = self.browser.find_element_by_link_text('fghgfh').click()

        self.assertRedirects(response, '/home/24/')

if __name__ == "__main__":
    unittest.main()
