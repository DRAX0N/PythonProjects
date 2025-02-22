from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    pass_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_text = web_entry.get()
    user_text = user_entry.get()
    pass_text = pass_entry.get()
    save_text = f"{web_text}|{user_text}|{pass_text}\n"
    new_date = {
        web_text:
            {
                "email": user_text,
                "password": pass_text,
            }
    }
    msg_box = False
    if len(web_text) != 0 and len(pass_text) != 0:
        msg_box = messagebox.askokcancel(title=web_text, message=f"This are the entered details: \nEmail: {user_text}"
                                     f"\nPassword: {pass_text}\nIs it ok to save?")
    else:
        first_box = messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    if msg_box == True:
        try:
            with open("data.json", mode="r") as data:
                data_s = json.load(data)
        except FileNotFoundError:
            with open("data.json", mode="w") as data:
                json.dump(new_date, data, indent=4)
        else:
            data_s.update(new_date)
            with open("data.json", mode="w") as data:
                json.dump(data_s, data, indent=4)
        finally:
            # data.write(save_text)
            web_entry.delete(first=0, last=END)
            #user_entry.delete(first=0, last=100)
            pass_entry.delete(first=0, last=END)

def find_password():
    web_text = web_entry.get()
    try:
        with open("data.json", mode="r") as data:
            data_s = json.load(data)
    except:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
            # web_list = []
            if web_text in data_s.keys():
                user_text = data_s[web_text]["email"]
                pass_text = data_s[web_text]["password"]
                messagebox.showinfo(title=f"{web_text}", message=f"User: {user_text}\nPassword: {pass_text}")
            else:
                messagebox.showinfo(title="Error", message=f"No details fort the {web_text} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
pass_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_image)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entries
web_entry = Entry(bg="white", width=32)
web_entry.grid(row=1, column=1)
web_entry.focus()
user_entry = Entry(bg="white", width=50)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "xxx@gmail.com")
pass_entry = Entry(bg="white", width=32)
pass_entry.grid(row=3, column=1)

#Buttons
gen_button = Button(text="Generate Password", width=14, command=generate_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
