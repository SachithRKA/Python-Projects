import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    passw_entry.insert(0, password)
    pyperclip.copy(password)


def sent_To_File():
    website = website_entry.get()
    email = em_user_entry.get()
    password = passw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            passw_entry.delete(0, END)


def find_password():
    website_id = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)  # read the data
    except FileNotFoundError:
        messagebox.showerror(message="Data file not found")
    else:
        try:
            password = data[website_id].get("password")
            email = data[website_id].get("email")
        except:
            messagebox.showerror(message="No details for the website exists")
        else:
            messagebox.showinfo(title="Password", message=f"Your Email: {email} and Password: {password}")
            passw_entry.insert(0, password)
            em_user_entry.delete(0, END)
            em_user_entry.insert(0, email)


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

website_entry = Entry(font="Arial", width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

em_user_entry = Entry(font="Arial", width=30)
em_user_entry.grid(row=2, column=1)
# em_user_entry.grid(row=2, column=1, columnspan=2)
em_user_entry.insert(0, "sachithRKA@gmail.com")

passw_entry = Entry(font="Arial", width=30)
passw_entry.grid(row=3, column=1)

generateP = Button(text="Generate Password", font="Arial", command=generate_password, width=15)
generateP.grid(row=3, column=2)

search = Button(text="Search", font="Arial", command=find_password, width=15)
search.grid(row=1, column=2)

add = Button(text="Add", width=36, command=sent_To_File)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
