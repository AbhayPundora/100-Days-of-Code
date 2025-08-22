import os
from email.message import EmailMessage

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import lxml
import  requests
import smtplib
import re

load_dotenv()

PRODUCT_URL = "https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDV7GC/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.MvgIitW9HqcWHlfONwYKQAzdj2K8ut0R-6Pzna2VyjxDCokrC9ztwHNFM3QhIuSw2yobPCwZ3IRq486TngA5tbH2uxhQp4jF793ZauHbMpcEtYCbFyGaKGlj7QFGudVJ74NXqdRkPKtheeM4Vnqqag8dEuVeX2qTuLEDTdCz_K4uHGfc3vEadvkmDkTOcBQ3TBRdRoGvEN7jiNy0lM1AgsZxV2HAuRdk-BuO6mkwN0E.9r9N10SxCquykKbLId68G37qYbA1tAF3PenrwOVvsBs&dib_tag=se&keywords=macbook&qid=1754988579&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
DESIRED_PRICE = 94000
SMTP_HEADER = os.getenv("SMTP_HEADER")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

headers = {
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
  }


response = requests.get(url=PRODUCT_URL, headers=headers)
contents = response.text


soup = BeautifulSoup(contents, "lxml")
# print(soup.prettify())


#for static(practice site)

#price_whole = soup.find(name="span", class_="a-price-whole").getText().split(".")[0]
# price_dec = soup.find(name="span", class_="a-price-decimal").getText()
# price_frac = soup.find(name="span", class_="a-price-fraction").getText()
# print(price_whole, price_dec, price_frac)
# price = float(price_whole + price_dec + price_frac)
# print(price)

price_whole = soup.find(name="span", class_="a-price-whole").getText().replace(",","").replace(".","")
# print(price_whole)
product_title = soup.find(name="span", id="productTitle").getText().strip()
clean_title = re.sub(r"\s+", " ", product_title).strip()

price_symbol =  soup.find(name="span", class_="a-price-symbol").getText()

price = int(price_whole)
# print(price)


def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Amazon Price Alert!"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    msg.set_content(f"{clean_title} is now {price_symbol}{price}\n\n{PRODUCT_URL}")
    with smtplib.SMTP(SMTP_HEADER) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)

if price < DESIRED_PRICE:
    send_email()
    print("Email is sent successfully😄")


