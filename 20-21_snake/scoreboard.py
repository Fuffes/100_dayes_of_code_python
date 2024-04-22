from turtle import Turtle
ALIGMENT = 'center'
FONT = ('Arial', 10)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.high_score = self.get_high_score()
        self.goto(0, 280)
        self.speed("fastest")
        self.color("white")
        self.print_score()

    def get_high_score(self):
        with open("high_score.txt", mode="r") as f:
            return int(f.read())

    def print_score(self):
        self.clear()
        self.write(f'Score : {self.score}, High score: {self.high_score}', align=ALIGMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.print_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f'GAME OVER', align=ALIGMENT, font=FONT)

    def reset_game(self):
        if (self.score > self.high_score):
            with open("high_score.txt", mode="w+") as file:
                file.write(f"{self.score}")


        self.score = 0
        self.print_score()

