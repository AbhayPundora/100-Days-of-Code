import requests
from _datetime import datetime
import smtplib

MY_LAT = 29.379910
MY_LNG = 79.477386

#sending email
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="scjncksdjnc", password="sckjcsd")
        connection.sendmail(from_addr="scnkjscnkjdnc",
                            to_addrs="scnskcjndc",
                            msg="Subject:Look Up!\n\nISS is right above you"
        )


def is_iss_close():
    # Fetching ISS Position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)
    print(iss_position)

    return iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LNG <= iss_longitude + 5


def is_dark():
    # Fetching Sunrise and Sunset time according to my location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    print(sunrise)
    print(sunset)
    print(time_now)

    return sunset <= time_now <= sunrise


if is_iss_close() and is_dark():
    send_email()


# my_position = (MY_LAT,MY_LNG)


print(is_iss_close())
print(is_dark())
