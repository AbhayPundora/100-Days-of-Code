from operator import index

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#scraping amazon

# driver.get("https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDV7GC/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.MvgIitW9HqcWHlfONwYKQAzdj2K8ut0R-6Pzna2VyjxDCokrC9ztwHNFM3QhIuSw2yobPCwZ3IRq486TngA5tbH2uxhQp4jF793ZauHbMpcEtYCbFyGaKGlj7QFGudVJ74NXqdRkPKtheeM4Vnqqag8dEuVeX2qTuLEDTdCz_K4uHGfc3vEadvkmDkTOcBQ3TBRdRoGvEN7jiNy0lM1AgsZxV2HAuRdk-BuO6mkwN0E.9r9N10SxCquykKbLId68G37qYbA1tAF3PenrwOVvsBs&dib_tag=se&keywords=macbook&qid=1754988579&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

# print(driver.page_source)
# price_rupees = driver.find_element(By.CSS_SELECTOR, value="span.priceToPay span.a-price-whole")
# print(price_rupees.text)

# price_rupees = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
# print(price_rupees.text)

#scraping python.org

driver.get("https://www.python.org/")

upcoming_events =  driver.find_elements(By.CLASS_NAME, value="shrubbery")[1]
# print(upcoming_events.find_elements("time"))

event_dates = upcoming_events.find_elements(By.CSS_SELECTOR, value=".menu time")
event_names = upcoming_events.find_elements(By.CSS_SELECTOR, value=".menu a")


dates = [date.get_attribute("datetime").split("T")[0] for date in event_dates]
# print(dates)

names = [name.text for name in event_names]
# print(names)

event_list = [{"time": dates[i], "name": names[i]} for i in range(len(dates))]
# print(event_list)

event_dict = {i : event_list[i] for i in range(len(event_list))}
print(event_dict)



# driver.close() #close the active tab
driver.quit() #close the entire browser