from tkinter import *
import pandas
import random


def create_dictionary(path):
    with open(path) as data:
        new_json = pandas.read_csv(data)
        new_json = new_json.to_dict()
        return new_json


def flip_card_back():
    canvas.create_image(500, 350, image=card_back)
    # header.config(text=lan_list[1])
    key = [n for n in dictionary[lan_list[0]] if dictionary[lan_list[0]][n] == word]
    # sentence.config()
def flip_card_front():
    canvas.create_image(500, 350, image=card_back)
    # header.config(text=lan_list[1])
    key = [n for n in dictionary[lan_list[0]] if dictionary[lan_list[0]][n] == word]

FONT = "Courier"
path = "French to English.csv"
timer = None
time = 3000
# UI
window = Tk()
window.title("Language Card")
window.config(padx=50, pady=50)
canvas = Canvas(width=1000, height=775, highlightthickness=0)
card_front = PhotoImage(file="card_1.png")
card_back = PhotoImage(file="card_2.png")
canvas.create_image(500, 350, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Accept
image_check = PhotoImage(file="Checklist-Logo.png")
image_check = image_check.subsample(4, 4)
check_button = Button(width=250, height=250, image=image_check, highlightthickness=0)
check_button.grid(column=0, row=1)
# Decline
image_decline = PhotoImage(file="Decline.png")
image_decline = image_decline.subsample(4, 4)
decline_button = Button(width=250, height=250,  image=image_decline, highlightthickness=0)
decline_button.grid(column=1, row=1)

#Label
dictionary = create_dictionary(path)
lan_list = list(dictionary.keys())
first_lan = Label(text=lan_list[0])
second_lan = Label(text=lan_list[1])
header = canvas.create_text(500, 250, text=lan_list[0], font=(FONT, 35, "bold"))

word = random.choice(dictionary[lan_list[0]])
sentence = canvas.create_text(500, 350, text=word, font=(FONT, 45, "bold"))
window.after(time, flip_card)

# print(lan_list[0])


window.mainloop()
