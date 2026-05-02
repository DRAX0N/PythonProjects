from tkinter import *

def miles_to_km():
    miles = int(input.get())
    km = 1.6 * miles
    Result.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=500)
# Entry
input = Entry(width=10, text="0")
input.grid(column=1, row=0)
# Label
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is qual to")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

Result = Label(text="0")
Result.grid(column=1, row=1)
# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()