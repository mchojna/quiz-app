import tkinter as tk


class Root:
    def __init__(self):
        self.root = tk.Tk()

    def create(self):
        self.root.minsize(width=400, height=540)
        self.root.config(bg="#53565B")
        self.root.title("Quiz App")

    def exist(self):
        self.root.mainloop()


class QuestionNumberLabel:
    def __init__(self):
        self.question_number_label = tk.Label()

    def create(self):
        self.question_number_label.config(text=f"Question: 0", font=("Arial", 18, "bold"), fg="white", bg="#53565B")
        self.question_number_label.place(x=50, y=22.5)

    def update(self, number):
        self.question_number_label.config(text=f"Question: {number}", font=("Arial", 18, "bold"), fg="white", bg="#53565B")


class ScoreNumberLabel:
    def __init__(self):
        self.score_number_label = tk.Label()

    def create(self):
        self.score_number_label.config(text=f"Score: 0", font=("Arial", 18, "bold"), fg="white", bg="#53565B")
        self.score_number_label.place(x=240, y=22.5)

    def update(self, number):
        self.score_number_label.config(text=f"Score: {number}", font=("Arial", 18, "bold"), fg="white", bg="#53565B")


class QuestionCanvas:
    def __init__(self):
        self.question_text = None
        self.question_canvas = tk.Canvas()

    def create(self):
        self.question_canvas.config(width=350, height=350, bg="white", highlightthickness=0)
        self.question_canvas.place(x=25, y=75)
        self.question_text = self.question_canvas.create_text(175, 175, text="", font=("Ariel", 24, "italic"), fill="#53565B", justify="left", width=300)

    def update(self, question_text=None):
        self.question_canvas.config(bg="white")
        self.question_canvas.itemconfig(self.question_text, text=question_text)

    def correct(self):
        self.question_canvas.config(bg="green")

    def wrong(self):
        self.question_canvas.config(bg="red")


class TrueButton:
    def __init__(self):
        self.true_image = tk.PhotoImage(file="images/true_img.png")
        self.true_button = tk.Button()

    def create(self):
        self.true_button.config(image=self.true_image, bd=0, highlightthickness=0, height=45, width=45)
        self.true_button.place(x=74.5, y=460)

    def command(self, command):
        self.true_button.config(command=command)


class FalseButton:
    def __init__(self):
        self.false_image = tk.PhotoImage(file="images/false_img.png")
        self.false_button = tk.Button()

    def create(self):
        self.false_button.config(image=self.false_image, bd=0, highlightthickness=0, height=45, width=45)
        self.false_button.place(x=174.5, y=460)

    def command(self, command):
        self.false_button.config(command=command)


class NextButton:
    def __init__(self):
        self.next_image = tk.PhotoImage(file="images/next_img.png")
        self.next_button = tk.Button()

    def create(self):
        self.next_button = tk.Button(image=self.next_image, bd=0, highlightthickness=0, height=45, width=45)
        self.next_button.place(x=274.5, y=460)

    def command(self, command):
        self.next_button.config(command=command)