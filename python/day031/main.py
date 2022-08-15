from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


# Flip the card
def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(title, text="English", fill="white")


# Generate random card
def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, flip_card)


# Save words if learned
def is_known():
    words.remove(current_card)
    df = pandas.DataFrame(words)
    df.to_csv("data/words_to_learn.csv", index=False)
    random_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer
flip_timer = window.after(3000, flip_card)

# Cards canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 253, text="trouve", font=("Ariel", 80, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
tick = PhotoImage(file="images/right.png")
cross = PhotoImage(file="images/wrong.png")
yes_button = Button(image=tick, highlightthickness=0, command=is_known)
no_button = Button(image=cross, highlightthickness=0, command=random_card)
yes_button.grid(row=1, column=1)
no_button.grid(row=1, column=0)

random_card()
window.mainloop()
