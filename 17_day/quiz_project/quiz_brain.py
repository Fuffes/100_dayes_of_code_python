class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def next_question(self):
        currentQuestion = self.questions_list[self.question_number]
        self.question_number += 1
        chose = input(f"Q.{self.question_number}: {currentQuestion.text}")
        self.check_answer(chose, currentQuestion.answer)

    def sill_got_questions(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, chose, answer):
        if answer.lower() == chose.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!(")
        print(f"The correct answer was {answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

