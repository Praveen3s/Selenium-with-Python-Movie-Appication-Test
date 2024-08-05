import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class HomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        ser_obj = Service("C:\\drivers\\chromedriver-win64\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser_obj, options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://qamoviesapp.ccbp.tech/login")
        cls.driver.maximize_window()
        cls.driver.find_element(By.XPATH, "//input[@id='usernameInput']").send_keys("rahul")
        cls.driver.find_element(By.XPATH, "//input[@id='passwordInput']").send_keys("rahul@2021")
        time.sleep(3)  # This is not ideal, consider using WebDriverWait
        cls.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_heading_text(self):
        home_movie_ele = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/h1")
        home_movie_text = home_movie_ele.text
        self.assertEqual(home_movie_text, "Trending Now", "home_movie_text is not Trending Now")

    def test_heading_text2(self):
        home_movie_ele2 = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Originals']")
        home_movie_text2 = home_movie_ele2.text
        self.assertEqual(home_movie_text2, "Originals", "home_movie_text is not Originals")

    def test_play_button(self):
        playButton_Ele = self.driver.find_element(By.XPATH, "//button[normalize-space()='Play']")
        self.assertTrue(playButton_Ele.is_displayed(), "Play button element is not displayed")

    def test_movies_section1(self):
        trends_movies_ele = self.driver.find_elements(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div")
        print(len(trends_movies_ele))
        self.assertGreater(len(trends_movies_ele), 0, "No movies are displayed in trending section")

    def test_movies_section2(self):
        popular_movies_ele = self.driver.find_elements(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div")
        print(len(popular_movies_ele))
        self.assertGreater(len(popular_movies_ele), 0, "No movies are displayed in popular section")

    def test_contact_us(self):
        contact_ele = self.driver.find_element(By.XPATH, "//p[@class='contact-us-paragraph']")
        self.assertTrue(contact_ele.is_displayed(), "Contact us is not displayed")

if __name__ == "__main__":
    unittest.main()
