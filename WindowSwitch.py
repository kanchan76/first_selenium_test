import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException
from selenium.webdriver.support.select import Select


class HandlingSelectTags(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://cookbook.seleniumacademy.com/Config.html")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")
        cls.driver.quit()

    def setUp(self):
        print("Nothing required for now")

    def test_window_alert(self):
        parent_window = self.driver.current_window_handle # window is a unique identification given by OS to all the open windows
        helpbutton = self.driver.find_element_by_id("helpbutton")
        helpbutton.click()
        try:
            self.driver.switch_to.window("HelpWindow")
        except NoSuchWindowException:
            self.fail("No help Window Found. ")
        self.assertEquals(self.driver.title,"Help","not help")
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(parent_window)

