from  tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


TRUE_IMAGE = "images/true.png"
FALSE_IMAGE = "images/false.png"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0 )
        self.q_text= self.canvas.create_text(150, 125, text="text", fill=THEME_COLOR, width=290, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file=TRUE_IMAGE)
        self.true_btn = Button(image=true_img,  highlightthickness=0, command=self.action_true)
        self.true_btn.grid(column=0, row=2)
        false_img = PhotoImage(file=FALSE_IMAGE)
        self.false_btn = Button(image=false_img,  highlightthickness=0, command=self.action_false)
        self.false_btn.grid(column=1, row=2)

        self.score_text = Label(text= f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)
        self.get_q()

        self.window.mainloop()

    def get_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text= f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state= "disabled")


    def action_true(self):
        check_result = self.quiz.check_answer("true")
        self.feedback(check_result)
        self.window.after(1000, self.get_q)


    def action_false(self):
       check_result = self.quiz.check_answer("false")
       self.feedback(check_result)
       self.window.after(1000, self.get_q)


    def feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")