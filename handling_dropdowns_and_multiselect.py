import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


class HandlingSelectTags(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This will get executed only once before the  setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        print("This will get executed only once after the  tearDown method for the last test")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="../resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_combo(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        make_element = self.driver.find_element_by_name("make")
        # all_options = make.find_elements_by_tag_name("option")
        make_select = Select(make_element)
        make_select.select_by_visible_text("Mercedes")
        time.sleep(3)
        make_select.select_by_value("honda")
        time.sleep(3)
        make_select.select_by_index(0)
        time.sleep(3)
        expected_options = ["BMW","Mercedes","Audi","Honda"]
        actual_options = []
        # options returns List of webelements
        for one_option in make_select.options:
            actual_options.append(one_option.text)

        self.assertListEqual(actual_options,expected_options)

        current_selection = make_select.first_selected_option # which option is current selected
        print(current_selection.text)
        self.assertListEqual(actual_options, expected_options)
    def test_multi_select(self):
        print("This test is to learn how to handle multi-select")

if __name__ == "__main__":
    unittest.main()