from tkinter import  *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx= 50, pady=50)

def calc_miles_in_km():
    miles = input.get()
    km = round(float(miles) * 1.609, 2)
    show_km = Label(text=km, padx=5, pady=5)
    show_km.grid(column=1, row=1)


input = Entry(width=10)
input.grid(column= 1, row=0)

miles_label = Label(text="Miles",padx=5, pady=5)
miles_label.grid(column= 2, row=0)

display_label = Label(text="is equal to", padx=5, pady=5)
display_label.grid(column=0, row=1)

km_label = Label(text="Km", padx=5, pady=5)
km_label.grid(column= 2, row=1)

button = Button(text="Calculate", command=calc_miles_in_km, padx=5, pady=5)
button.grid(column=1, row=2)











window.mainloop()