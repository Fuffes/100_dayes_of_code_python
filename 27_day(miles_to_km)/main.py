from tkinter import *



window = Tk()

# window setting
window.title("GUI")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)

# components
def clicked():
    print("Clicked")
    entered_value = input.get()
    label.config(text=entered_value)


# label
label = Label(text="Label", font=("Arial", 20 , "bold"))
label['text'] = "New text"
label.grid(column=0, row=0)

# button
button = Button(text="Click", command=clicked)
button.grid(column=1, row=1)

# button2
button2 = Button(text="Click", command=clicked)
button2.grid(column=2, row=0)

# entry
input = Entry(width=10)
input.grid(column=4, row=2)


window.mainloop()