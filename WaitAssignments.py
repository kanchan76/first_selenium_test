# Assigment 1:  In Yahoomail login, remove Thread.sleep and implict Wait and replace with explicit wait
# Assignment 2: Before Clicking on compose, remove Thread.sleep and replace with explicit wait
# Assignment 3: Yahoo Logout implementation

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Yahoo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        #cls.driver.implicitly_wait(8)
        cls.wait = WebDriverWait(cls.driver, 20,poll_frequency=0.5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://login.yahoo.com")

    def tearDown(self):
        self.driver.close()

    def test_yahoologin(self):
        try:
            username = self.driver.find_element_by_id("login-username")
            username.send_keys("kanchan7696")
            self.driver.find_element_by_xpath("//input[@id='login-signin']").submit()
            self.wait.until(expected_conditions.visibility_of_element_located((By.NAME,"password")))
            password = self.driver.find_element_by_name("password")
            password.send_keys("aarav17yahoo")
            self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "login-signin")))
            self.driver.find_element_by_id('login-signin').submit()
            self.wait.until(expected_conditions.visibility_of_element_located((By.ID,"atomic")))
            if self.driver.find_element_by_id("atomic") in self.driver.page_source:
                self.assertTrue(True,"Login successful")
            else:
                self.assertFalse(False,"Login unsuccessful")


        except NoSuchElementException:
            self.fail("No such Element Found")

    def test_compose(self):

        try:
            self.test_yahoologin()
            self.wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "D(ib) H(46px) Mstart(14px) Mt(5px) Va(t) tab wafer-fetch wf-trigger-activated wafer-fetch-complete")))
            self.driver.find_element_by_class_name("D(ib) H(46px) Mstart(14px) Mt(5px) Va(t) tab wafer-fetch wf-trigger-activated wafer-fetch-complete").click()
            self.wait.until(expected_conditions.visibility_of_element_located((By.ID,"compose-button")))
            self.driver.find_element_by_id("compose-button").click()
        except NoSuchElementException:
            self.fail("No such Element found")

    def test_logout(self):
        self.test_compose()
        try:
            self.driver.find_element_by_id("ybarAccountMenu")
            self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "compose-button")))
            self.driver.find_element_by_link_text("Sign out").click()
        except NoSuchElementException:
            self.fail("No such Element found")









