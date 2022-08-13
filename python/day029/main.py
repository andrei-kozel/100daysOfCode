from tkinter import *

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

window.columnconfigure(0, weight=1)
window.columnconfigure(3, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(5, weight=1)

# Logo image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website row
website_text = Label(text="Website:", font=(FONT_NAME, 14))
website_text.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)

# Email/Username row
emu_text = Label(text="Email/Username:", font=(FONT_NAME, 14))
emu_text.grid(column=0, row=2)
emu_entry = Entry(width=35)
emu_entry.grid(column=1, columnspan=2, row=2)

# Password row
password_text = Label(text="Password:", font=(FONT_NAME, 14))
password_text.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3)

# Add password row
add_button = Button(text="Add", width=30)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
