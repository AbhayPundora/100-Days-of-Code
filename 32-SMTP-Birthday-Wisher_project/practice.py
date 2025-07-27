import  smtplib
import datetime as dt
import random

my_email = "exmail"
password = "cbdcbsdhcbhd"

with open("quotes.txt") as file:
    data = file.readlines()
    quote = random.choice(data)

    now = dt.datetime.now()
    # year = now.year
    # print(now)
    # print(year)

    current_week = now.weekday()

    if current_week == 3:

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="anotheremail",
                                msg=f"Subject:motivational quote\n\n{quote}"
                                )






