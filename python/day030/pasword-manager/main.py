from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate():
    if len(website_entry.get()) > 0 and len(emu_entry.get()) > 0 and len(password_entry.get()):
        return True
    else:
        messagebox.showinfo(title="Error", message="You left some fields empty!")
        return False


def save_password():
    if validate():
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"There are the details entered: \n"
                                                                          f"Email: {emu_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"Is it ok to save?")
        new_data = {website_entry.get(): {
            "email": emu_entry.get(),
            "password": password_entry.get()
        }}

        if is_ok and validate:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            else:
                data.update(new_data)

                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_password():
    site_to_search = website_entry.get()

    if len(site_to_search) == 0:
        messagebox.showinfo(title="Error", message="You have to type website name")

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            credentials = data[site_to_search]
            print(credentials)
            messagebox.showinfo(title="Success", message=f"Email: {credentials['email']}\n"
                                                         f"Password: {credentials['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    except KeyError as error:
        messagebox.showinfo(title="Error", message=f"Password for {error} doesn't exist")


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
website_entry.grid(column=1, row=1, sticky='we')
search_button = Button(text="Search", command=search_password)
search_button.grid(column=2, row=1, sticky='we')

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
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)
generate_password()

# Add password row
add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, columnspan=2, row=4, sticky='we')

window.mainloop()
