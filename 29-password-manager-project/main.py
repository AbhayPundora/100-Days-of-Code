from tkinter import *
from tkinter import messagebox
from  random import  randint, shuffle, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    final_list = letter_list + symbol_list + number_list

    shuffle(final_list)

    final_password = "".join(final_list)

    password_input.insert(0,final_password)
    pyperclip.copy(final_password)

    # print(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def handle_submit():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")

    if is_ok:
        try:
            with open("my_pass.json",mode="r") as file:
                # reading old data
                data = json.load(file)
                # print(data)

        except FileNotFoundError:
            with open("my_pass.json", mode="w") as file:
                #saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)
            with open("my_pass.json", mode="w") as file:
                #saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)

# ---------------------------- SEARCH ------------------------------- #

def search_password():
    website_name = website_input.get().lower()
    try:
        with open("my_pass.json", "r") as file:
            data = json.load(file)
            website_data = data[website_name]
            email = website_data["email"]
            password = website_data["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No website named '{website_name}' Found.")
    else:
        messagebox.showinfo(title=website_name, message=f"Email {email} \nPassword: {password}")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#LABEL
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#INPUT
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

email_username_input = Entry(width=52)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "abhay@.com")

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=handle_submit)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)











window.mainloop()
