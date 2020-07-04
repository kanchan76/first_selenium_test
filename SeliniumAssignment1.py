import time
from selenium import webdriver

# creating object of chrome class
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe") # r for raw string in order to avoid /n
driver.maximize_window()
driver.get("http://login.yahoo.com")
username = driver.find_element_by_id("login-username")
username.send_keys("kanchan7696")
driver.find_element_by_xpath("//input[@id='login-signin']").submit()
time.sleep(3)
password = driver.find_element_by_id("login-passwd")
password.send_keys("aarav17yahoo")
driver.find_element_by_id('login-signin').submit()
time.sleep(7)

driver.quit()