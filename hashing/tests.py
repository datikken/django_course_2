from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib

# class FunctionalTestCase(TestCase):
    # def setUp(self):
    #     self.browser = webdriver.Firefox()
    #
    # def test_home_page_response(self):
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn('install', self.browser.page_source)
    #
    # def test_home_page_has_input(self):
    #     self.browser.get('http://localhost:8000')
    #     text = self.browser.find_element_by_id('user_input')
    #     text.send_keys('hello')
    #     self.browser.find_element_by_name('submit').click()
    #     self.assertIn('', self.browser.page_source)
    #
    # def tearDown(self):
    #     self.browser.quit()

class UnitTestCase(TestCase):
    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())

    def test_hash_farsh(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)
