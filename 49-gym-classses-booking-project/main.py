from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import os

import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait

ACCOUNT_EMAIL = "pundora3@test.com"
ACCOUNT_PASSWORD = "helloabhay3"
PROFILE_PATH = r"C:\Users\abhay\PycharmProjects\49\Gym_Profile_2"



GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={PROFILE_PATH}")

driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)


wait = WebDriverWait(driver, 2)

booked = 0
waitlist_joined = 0
already_booked_or_wishListed = 0

new_booking = []
new_waitlist = []

attempts = 0

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
    submit_btn.click()






def booking_function(day, day_title, card):
    global booked, waitlist_joined, already_booked_or_wishListed
    if day in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "7:00 AM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            if "ClassCard_booked" in button.get_attribute("class"):
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked_or_wishListed += 1

            elif "ClassCard_waitlisted" in button.get_attribute("class"):
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                already_booked_or_wishListed += 1

            else:
                if "ClassCard_available" in button.get_attribute("class"):
                    print(f"✓ Successfully Booked: {class_name} on {day_title}")
                    booked += 1
                    new_booking.append(class_name + "on" + day_title)

                else:
                    print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                    waitlist_joined += 1
                    new_waitlist.append(class_name + "on" + day_title)

                max_attempts = 5
                attempt = 0

                while attempt < max_attempts:
                    try:
                        wait.until(ec.element_to_be_clickable(button)).click()

                        if "Booked" in button.text or "Waitlisted" in button.text:
                            break
                    except:
                        pass

                    attempt += 1
                    time.sleep(1)

                if attempt == max_attempts:
                    print(f"❌ Failed to book {class_name} on {day_title} after {max_attempts} tries")



def book_class():
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for card in class_cards:
        # Get the day title from the parent day group
        day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        # Check if this is a Tuesday
        booking_function("Tue", day_title=day_title, card=card)
        booking_function("Thu", day_title=day_title, card=card)

    # print("--- BOOKING SUMMARY ---")
    # print(f"Classes booked: {booked}")
    # print(f"Waitlists joined: {waitlist_joined}")
    # print(f"Already booked/waitlisted: {already_booked_or_wishListed}")

    total_classes = booked + waitlist_joined + already_booked_or_wishListed
    print(f"Total Tuesday and Thursday 6pm classes processed: {total_classes}")

    # print("--- DETAILED CLASS LIST ---")
    #
    # for booking in new_booking:
    #     print(f"  • [New Booking] {booking}")
    #
    # for waitlist in new_waitlist:
    #     print(f"  • [New Waitlist] {waitlist}")
    #
    # if len(new_booking) == 0 and len(new_waitlist):
    #     print("No new Booking Recently")

    my_booking_button = driver.find_element(By.ID, value="my-bookings-link")
    my_booking_button.click()

    my_booking_page = wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

    all_classes = new_booking + new_waitlist
    check_booking_count = 0

    print("--- VERIFYING ON MY BOOKINGS PAGE ---")

    my_classes = my_booking_page.find_elements(By.CSS_SELECTOR, value="div[class^=MyBookings_bookingCard]")
    # print(my_classes)

    if not my_classes:
        raise NoSuchElementException("No booking found")

    else:
        for my_class in my_classes:
            class_title = my_class.find_element(By.TAG_NAME, value="h3").text

            if "Booking" in my_class.find_element(By.TAG_NAME, value="button").text:
                if class_title in new_booking:
                    print(f"✓ Verified: {class_title}")
                    check_booking_count += 1

            if "Waitlist" in my_class.find_element(By.TAG_NAME, value="button").text:
                print("y")
                if class_title in new_booking:
                    print(f"✓ Verified: {class_title} (Waitlist)")
                    check_booking_count += 1

    if len(new_booking) == 0:
        print("No new Bookings")


    check_booking_count = len(all_classes) - check_booking_count # bcz check booking count check all present classes in the booking page, and all classes just contain the fresh requests of this script

    print("--- VERIFICATION RESULT ---")
    print(f"Expected: {len(all_classes)} bookings")
    print(f"Found: {check_booking_count} bookings")

    if len(all_classes) == check_booking_count:
        print("✅ SUCCESS: All bookings verified!")

    else:
        print(f"❌ MISMATCH: Missing {len(all_classes) - check_booking_count} bookings")




def retry(login_func, book_func):
    global attempts
    login_func()

    try:
        time.sleep(2)
        schedule_page = driver.find_element(By.ID, "schedule-page")

        print(schedule_page)

    except NoSuchElementException:
        attempts += 1
        print(f"Attempts: {attempts}")
        retry(login_func, book_func)

    else:
        book_func()


retry(login, book_class)

#
# #first solution ======>
#
# # day_title = schedule_page.find_element(By.XPATH, '//*[@id="day-group-tue,-aug-19"]')
# #
# # classes_list = day_title.find_elements(By.CLASS_NAME, "ClassCard_card__KpCx5")
# #
# #
# # class_to_book = random.choice(classes_list)
# # class_to_book_button = class_to_book.find_element(By.CSS_SELECTOR, "button")
# # class_to_book_button.click()
# #
# # day_title_text = day_title.find_element(By.CSS_SELECTOR, value="h2").text
# #
# # print(f"✓ Booked: {class_to_book.text.split("\n")[0]} on {day_title_text}")
#
#
# #second solution =====>
#
# # days = schedule_page.find_elements(By.CSS_SELECTOR, value="div[id^=day-group-]")
# #
# #
# # for day in days:
# #     day_title = day.find_element(By.CSS_SELECTOR, value="h2").text
# #
# #     if "Tue" in day_title:
# #         classes_list = day.find_elements(By.CLASS_NAME, "div[class^=ClassCard_card]")
# #
# #         for cl in classes_list:
# #             time = cl.find_element(By.CSS_SELECTOR, value="p[id^=class-time-]").text
# #             if "6:00 AM" in time:
# #                 class_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button")))
# #                 class_button.click()
#
#
#
# #final =====>
