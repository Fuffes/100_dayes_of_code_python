from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question_bank.append(Question(text=item["question"], answer=item["correct_answer"]))


quiz = QuizBrain(questions=question_bank)
while quiz.sill_got_questions():
    quiz.next_question()

print('You have completed the quiz')
print(f"Your final score: {quiz.score}/{len(question_bank)}")

