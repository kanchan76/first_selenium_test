import time

from selenium import webdriver

# creating object of chrome class
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe") # r for raw string in order to avoid /n
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/")
element = driver.find_element_by_id("loginname")
element.send_keys("stc123")
print(element.get_attribute("value"))
print(element.value_of_css_property("color"))
print(element.tag_name)
login_button = driver.find_element_by_id("loginbutton")
print("Is displayed = ",login_button.is_displayed())
print("Is Enabled - ", login_button.is_enabled())
print("Is selected - ",login_button.is_selected())
print(login_button.text)
element.clear()
print(label_element.get_attribute("for"))
