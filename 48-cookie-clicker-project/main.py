from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(7)

language = driver.find_element(By.CLASS_NAME, value="langSelectButton")
language.click()

time.sleep(7)

timeout = time.time() + 30

cookie_button = driver.find_element(By.ID, value="bigCookie")

# unlocked_skills = driver.find_element(By.CSS_SELECTOR, value=".disabled .content .price")
# print(unlocked_skills.text)



while True:
    if time.time() > timeout:
        break

    click_time = time.time() + 60*5
    while True:
        if time.time() > click_time:
            break
        cookie_button.click()

    cookie_count_tag = driver.find_element(By.ID, value="cookies")
    cookie_count = int(cookie_count_tag.text.split(" ")[0])
    print(cookie_count)

    unlocked_products = driver.find_elements(By.CSS_SELECTOR, ".product.enabled")
    print(unlocked_products)

    if unlocked_products:
        skill_list = [int(skill.find_element(By.CLASS_NAME, value="price").text) for skill in unlocked_products]
        ids = [skill.get_attribute("id") for skill in unlocked_products]
        print(skill_list)
        print(ids)

    max_price = max(skill_list)
    max_index = skill_list.index(max_price)
    max_id = ids[max_index]
    print(max_id)

    expansive_product = driver.find_element(By.ID, value=max_id)
    print(expansive_product)
    expansive_product.click()



cookie_count_tag = driver.find_element(By.ID, value="cookies")
cookies_per_sec = cookie_count_tag.text.split(" ")[3]
print(f"cookies/second: {cookies_per_sec}")

