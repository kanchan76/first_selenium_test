from selenium import webdriver

# creating object of chrome class
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\rajdeep.m\PycharmProjects\duringclass\resources/chromedriver.exe") # r for raw string in order to avoid /n
driver.maximize_window()
driver.get("http://selenium-examples.nichethyself.com/customised.html")
england = driver.find_element_by_xpath("//div[@class= 'checkbox-inline'][2]")
england = driver.find_element_by_xpath("//div[@class= 'checkbox-inline'][2]")
england.click()

driver.quit()