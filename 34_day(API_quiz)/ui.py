from  tkinter import *

THEME_COLOR = "#375362"
TRUE_IMAGE = "34_day(API_quiz)/images/true.png"
FALSE_IMAGE = "34_day(API_quiz)/images/false.png"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0 )
        self.q_text= self.canvas.create_text(150, 125, text="", font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.true_btn = Button(image=TRUE_IMAGE, highlightthickness=0, command=self.action_true)
        self.true_btn.grid(column=0, row=2)
        self.false_btn = Button(image=FALSE_IMAGE, highlightthickness=0, command=self.action_false)
        self.false_btn.grid(column=1, row=2)

        self.window.mainloop()

    def action_true(self):
        pass

    def action_false(self):
        pass