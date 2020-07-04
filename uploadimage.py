import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
#to modify file in git
#check check working directory

class UploadImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("http://the-internet.herokuapp.com/upload")
        cls.wait = WebDriverWait(cls.driver,10)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_uploadimage(self):
        self.driver.find_element_by_id("file-upload").send_keys('E:\\ghyj.png')
        self.driver.find_element_by_id("file-submit").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div[@class='example']/h3")))
        self.assertEqual(self.driver.find_element_by_xpath("//div[@class='example']/h3").text,'File Uploaded!')
