import sys
from tkinter import *
import os
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.geometry("500x600+500+100")
        self.window.title("Quizzy")
        self.window.config(bg="gray", padx=50, pady=30)

        self.score_label = Label(text=f"{self.quiz.score}/15", bg="gray", fg="white", font=("calibre", 20, "bold"))
        self.score_label.grid(column=0, row=0, sticky="n")

        self.canvas = Canvas(height=400, width=400, bg=THEME_COLOR, highlightthickness=0)
        self.question = self.canvas.create_text(200, 200, text="yjcj", width=380, fill="white",
                                                font=("Arial", 14, "italic"))
        self.canvas.grid(column=0, row=1, pady=10)

        right = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right, borderwidth=0, highlightthickness=0, command=self.is_true)
        self.right_button.grid(column=0, row=2, sticky="w")

        wrong = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong, borderwidth=0, highlightthickness=0, command=self.is_false)
        self.wrong_button.grid(column=0, row=2, sticky="e")

        self.change_question()

        self.window.mainloop()

    def change_question(self):
        self.canvas.config(bg=THEME_COLOR)
        if not self.quiz.still_has_questions():
            self.end()
        self.canvas.itemconfig(self.question, text=self.quiz.next_question())

    def is_true(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"{self.quiz.score}/15")
        self.window.after(2000, self.change_question)

    def is_false(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.score_label.config(text=f"{self.quiz.score}/15")
        self.window.after(2000, self.change_question)

    def end(self):
        messagebox.showinfo(title="Thanks for staying with us!", message=f"You got {self.quiz.score}/15 in the quiz.")
        exit()
