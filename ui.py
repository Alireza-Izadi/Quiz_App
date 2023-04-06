from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT =("Arial", 20, "italic")
#-------------------------UI--------------------------#
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: 0",
            bg= THEME_COLOR,
            fg="white",
            font=("Arial", 10, "bold")
            )
        self.score_label.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Here Goes Your Question",
            fill=THEME_COLOR,
            font=FONT
            )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_img, command=self.true_command)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_img, command=self.false_command)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have answered all the questions and your score is: {self.quiz.score}/50")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def true_command(self):
        answer = self.quiz.check_answer("True")
        self.give_feedback(answer)
        self.add_score()

    def false_command(self):
        answer = self.quiz.check_answer("False")
        self.give_feedback(answer)
        self.add_score()

    def give_feedback(self, answer):
        if answer == True:
            self.canvas.configure(bg="green")  
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
            
    def add_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")        
        
#=======================================================================#