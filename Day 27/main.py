from tkinter import *

window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)


# my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()


# def button_clicked():
#     print("I got clicked")
#     my_label["text"] = entry.get()


# button = Button(text="Click Me", command=button_clicked)
# button.pack()


# entry = Entry(width=10)
# entry.pack()

# window.mainloop()


# Mile to Km converter

window.title("Mile to Km converter")
window.minsize(width=500, height=300)
window["padx"] = 175
window["pady"] = 120


def convert():
    result_label["text"] = f"{round(int(entry.get()) * 1.6)}"


entry = Entry(width=15)
entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equalto_label = Label(text="is equal to")
is_equalto_label.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
