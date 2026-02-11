import pwd
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #  creating random password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(letters) for _ in range(randint(2, 4))]
    symbols_list = [choice(letters) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list

    # deleting anything inside password

    password.delete(0, END)

    # populating password entry

    new_password = "".join(password_list)
    password.insert(0, new_password)
    print(f"Your password is: {password.get()}")
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    if len(website.get())==0 or len(password.get())==0:
        messagebox.showinfo(title="Oops", message="Please enter website and password.")
    else:
        is_ok = messagebox.askokcancel(title= website.get(), message= f"These are the details enterend :\n"
                                                                      f"website: {website.get()}\n"
                                                                      f"password: {password.get()}\n")
        if is_ok:
            with open('Data.txt', mode='a') as file:
                file.write(f"{website.get()} | f{email.get()} | {password.get()}\n")
                website.delete(0, END)
                password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200 )
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

#Entry
website = website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email = email_entry = Entry(width=35)
email_entry.insert(0, "abuhurayrafarhan@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password = password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Password", width=11, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=33, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2)





window.mainloop()