from tkinter import *

window = Tk()

window.title("Mile to Km Conterver")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row= 0)

def button_clicked():
  my_label.config(text=input.get())

input = Entry(width=10)
input.grid(column=3, row= 3)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row= 1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=3, row= 1)

window.mainloop()
