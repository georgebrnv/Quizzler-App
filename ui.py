from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Question", fill=THEME_COLOR,
                                                  font=("Arial", 20, "italic"), width=280)
        # True button
        true_button_png = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_png, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)
        # False button
        false_button_png = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_png, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        # Label
        self.score_text = Label(text="Score: ", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz! "
                                                            f"Your score is {self.quiz.score}!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)