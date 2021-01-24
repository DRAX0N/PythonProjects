from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.label = Label(text=f"Score {self.score}", fg="white")
        self.label.grid(row=0, column=1)
        self.label.config(bg=THEME_COLOR)

        # self.text_box = Text(width=30, height=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_box = self.canvas.create_text(150, 125, text="TEMP", fill=THEME_COLOR, font=FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # self.text_box.config()

        correct_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.correct = Button(padx=20, pady=20, image=correct_img, highlightthickness=0, command=self.check_if_true)
        self.correct.grid(row=2, column=0)
        self.false = Button(padx=20, pady=20, image=false_img, highlightthickness=0, command=self.check_if_false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_box, text=q_text)
        else:
            self.canvas.itemconfig(self.text_box, text="THE END")
            self.correct.config(state="disable")
            self.false.config(state="disable")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        # print(is_right)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)



