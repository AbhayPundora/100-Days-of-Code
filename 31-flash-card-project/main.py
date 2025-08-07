from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
keys = []


window = Tk()
window.title("Fleshy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)


#reading data
try:
    data = pandas.read_csv("data/world_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR , highlightthickness=0)
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 260, image=front_card)
canvas.grid(row=0,column=0,columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 50, "bold"))

def flip_card():
    canvas.itemconfig(card_title, text=keys[1], fill="white")
    canvas.itemconfig(card_word, text=current_card[keys[1]], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def next_card():
    global current_card, keys, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    keys = list(current_card.keys())
    # print(keys)
    canvas.itemconfig(card_title, text=keys[0], fill="black")
    canvas.itemconfig(card_word, text=current_card[keys[0]], fill="black")

    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)

def save_card():
    data.remove(current_card)
    new_df = pandas.DataFrame(data)
    # print(new_df)
    new_df.to_csv("data/world_to_learn.csv", index=False)
    next_card()




flip_timer = window.after(3000, func=flip_card)



#BUTTON
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0,command=save_card)
right_button.grid(row=1, column=1)







next_card()





















window.mainloop()
