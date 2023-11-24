import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)




class Test_pyTest:

    def test_credence_007(self):
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(4)

        driver.get('https://credence.in/')

        time.sleep(2)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()

        time.sleep(2)

        num_list = driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a")

        contact_list = []
        for r in range(1, len(num_list) + 1):
            num = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a[" + str(
                r) + "]").text
            contact_list.append(num)

        if '+91 9091929355' in contact_list:
            assert True
        else:
            assert False

