import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        ser_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser_obj, options=options)
        cls.driver.get("https://qamoviesapp.ccbp.tech/login")
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_website_logoTest(self):
        website_logo = self.driver.find_element(By.XPATH, "//img[@alt='login website logo']")
        self.assertTrue(website_logo.is_displayed(), "website_logo is not displayed")

        heading_ele = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Login']")
        heading_text = heading_ele.text
        self.assertEqual(heading_text, "Login", "heading text not equal")


    def test_labelText(self):
        username_label = self.driver.find_element(By.XPATH, "//label[normalize-space()='USERNAME']")
        username_text = username_label.text
        self.assertEqual(username_text, "USERNAME", "Username label text is not 'USERNAME'")

        password_label = self.driver.find_element(By.XPATH, "//label[normalize-space()='PASSWORD']")
        password_text = password_label.text
        self.assertEqual(password_text, "PASSWORD", "Password label text is not 'PASSWORD'")

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        self.assertTrue(login_button.is_displayed(), "Login button is not displayed")

    def test_emptyInputFields(self):
        username_empty_field = self.driver.find_element(By.XPATH, "//input[@id='usernameInput']")
        username_empty_field.send_keys("")
        password_empty_field = self.driver.find_element(By.XPATH, "//input[@id='passwordInput']")
        password_empty_field.send_keys("")

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        error_message1 = self.driver.find_element(By.XPATH, "//p[contains(@class, 'error-message')]")
        self.assertTrue(error_message1.is_displayed(), "Error message is not displayed")

    def test_usernameEmpty(self):
        self.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("rahul@2021")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        error_message2 = self.driver.find_element(By.XPATH, "//p[contains(@class, 'error-message')]")
        self.assertTrue(error_message2.is_displayed(), "Error message is not displayed")


    def test_passwordEmpty(self):
        self.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("rahul")
        self.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        error_message3 = self.driver.find_element(By.XPATH, "//p[contains(@class, 'error-message')]")
        self.assertTrue(error_message3.is_displayed(), "Error message is not displayed")

    def test_wrongCredentials(self):
        self.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("rahul")
        self.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("praveen@2021")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(3)
        error_message4 = self.driver.find_element(By.XPATH, "//p[contains(@class, 'error-message')]")
        self.assertTrue(error_message4.is_displayed(), "Error message is not displayed")

    def test_rightCredentials(self):
        self.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("rahul")
        self.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("rahul@2021")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

        WebDriverWait(self.driver, 10).until(EC.url_contains("dashboard"))
        self.assertIn("dashboard", self.driver.current_url, "successful login do not redirect to dashboard")

if __name__ == "__main__":
    unittest.main()