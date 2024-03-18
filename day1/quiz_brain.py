class Quiz_brain:
    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False) : "
        ).lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, corr_ans):
        if user_ans.lower() == corr_ans.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}")
        else:
            print("It is wrong!")
            print(f"Your current score is {self.score}/{self.question_number}")
        print(f"The correct answer was {corr_ans.title()}\n")

    def final_score(self):
        print("You have completed the quiz!")
        print(f"Your final score is {self.score}/{len(self.question_list)}")
