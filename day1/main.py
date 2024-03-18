from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain


question_bank = []
for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = Quiz_brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_score()
