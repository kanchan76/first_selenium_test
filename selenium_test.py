import time

from selenium import webdriver

# creating object of chrome class
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe") # r for raw string in order to avoid /n
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/")
element = driver.find_element_by_id("loginname")
element.send_keys("stc123")
element.get_attribute("value")
print(type(element))
element2 = driver.find_element_by_id("loginpassword")
element2.send_keys("12345")
driver.find_element_by_id("loginbutton").click() #method Chaining
#driver.quit()
print(driver.title)
driver.get("http://www.google.com")
driver.back()
driver.forward()
#driver.find_element(by=By.ID, value="username")
print(driver.name)
driver.refresh()
# print(driver.page_source)
print(driver.current_url)
driver.minimize_window()
time.sleep(2)
driver.refresh()
driver.maximize_window()
print(driver.get_cookies())
driver.delete_all_cookies()
print(driver.get_cookies())

s= ""
s.title()