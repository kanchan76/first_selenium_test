# Go to https://the-internet.herokuapp.com/javascript_alerts
#   1. "Click for JS Alert" - click on this option, handle the alert,
#       read the message and verify. Also verify the text displayed under Result is
#       "You successfuly clicked an alert" and it is in green color.
#       Repeat same for other two buttons having different alerts
#  2. go to http://www.cookbook.seleniumacademy.com/Alerts.html
#  and handle all the three alerts and verify the messages on the home page.


import unittest
from selenium import webdriver
import time
from selenium.common.exceptions import NoAlertPresentException


class AlertAssignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("Nothing required for now")

    def tearDown(self):
        print("Nothing required for now")

    def test_simple_alert(self):
        self.driver.find_element_by_xpath('//button[@onclick = "jsAlert()"]').click()
        try:
            simple_alert = self.driver.switch_to.alert
            actual_message = simple_alert.text
            self.assertEquals(actual_message,"I am a JS Alert")
            time.sleep(3)
            simple_alert.accept()
        except NoAlertPresentException:
            print("No alert present.")

    def test_confirm_alert(self):
        self.driver.find_element_by_xpath('//button[@onclick = "jsConfirm()"]').click()
        try:
            simple_alert = self.driver.switch_to.alert
            actual_message = simple_alert.text
            self.assertEquals(actual_message,"I am a JS Confirm")
            time.sleep(3)
            simple_alert.dismiss()
            self.assertEquals(self.driver.find_element_by_id('result').text,"You clicked: Cancel")

        except NoAlertPresentException:
            print("No alert present.")

    def test_prompt_alert(self):
        self.driver.find_element_by_xpath('//button[@onclick = "jsPrompt()"]').click()
        try:
            simple_alert = self.driver.switch_to.alert
            actual_message = simple_alert.text
            self.assertEquals(actual_message,"I am a JS prompt")
            time.sleep(3)
            simple_alert.send_keys("Good morning")
            simple_alert.accept()
            self.assertEquals(self.driver.find_element_by_id('result').text,"You entered: Good morning")

        except NoAlertPresentException:
            print("No alert present.")




