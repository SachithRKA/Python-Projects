from tkinter import *

window = Tk()

window.title("Mile to Km Conterver")
window.minsize(width=500, height=300)

input = Entry(width=10)
input.grid(column=2, row= 0)

miles = Label(text="Miles ", font=("Arial", 24, "bold"))
miles.grid(column=0, row= 1)

middle_m = Label(text="is equal to ", font=("Arial", 24, "bold"))
middle_m.grid(column=0, row= 1)

km_label = Label(text="0", font=("Arial", 24, "bold"))
km_label.grid(column=1, row= 1)

km_unit = Label(text="KM", font=("Arial", 24, "bold"))
km_unit.grid(column=2, row= 1)

def milesToKm():
    km = float(input.get())
    km =  km * 1.609347
    km_label.config(text=km)

button = Button(text="Calculate", command=milesToKm)
button.grid(column=2, row= 3)


window.mainloop()
