import time
from tabnanny import check
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label["text"] = "Timer"
    label2["text"] = ''
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="BREAK", fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="WORK", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    mins = math.floor(count/60)
    secs = count % 60
    if secs < 10:
        secs= f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += CHECK_MARK
            label2.config(text=marks)
        reset()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(pady=50, padx= 100, bg=YELLOW)


#image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=False)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# start button
start_btn = Button(text="Start", command=start)
start_btn.grid(column=0, row=2)

# button2
reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=2)

# Timer label
label = Label(text="Timer", font=("Courier", 35 , "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

# checkmark label
label2 = Label(font=(10), fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

window.mainloop()



