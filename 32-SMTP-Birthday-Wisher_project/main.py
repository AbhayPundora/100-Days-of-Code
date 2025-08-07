

##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "exmail"
MY_PASSWORD = "dcjndjcjds"

current_date = dt.datetime.now()
current_day = current_date.day
current_month = current_date.month

print(current_day)
print(current_month)

birthday_people = pandas.read_csv("birthdays.csv")

people_to_wish = {person.birthday_person: person.email for (_, person) in birthday_people.iterrows() if current_day == person.day and current_month == person.month}

names = list(people_to_wish.keys())

for name in names:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        # print(name)
        data = letter.readlines()
        content = [line.replace("[NAME]", name) for line in data]

        formated_letter = "".join(content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=people_to_wish[name], msg=f"Subject:Happy Birthday\n\n{formated_letter}")





