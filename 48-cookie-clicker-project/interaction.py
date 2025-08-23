from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.get("https://secure-retreat-92358.herokuapp.com/")

# links = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")


# num_of_articles = links[1].text
# print(num_of_articles)

# links[1].click()

# num_of_articles = 0
#
# for link in links:
#     if link.get_attribute("title") == "Special:Statistics":
#         num_of_articles = link.text
#
# print(num_of_articles)

# pages = driver.find_element(By.LINK_TEXT, value="Pages")
# pages.click()

# search_icon = driver.find_element(By.CLASS_NAME, value="mw-ui-icon-search")
# search_icon.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

#sign-up page

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Abhay")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Pundora")

email = driver.find_element(By.NAME, value="email")
email.send_keys("abhay@gmail.com")

button = driver.find_element(By.CLASS_NAME, value="btn")
button.click()



# driver.quit()
