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

    def test_AllUIEle(self):
        Account_button = self.driver.find_element(By.XPATH, "//img[@alt='profile']")
        Account_button.click()


        Account_ELE = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Account']")
        self.assertTrue(Account_ELE.is_displayed(), "Account is not disPLAYED")

        Member_ship_ele = self.driver.find_element(By.XPATH, "//p[normalize-space()='Member ship']")
        self.assertTrue(Member_ship_ele.is_displayed(), "Member_ship_ele is not displayed")

        membership_username_ele = self.driver.find_element(By.XPATH, "//p[@class='membership-username']")
        self.assertTrue(membership_username_ele.is_displayed(), "membership_username_ele is not displayed")

        membership_password_ele = self.driver.find_element(By.XPATH, "//p[@class='membership-password']")
        self.assertTrue(membership_password_ele.is_displayed(), "membership_password_ele is not displayed")

        Plan_details_ele = self.driver.find_element(By.XPATH, "//p[normalize-space()='Plan details']")
        self.assertTrue(Plan_details_ele.is_displayed(), "Plan_details_ele is not displayed")

        plan_paragraph = self.driver.find_element(By.XPATH, "//p[@class='plan-paragraph']")
        self.assertTrue(plan_paragraph.is_displayed(), "plan_paragraph is not displayed")

        plan_details = self.driver.find_element(By.XPATH, "//p[@class='plan-details']")
        self.assertTrue(plan_details.is_displayed(), "plan-details is not displayed")

        Logout_ele = self.driver.find_element(By.XPATH, "//button[normalize-space()='Logout']")
        self.assertTrue(Logout_ele.is_displayed(), "Logout_ele is not displayed")

        footer_icons_container = self.driver.find_element(By.XPATH, "//div[@class='footer-icons-container']")
        self.assertTrue(footer_icons_container.is_displayed(), "footer_icons_container is not displayed")

        contact_us_paragraph = self.driver.find_element(By.XPATH, "//p[@class='contact-us-paragraph']")
        self.assertTrue(contact_us_paragraph.is_displayed(), "contact_us_paragraph is not displayed")

if __name__ == "__main__":
    unittest.main()