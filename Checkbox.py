import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe") # r for raw string in order to avoid /n
driver.maximize_window()
driver.get("http://cookbook.seleniumacademy.com/Config.html")
driver.find_element_by_xpath("//input[@value='ABS']").click()
# driver.find_element_by_xpath("input[value='ABS']").click() by Css selector
#check the check box
airbags = driver.find_element_by_name("airbags")
if not airbags.is_selected(): # Check Unchecked Checkbox
    airbags.click()

time.sleep(3)

if airbags.is_selected(): #uncheck checked checkbox
    airbags.click()


