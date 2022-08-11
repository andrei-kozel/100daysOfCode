from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

window.columnconfigure(0, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(2, weight=1)

mile_text = Label(text="Miles")
mile_text.grid(row=0, column=2)

km_text = Label(text="Km")
km_text.grid(row=1, column=2)

equal_text = Label(text="is equal to")
equal_text.grid(row=1, column=0)

value_text = Label(text="0")
value_text.grid(row=1, column=1)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)


def calculate():
    entry_miles = int(entry.get())
    km = entry_miles * 1.60934
    value_text.config(text=km)


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
