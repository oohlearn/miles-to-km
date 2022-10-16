from tkinter import *

window = Tk()
window.minsize(height=300, width=300)
window.config(padx=100, pady=100)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal .grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)


def button_clicked():
    word = input.get()
    convert = int(int(word) * 1.6)
    result.config(text=f"{convert}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

input = Entry(width=5)
input.grid(column=1, row=0)

window.mainloop()

