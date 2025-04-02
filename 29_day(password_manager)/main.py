from tkinter import *
from tkinter import messagebox
import password_gen as pg
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password = pg.get_rand_password()
    save_to_clipboard(password)
    password_input.delete(0, END)
    password_input.insert(0, password)

def generator():
    pass

def save_to_clipboard(text):
    pyperclip.copy(text)
# ---------------------------- WORK WITH JSON FILE ------------------------------- #
def save_to_file(json_data):
    with open("data.json", "w") as file:
        json.dump(json_data, file, indent=4)

def load_from_file():
    try:
        with open("data.json", "r") as file:
            loaded_data = json.load(file)
    except FileNotFoundError as e:
        return {}
    else: return loaded_data

def update_file(json_data):
    loaded_data = load_from_file()
    loaded_data.update(json_data)
    save_to_file(loaded_data)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_btn_actions():
    email = email_input.get()
    password = password_input.get()
    website = website_input.get()
    data = {
        website: {
            "password": password,
            "email" : email,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(message="Fields shouldn't be empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n \nEmail: {email} \nWebsite: {website} \nPassword: {password}\n \nIs it OK to save?")

        if is_ok:
            update_file(data)
            password_input.delete(0, END)
            website_input.delete(0, END)
            website_input.focus()
# ---------------------------- SEARCH ------------------------------- #
def search_btn_action():
    website = website_input.get()
    credentials = search(website)
    if credentials != None:
        messagebox.showinfo(message=f"Email: {credentials["email"]}  \nPassword: {credentials["password"]}\n")
    else:
        messagebox.showinfo(message="There is no data")

def search(website):
    data = load_from_file()
    try:
        result = data.get(website)
    except AttributeError:
        return None
    else:
        return result

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx= 50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=54)
email_input.insert(0, string="email@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=35)
password_input.grid(column=1, row=3 )

password_gen_btn = Button(text="Generate Password", command=password_gen)
password_gen_btn.grid(column=2, row=3)
add_btn = Button(text="Add", command=add_btn_actions, width=46)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn = Button(text="Search", command=search_btn_action, width=15)
search_btn.grid(column=2, row=1)


window.mainloop()