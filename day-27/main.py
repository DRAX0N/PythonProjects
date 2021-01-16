from tkinter import *

def on_click():
    text = input.get()
    # my_label["text"]="Clicked"
    # my_label.config(text="Clicked")
    my_label.config(text=text)

window = Tk()
window.title("First program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label
my_label = Label(text="I am a label", font=("Arial", 24,"bold"))
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click me", command=on_click)
button.grid(column=1, row=1)

button1 = Button(text="Click me 2", command=on_click)
button1.grid(column=2, row=0)
#Entry

input = Entry(width=10)
text = input.get()
input.grid(column=3, row=3)

#pack
# button.pack()
# my_label.pack()
# input.pack()
window.mainloop()
