# 1. http://the-internet.herokuapp.com/tables -
#      Example 2 - Delete the row containing jdoe in Email Column.
import time
import unittest
from selenium import webdriver

from first_selenium_test.Webtable import WebtableOptimized


class WebtableAssignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once before the  setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_combo(self):
        self.driver.get("http://the-internet.herokuapp.com/tables")
        table = WebtableOptimized(self.driver.find_element_by_id("table1"))
        print(table.get_row_count())
        print(table.get_column_count())
        print(table.get_data_rows())
        table.delete_a_row("First Name","Jason")
        time.sleep(3)
        table.delete_a_row("First Name", "Jason")
        time.sleep(3)
