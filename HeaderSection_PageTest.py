import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class HeaderSection(unittest.TestCase):

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

    def test_HeaderSectionUi(self):
        website_logo = self.driver.find_element(By.XPATH, "//img[@alt='website logo']")
        self.assertTrue(website_logo.is_displayed(), "website_logo is not displayed")

    def test_NavbarSection(self):
        HomeNavbar_ele = self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
        self.assertTrue(HomeNavbar_ele.is_displayed(), "HomeNavbar_ele is not displayed")

    def test_NavbarSection2(self):
        PopularNavbar_ele = self.driver.find_element(By.XPATH, "//a[normalize-space()='Popular']")
        self.assertTrue(PopularNavbar_ele.is_displayed(), "PopularNavbar_ele is not displayed")

    def test_NavigationHome(self):
        NavigateTo_Home_ele = self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']")
        NavigateTo_Home_ele.click()
        time.sleep(3)
        self.assertIn("", self.driver.current_url, "navigate to home page is failed")

    def test_NavigationPopular(self):
        NavigateTo_Popular_ele = self.driver.find_element(By.XPATH, "//a[normalize-space()='Popular']")
        NavigateTo_Popular_ele.click()
        time.sleep(3)
        self.assertIn("popular", self.driver.current_url, "navigate to popular page is failed")

if __name__ == "__main__":
    unittest.main()