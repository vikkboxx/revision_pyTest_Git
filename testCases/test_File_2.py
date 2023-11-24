import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


class Test_pyTest:

    def test_sum_005(self):
        a = 4
        b = 3
        sum_ab = a + b

        if sum_ab == 7:
            assert True
        else:
            assert False

    # Write a test case to check if a particular number is present in a contact list

    def test_credence_login_006(self):
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(4)

        driver.get('https://automation.credence.in/shop')
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys('vikasahire0004@gmail.com')
        driver.find_element(By.ID, "password").send_keys('vikas123')
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        if driver.title == 'CredKart':
            assert True
        else:
            assert False



