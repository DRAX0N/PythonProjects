from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.stil_has_questions():
    quiz.next_question()

print("You completed quiz!!!")
print(f"Your score is {quiz.score}/{quiz.question_number}")