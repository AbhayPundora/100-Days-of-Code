from selenium import webdriver
import time

from selenium.common import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import os
from dotenv import load_dotenv
load_dotenv()

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INSTA_URL = "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(INSTA_URL)

    def login(self):
        print("login")

        input_username = self.wait.until(ec.presence_of_element_located((By.NAME, "username")))
        input_username.send_keys(USERNAME)

        time.sleep(3)

        input_password = self.driver.find_element(By.NAME, "password")
        input_password.send_keys(PASSWORD)

        time.sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]//div[text()="Log in"]')
        login_button.click()


    def find_followers(self):
        print("find")
        try:
            # Wait up to 5 seconds for "Not now" button
            not_now_button = self.wait.until(
                ec.presence_of_element_located((By.XPATH, "//div[@role='button' and text()='Not now']"))
            )
            not_now_button.click()
            print("Clicked 'Not now'")
        except:
            print("'Not now' button not present")


        try:
            time.sleep(15)
            search_button = self.driver.find_element(By.XPATH, "//a[@role='link']//span[text()='Search']")
            search_button.click()


            time.sleep(10)
            search_input = self.driver.find_element(By.XPATH, "//input[@aria-label='Search input']")
            search_input.send_keys(SIMILAR_ACCOUNT)

            time.sleep(10)
            similar_account = self.driver.find_element(By.XPATH, f"//a[@href='/{SIMILAR_ACCOUNT}/']")
            similar_account.click()

        except NoSuchElementException:
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")


        time.sleep(10)
        similar_account_followers = self.driver.find_element(By.XPATH, "// a[ @ href = '/piyushgarg_dev/followers/']")
        similar_account_followers.click()

        time.sleep(15)
        # To access the followers pop-up.

        # not worked for me
        # scroll_box = self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))


        scrollable_div = self.driver.find_element(By.XPATH, "//div[@class='x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")

        # last_height = self.driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        last_height = 0
        while True:
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div
            )
            time.sleep(2)

            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", scrollable_div
            )
            if new_height == last_height:
                break  # no more to load
            last_height = new_height

    def follow(self):
        follower_list = self.driver.find_elements(By.XPATH,
                                             "//div[contains(@class, 'xdj266r') and contains(@class, 'x1plvlek')]")

        # Loop through each element and find the "Follow" button
        for f in follower_list:
            try:
                follow_button = f.find_element(By.XPATH,
                                              ".//button[contains(@class, '_aswp _aswr _aswu _asw_ _asx2')]")

                follow_button.click()
                print(f"Clicked follow button")
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            time.sleep(1)


bot = InstaFollower()

bot.login()
time.sleep(3)

bot.find_followers()
time.sleep(3)

bot.follow()