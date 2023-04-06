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
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_command(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def false_command(self):
        self.quiz.check_answer("False")
        self.get_next_question()