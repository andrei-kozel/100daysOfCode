import os
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("passwords.txt", "a") as file:
        file.write(f"{website_entry.get()} | {emu_entry.get()} | {password_entry.get()}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# Logo image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website row
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1, sticky='we')

# Email/Username row
emu_text = Label(text="Email/Username:")
emu_text.grid(column=0, row=2)
emu_entry = Entry()
emu_entry.insert(0, "email@example.com")
emu_entry.grid(column=1, columnspan=2, row=2, sticky='we')

# Password row
password_text = Label(text="Password:")
password_text.grid(column=0, row=3)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='we')
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

# Add password row
add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, columnspan=2, row=4, sticky='we')

window.mainloop()
