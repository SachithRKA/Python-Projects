from tkinter import *
from tkinter import messagebox
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []
password_list = [random.choice(letters) for char in range(nr_letters)]
password_list += [random.choice(symbols) for char in range(nr_symbols)]
password_list += [random.choice(numbers) for char in range(nr_numbers)]

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

def generate_password():
    passw_entry.insert(0, password)

def sent_To_File():
    website_input = website_entry.get()
    em_user_input = em_user_entry.get()
    passw_input = passw_entry.get()
    isok = False

    if website_input == em_user_input and passw_input == em_user_input:
        messagebox.showerror(title="Error", message="Password is invalid")
    elif len(website_input) == 0 or len(em_user_input) == 0 or len(passw_input) == 0:
        messagebox.showinfo(title="Error", message="Fields are empty.")
    else:
        isok = messagebox.askokcancel(title=website,
                                      message=f"Are you sure: \nEmail: {em_user_input}\nPassword: {passw_input} \n Is it ok to save?")

    if isok:
        with open("data.txt", mode="a") as file:
            file.write(f"\n Website Name= {website_input} Email= {em_user_input} Password = {passw_input}")

    website_entry.delete(0, END)
    passw_entry.delete(0, END)

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
em_user_entry.insert(0,"sachithRKA@gmail.com")

passw_entry = Entry(font="Arial", width=21)
passw_entry.grid(row=3, column=1)

generateP = Button(text="Generate Password", font="Arial", command=generate_password)
generateP.grid(row=3, column=2)

add= Button(text="Add", width=36, command=sent_To_File)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
