# Assignment2
# go to http://cookbook.seleniumacademy.com/Config.html/ and try to switch
# between multiple windows ("Help", "Online Chat Support" and "Visit US")
#
# go to http://www.demoqa.com/browser-windows and try to switch between multiple windows
#
# http://the-internet.herokuapp.com/windows
#
# Assignment4
# goto http://the-internet.herokuapp.com/frames and select the frames link and navigate between frames
# Navigate in nested frames.
#
# Assignemnt5
# google the difference between frame and iframe
#checking for git test2
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchWindowException


class SwitchFrameWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://cookbook.seleniumacademy.com/Config.html")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_Help(self):
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_id("helpbutton").click()
        try:
            self.driver.switch_to.window("HelpWindow")
            help_window_handle = self.driver.current_window_handle
            print(help_window_handle)
        except NoSuchWindowException:
            print("Help window was expected but not present.")
        self.assertEquals(self.driver.title,"Help","Title do not match")
        self.driver.close()
        self.driver.switch_to.window(parent_window)

    def test_chat(self):
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_id("chatbutton").click()
        try:
            all_open_window = self.driver.window_handles
            for one_window in all_open_window:
                if one_window != parent_window:
                    self.driver.switch_to.window(one_window)
                    self.driver.find_element_by_id("closebutton").click()
                    self.driver.switch_to.window(parent_window)
        except NoSuchWindowException:
            print("Help window was expected but not present.")

    def test_visit(self):
        parent_window = self.driver.current_window_handle
        self.driver.find_element_by_id("visitbutton").click()
        try:
            self.driver.switch_to.window("VisitUsWindow")
            visit_window_handle = self.driver.current_window_handle
            print(visit_window_handle)
        except NoSuchWindowException:
            print("visit window was expected but not present.")
        self.assertEquals(self.driver.title,"Visit Us","Title do not match")
        self.driver.close()
        self.driver.switch_to.window(parent_window)









