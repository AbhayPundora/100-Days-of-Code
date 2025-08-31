from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv

load_dotenv()


PROFILE_PATH = r"C:\Users\abhay\PycharmProjects\51\complain"

SPEED_TEST_URL = "https://www.speedtest.net/"
X_URL = "https://twitter.com/"
MY_USERNAME = os.getenv("MY_USERNAME")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument(f"--user-data-dir={PROFILE_PATH}")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)


    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        wait = WebDriverWait(self.driver, 6)
        go = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a.js-start-test.test-mode-multi")))
        go.click()
        print("h")

        time.sleep(50)

        download_speed = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print("Down: " + download_speed)
        print("Up: " + upload_speed)

        self.down = download_speed
        self.up = upload_speed

    def tweet_at_provider(self, down, up):

        self.driver.get(X_URL)

        login_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '// *[ @ id = "react-root"] / div / div / div[2] / main / div / div / div[1] / div / div / div[3] / div[4] / a')))
        login_button.click()

        name_field = self.wait.until(ec.presence_of_element_located((By.NAME, "text")))
        name_field.send_keys(MY_USERNAME)


        # next_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/button[2]')
        # next_button.click()

        next_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button//span[text()="Next"]')))
        next_button.click()

        password_field = self.wait.until(ec.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(MY_PASSWORD)

        confirm_buttton = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//button[@data-testid="LoginForm_Login_Button"]')))
        confirm_buttton.click()

        new_post_button = self.wait.until(ec.element_to_be_clickable((By.XPATH, '//a[@data-testid="SideNav_NewTweet_Button"]')))
        new_post_button.click()

        textarea = self.wait.until(ec.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]')))
        textarea.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {down}down/{up}up?")

        make_post_button = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="tweetButton"]')))
        make_post_button.click()


