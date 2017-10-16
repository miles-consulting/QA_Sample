#!/usr/bin/env python 
import unittest
from selenium import webdriver

baseURL = "http://localhost:8080"

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(baseURL)

    def testHomePage(self):
        driver = self.browser
        self.assertEqual('Home Page', driver.title)

    def testWeclome(self):
        welcome_msg = None
        driver = self.browser
        welcome_msg = driver.find_element_by_id("welcome")
        #assert value isn't empty
        self.assertTrue(welcome_msg.text)

    def testCopyright(self):
        copyright_msg = None
        driver = self.browser
        copyright_msg = driver.find_element_by_id("copyright")
        #assert value isn't empty
        self.assertTrue(copyright_msg.text)

    def testUserTable(self):
        tbody = None
        table = self.browser.find_element_by_tag_name("tbody")
        #ensure element exists
        self.assertTrue(table)
        rows = table.find_elements_by_tag_name("tr");
        account_driver = webdriver.Firefox()
        for row in rows:
            name_cell = row.find_element_by_class_name("user_name")
            name_anchor = name_cell.find_element_by_tag_name("a")
            self.assertTrue(name_anchor.text)
            name_link = name_anchor.get_attribute('href')
            self.assertTrue(name_link)

            email_cell = row.find_element_by_class_name("user_email")
            email_anchor = email_cell.find_element_by_tag_name("a")
            email_link = email_anchor.get_attribute('href')
            self.assertRegex(email_link, 'mailto:.+@+.+\.+.+')
            self.assertTrue(email_anchor.text)

            self.helperTestAccountPage(name_link, account_driver)
        account_driver.quit()

    def helperTestAccountPage(self,link, account_driver):
        account_driver.get(link)
        name_cell = account_driver.find_element_by_id("name")
        self.assertTrue(name_cell.text)
    
        email_cell = account_driver.find_element_by_id("email")
        email_anchor = email_cell.find_element_by_tag_name("a")
        self.assertTrue(email_anchor.text)
        email_link = email_anchor.get_attribute('href')
        self.assertRegex(email_link, 'mailto:.+@+.+\.+.+')
        self.assertTrue(email_anchor.text)

        website_cell = account_driver.find_element_by_id("website")
        website_anchor = website_cell.find_element_by_tag_name("a")
        self.assertTrue(website_anchor.text)
        website_link = website_anchor.get_attribute('href')
        self.assertTrue(website_link)

        location_cell = account_driver.find_element_by_id("location")
        location_anchor= location_cell.find_element_by_tag_name("a")
        self.assertTrue(location_cell.text)
        location_link = location_anchor.get_attribute('href')
        self.assertTrue(location_link)

        copyright_msg = None
        copyright_msg = account_driver.find_element_by_id("copyright")
        #assert value isn't empty
        self.assertTrue(copyright_msg.text)

        button = account_driver.find_element_by_class_name('btn-primary')
        self.assertTrue(button.text == "Back")
        button.click()

        self.assertTrue(account_driver.title == "Home Page")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)




