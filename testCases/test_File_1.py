import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

from selenium.webdriver.common.service import Service

headless_option = webdriver.ChromeOptions()
headless_option.add_argument('headless')

class Test_pyTest:

    def test_sum_001(self):
        a = 4
        b = 3
        sum_ab = a + b

        print(sum_ab)

    def test_mutiply_002(self):
        x = 5
        y = 4
        multi = x * y

        if multi == 20:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_sum_003(self):
        x = 5
        y = 4
        sum_xy = x * y

        if sum_xy == 10:
            assert True
        else:
            assert False

    def test_credence_registration_004(self):
        driver = webdriver.Chrome(options=headless_option)
        driver.implicitly_wait(4)
        driver.get('https://automation.credence.in/shop')

        driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        driver.find_element(By.ID, 'name').send_keys("Vikas Ahireism")
        driver.find_element(By.ID, 'email').send_keys("vikasahire004@gmail.com")
        driver.find_element(By.ID, 'password').send_keys("vikasahireism123")
        driver.find_element(By.ID, 'password-confirm').send_keys("vikasahireism123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        if driver.title == 'CredKart':
            print("Success !")
        else:
            print("Failed !")






