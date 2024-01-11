from tkinter import *

def sentToFile():
    with open("data.txt", mode="w") as file:






window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="Website: ", font="Arial")
website.grid(row=1, column=0)

em_user = Label(text="Email/Username: ", font="Arial")
em_user.grid(row=2, column=0)

passw = Label(text="Password: ", font="Arial")
passw.grid(row=3, column=0)

website_entry = Entry(font="Arial", width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

em_user_entry = Entry(font="Arial", width=35)
em_user_entry.grid(row=2, column=1, columnspan=2)
em_user_entry.insert(0, "sachithRKA@gmail.com")
passw_entry = Entry(font="Arial", width=21)
passw_entry.grid(row=3, column=1)

generateP = Button(text="Generate Password", font="Arial")
generateP.grid(row=3, column=2)

add= Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
