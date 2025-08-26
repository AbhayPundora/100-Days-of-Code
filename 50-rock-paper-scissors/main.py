import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import random

GYM_URL = "https://rockpaperscissors-ai.vercel.app/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)


rock = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[1]/button[1]')
paper = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[1]/button[2]')
scissor = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[1]/button[3]')

my_moves = [rock, paper, scissor]

def play_game():
    current_move = random.choice(my_moves)
    current_move.click()
    print(f"Your Move: {current_move.text}")

    ai_move = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[3]')
    print(f"AI Move: {ai_move.text}")

    my_score = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[1]/p[1]')
    ai_score = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[1]')

    result = driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[2]/p')
    print(result.text)

    print(f"My Score: {my_score.text}\nAI Score: {ai_score.text}")



while "10" not  in driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[3]/div[3]/p').text:
    time.sleep(2)
    play_game()


my_final_score = int(driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[1]/p[1]').text)
ai_final_score = int(driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div/div[1]/div[3]/div[1]/div[2]/p[1]').text)

if my_final_score > ai_final_score:
    print(f"You Win, {my_final_score}-{ai_final_score}")
elif ai_final_score > my_final_score:
    print(f"You Lose, {ai_final_score}-{my_final_score}")
else:
    print(f"Draw, {my_final_score}-{ai_final_score}")

