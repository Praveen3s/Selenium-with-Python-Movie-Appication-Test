import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class HeaderSection(unittest.TestCase):

    @classmethod
    def setUp(cls):
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
    def tearDown(cls):
        cls.driver.close()

    def test_SearchFunctionality(self):

        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@fill='none'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='search']").send_keys("titanic")
        self.driver.find_element(By.XPATH, "//button[@class='search-button']//*[name()='svg']").click()
        movies_list = self.driver.find_elements(By.XPATH, "//img[@alt='Titanic']")
        print(len(movies_list))
        self.assertGreater(len(movies_list), 0, "it is not showing any movie")

    def test_WrongSearchFunctionality(self):
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@fill='none'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Bahubali")
        self.driver.find_element(By.XPATH, "//button[@class='search-button']//*[name()='svg']").click()
        error_img = self.driver.find_element(By.XPATH, "//img[@alt='no movies']")
        error_img_text = error_img.text
        print(error_img_text)
        Nomovies_ele = self.driver.find_element(By.XPATH, "//p[@class='not-found-search-paragraph']")
        Invalid_Moviename = Nomovies_ele.text
        self.assertEqual(Invalid_Moviename, "Your search for Bahubali did not find any matches.", "It is not working properly")


if __name__ == "__main__":
    unittest.main()