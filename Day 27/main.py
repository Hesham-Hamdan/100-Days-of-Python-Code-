from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    print("I got clicked")
    my_label["text"] = entry.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()


entry = Entry(width=10)
entry.pack()

window.mainloop()
