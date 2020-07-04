import time
import unittest
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
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe")
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

    def test_multi_select(self):
        self.driver.get("http://cookbook.seleniumacademy.com/Config.html")
        time.sleep(3)
        color = Select(self.driver.find_element_by_name("color"))
        color.deselect_all()
        color.select_by_index(2)
        color.select_by_visible_text("Silver")
        color.select_by_value("br")
        expected_selected_colors=['White',"Brown","Silver"]
        actual_selected_colors = []
        for one_selected_options in color.all_selected_options:
            actual_selected_colors.append(one_selected_options)
        self.assertListEqual(expected_selected_colors,actual_selected_colors)
