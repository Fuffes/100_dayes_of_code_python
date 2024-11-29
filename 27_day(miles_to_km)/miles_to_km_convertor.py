from tkinter import Label, Tk, Button, Entry, END


def convert():
    miles = float(field.get())
    km = miles*1.609
    result_label.config(text=f"{km}")


# Window setup
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=10)

# Labels
is_equal_to_label = Label(text="is equal to")
result_label = Label(text="0")
miles_label = Label(text="Miles")
km_label = Label(text="Km")

# button
button = Button(text="Calculate", command=convert)

# input
field = Entry()
field.insert(END, string="0")
field.config(width=10)


# positioning
is_equal_to_label.grid(column=0,row=1)
field.grid(column=1, row=0)
result_label.grid(column=1, row=1)
button.grid(column=1, row=2)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)



window.mainloop()






