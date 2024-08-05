import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class PopularPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=serv_obj, options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://qamoviesapp.ccbp.tech/login")
        cls.driver.maximize_window()
        cls.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("rahul")
        cls.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("rahul@2021")
        time.sleep(3)
        cls.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_Popular_moviePage(self):
        Popular_ele = self.driver.find_element(By.XPATH, "//a[normalize-space()='Popular']")
        Popular_ele.click()
        movies_lst = self.driver.find_elements(By.XPATH, "//div[@class='search-movies-container']//li")
        print(len(movies_lst))
        self.assertGreater(len(movies_lst), 0, "In popular page the movies are displayed")


if __name__ == "__main__":
    unittest.main()