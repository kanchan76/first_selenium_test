# 1. Goto http://the-internet.herokuapp.com/dropdown and select 3rd option
# 2. Select any website which has all these things and try to automate.


import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class SelectAssignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once before the  setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_select_dropdown(self):
        self.driver.get("http://the-internet.herokuapp.com/dropdown")
        time.sleep(3)
        dropdown = Select(self.driver.find_element_by_id("dropdown"))
        dropdown.select_by_value("2")
        time.sleep(60)
