# Assignment1 (doubleClick)
# http://only-testing-blog.blogspot.in/2014/09/selectable.html
# - "Double click me to see alert" - double click
# - alert ok button click
#
# Assignment2 (In WebDriver - moveToElement)
# - Anna assignment
# 1. goto http://annauniv.edu/
# 2. click on "Departments" link
# 3. Goto "Faculty Of Civil Engineering" and click on "Institute for Ocean Management"
# 4. Verify the page title.
# 5. Goto "Research Themes" options and Click "Coastal Pollution Monitoring and Hazards"
# 6. Verify the page title.
# Assignment4
# 1. Go to google.com
# 2. Click on Gmail link such that it opens in the same window in a new tab
# 3. then login into Gmail.
# 4. Come back to google.com tab and search on "jobs in Selenium"
#
# Assignment5
# 1. Go to http://cookbook.seleniumacademy.com/DoubleClickDemo.html
# 2. Double click on the blue area and verify whether it turns to yellow
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ActionAssignments(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Nothing for now")

    @classmethod
    def tearDownClass(cls):
        print("Nothing for now")

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"../resources\ChromeDriver83/chromedriver.exe")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver,20)

    def tearDown(self):
        self.driver.quit()

    def test_assignment2(self):
        self.driver.get("http://annauniv.edu/")
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,'Departments')))
        department = self.driver.find_element_by_link_text('Departments')
        self.driver.execute_script("arguments[0].click();", department)
        self.wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'link13')))
        self.builder = ActionChains(self.driver)
        self.builder.move_to_element(self.driver.find_element_by_name("link13")).perform()
        self.builder.move_to_element(self.driver.find_element_by_id("menuItemHilite32")).click().perform()
        oceanmanagementtitle = "Institute For Ocean Management - Anna University offers M.Tech in Coastal Management. ENVIS Center for Coastal Zone Management and Coastal Shelterbelts"
        self.wait.until(expected_conditions.title_contains(oceanmanagementtitle))
        self.assertTrue(self.driver.title,oceanmanagementtitle)
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Research Themes")))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_link_text("Research Themes")).perform()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("menuItemHilite13")).click().perform()
        costalmanagementtitle = ":: IOM - Institute For Ocean Management -  Anna University ::"
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Research Themes > Coastal pollution  monitoring and hazards')]")))
        self.assertTrue(self.driver.title, costalmanagementtitle)





    def test_assignment(self):
        self.driver.get("https://www.google.com/")
        mainwindow = self.driver.current_window_handle
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Gmail")))
        link = self.driver.find_element_by_link_text("Gmail")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        signin = self.driver.find_element_by_link_text("Sign in")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(signin).key_up(Keys.CONTROL).perform()
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "identifierId")))
        self.driver.find_element_by_id("identifierId").send_keys("uhfhw")
        self.driver.switch_to.window(mainwindow)
        self.wait.until(expected_conditions.visibility_of_element_located((By.NAME, "q")))
        self.driver.find_element_by_name("q").send_keys("jobs in Selenium")
        ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()




    def test_assignment5(self):
        self.driver.get("http://cookbook.seleniumacademy.com/DoubleClickDemo.html")
        builder = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID,"message")))
        message_box = self.driver.find_element_by_id("message")
        orginalcolor = message_box.value_of_css_property("color")
        builder.double_click(message_box).perform()
        self.assertTrue((orginalcolor != message_box.value_of_css_property("color")))


