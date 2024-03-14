from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 10)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.speed("fastest")
        self.color("white")
        self.print_score()

    def print_score(self):
        self.write(f'Score : {self.score}', align=ALIGMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGMENT, font=FONT)




