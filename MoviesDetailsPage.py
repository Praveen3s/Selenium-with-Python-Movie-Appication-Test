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

    def test_HomeUIElements(self):
        self.driver.find_element(By.XPATH, "//img[@alt='No Time to Die']").click()
        movie_title = self.driver.find_element(By.XPATH, "//h1[normalize-space()='No Time to Die']")
        self.assertTrue(movie_title.is_displayed(), "movie_title is not displayed")

        movie_review_container = self.driver.find_element(By.XPATH, "//div[@class='movie-review-container']")
        self.assertTrue(movie_review_container.is_displayed(), "movie_review_container is not displayed")

        movie_overview = self.driver.find_element(By.XPATH, "//p[@class='movie-overview']")
        self.assertTrue(movie_overview.is_displayed(), "movie_overview is not displayed")

        Play_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Play']")
        self.assertTrue((Play_button.is_displayed(), "Play_button is not displayed"))

        genres_category = self.driver.find_element(By.XPATH, "//div[@class='genres-category']")
        self.assertTrue(genres_category.is_displayed(), "genres_category is not displayed")

        audio_category = self.driver.find_element(By.XPATH, "//div[@class='audio-category']")
        self.assertTrue(audio_category.is_displayed(), "audio_category is not displayed")

        rating_category = self.driver.find_element(By.XPATH, "//div[@class='rating-category']")
        self.assertTrue(rating_category.is_displayed(), "rating-category is not displayed")

        budget_category = self.driver.find_element(By.XPATH, "//div[@class='budget-category']")
        self.assertTrue(budget_category.is_displayed(), "budget_category is not displayed")

    def test_popularUIEle(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Popular']").click()
        self.driver.find_element(By.XPATH, "//img[@alt='Black Widow']").click()

        popular_movie_title = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Black Widow']")
        self.assertTrue(popular_movie_title.is_displayed(), "popular_movie_title is not displayed")

        pop_movie_review_container = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Black Widow']")
        self.assertTrue(pop_movie_review_container.is_displayed(), "movie_review_container is not displayed")

        movie_overview = self.driver.find_element(By.XPATH, "//p[@class='movie-overview']")
        self.assertTrue(movie_overview.is_displayed(), "movie_overview is not displayed")

        Play_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Play']")
        self.assertTrue((Play_button.is_displayed(), "Play_button is not displayed"))

        genres_category = self.driver.find_element(By.XPATH, "//div[@class='genres-category']")
        self.assertTrue(genres_category.is_displayed(), "genres_category is not displayed")

        audio_category = self.driver.find_element(By.XPATH, "//div[@class='audio-category']")
        self.assertTrue(audio_category.is_displayed(), "audio_category is not displayed")

        rating_category = self.driver.find_element(By.XPATH, "//div[@class='rating-category']")
        self.assertTrue(rating_category.is_displayed(), "rating-category is not displayed")

        budget_category = self.driver.find_element(By.XPATH, "//div[@class='budget-category']")
        self.assertTrue(budget_category.is_displayed(), "budget_category is not displayed")




if __name__ == "__main__":
    unittest.main()