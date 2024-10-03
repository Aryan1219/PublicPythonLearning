from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz : QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        #Label
        self.score_label = Label(text=f'Score: {0}',bg=THEME_COLOR)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width=300,height=250,bg = 'white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text = '',
            fill = THEME_COLOR,
            font= ('Arial',20,'italic'),
            width = 280)
        self.canvas.grid(row=1,column = 0,columnspan = 2,pady = 40)

        #Buttons
        right_image = PhotoImage(file = "images/true.png")
        self.is_true_button = Button(image=right_image,highlightthickness=0,command = self.true_pressed)
        self.is_true_button.grid(row=2,column =0)

        left_image = PhotoImage(file = "images/false.png")
        self.is_false_button = Button(image=left_image,highlightthickness=0,command= self.false_pressed)
        self.is_false_button.grid(row=2,column =1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = 'You have reached the end of the quiz.')
            self.is_true_button.config(state='disabled')
            self.is_false_button.config(state='disabled')



    def true_pressed(self):
        response = self.quiz.check_answer('True')
        if response != False:
            self.score_label.config(text=f'Score: {response}')
            self.feedback(True)
            self.canvas.after(1000, self.get_next_question)
        else:
            self.feedback(False)
            self.canvas.after(1000, self.get_next_question)

    def false_pressed(self):
        response = self.quiz.check_answer('False')
        if response != False:
            self.score_label.config(text=f'Score: {response}')
            self.feedback(True)
            self.canvas.after(1000, self.get_next_question)
        else:
            self.feedback(False)
            self.canvas.after(1000, self.get_next_question)

    def feedback(self,is_correct:bool):
        if is_correct:
            self.canvas.config(bg='green')
            self.canvas.after(1000, self.turn_white)
        else:
            self.canvas.config(bg='red')
            self.canvas.after(1000, self.turn_white)

    def turn_white(self):
        self.canvas.config(bg='white')









