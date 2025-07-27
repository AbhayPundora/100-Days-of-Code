from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text="i am a label", font=("Arial", 24, "bold"), padx=10, pady=10)
my_label.grid(column=0, row=0)

def handle_click():
    my_label.config(text=input.get())


button = Button(text="Click me", command= handle_click, padx=10, pady=10)
button.grid(column=1, row=1)

button2 = Button(text="Click me", command= handle_click, padx=10, pady=10)
button2.grid(column=2, row=0)


#Entry

input = Entry(width=10)
input.grid(column=3, row=2)
















window.mainloop()