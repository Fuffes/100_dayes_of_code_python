from tkinter import *
import pandas as pd
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"
file = "words.csv"
to_learn_file = "to_learn.csv"
current_card = {}
to_learn = {}

# ------------------------------- WORK WITH DATA -------------------------------
try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------------------------------- ACTIONS -------------------------------
def flip_card():
    canvas.itemconfig(canvas_img, image=back_card_img)
    canvas.itemconfig(lang_text, text="Russian", fill="white")
    canvas.itemconfig(word_text, text=current_card["Ru"], fill="white")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_img, image=front_card_img)
    canvas.itemconfig(lang_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["En"], fill="black")
    flip_timer = window.after(3000, flip_card)

def remove_card():
    global current_card, to_learn
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()



# ------------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Flash card app")
window.config(pady=50, padx= 50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0 )
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_card_img )
lang_text= canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text= canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_btn_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_image, highlightthickness=0, command=remove_card)
right_btn.grid(column=1, row=1)

wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

next_card()

window.mainloop()
