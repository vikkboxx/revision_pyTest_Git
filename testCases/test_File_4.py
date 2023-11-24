import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)




class Test_pyTest:

    def test_OrangeHRM_008(self):
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(4)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.implicitly_wait(4)
        # Enter "Admin" into "Username"
        #time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # Enter "******" into "Password"
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # Click on "Login"
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # Click on Menu Button
        time.sleep(2)
        driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        # Click on "Logout"
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()


