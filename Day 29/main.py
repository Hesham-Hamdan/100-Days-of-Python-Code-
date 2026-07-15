from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def generate_password():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)]
        + [random.choice(symbols) for _ in range(nr_symbols)]
        + [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)

    final_password = "".join(password_list)
    pyperclip.copy(final_password)

    password.delete(0, END)
    password.insert(0, final_password)


# print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    site = website.get()
    email = email_username.get()
    pasrd = password.get()

    if site == "" or pasrd == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the detail entered: \nEmail: {email}\nPassword: {pasrd}\n Is it ok to save?",
        )
        if is_ok:
            with open("Day 29/passwords.txt", mode="a") as file:
                file.write(f"{site} | {email} | {pasrd}\n")
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manger")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(
    file="Day 29/logo.png",
)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)


email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website = Entry(width=35)
website.grid(row=1, column=1, columnspan=2)
website.focus()

email_username = Entry(width=35)
email_username.grid(row=2, column=1, columnspan=2)
email_username.insert(0, "Hello@gmail.com")

password = Entry(width=21)
password.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2)

add = Button(width=36, text="Add", command=save_password)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
