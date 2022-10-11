import user_inteface
import question_data
from question_model import Question
import html


def empty_func():
    pass


def on_command():
    true_button.command(command=true)
    false_button.command(command=false)
    next_button.command(command=empty_func)


def off_command():
    true_button.command(command=empty_func)
    false_button.command(command=empty_func)
    next_button.command(command=next_question)


def new_question():
    global question_bank

    question_data.new_request()

    for another_question in question_data.question_data["results"]:
        question_bank.append(Question(question=another_question["question"], answer=another_question["correct_answer"]))


def next_question():
    global question_number
    global question
    global answer

    on_command()

    question = html.unescape(question_bank[question_number].question)
    answer = question_bank[question_number].answer

    canvas.question_canvas.config(bg="white")
    canvas.update(question_text=question)

    question_number += 1

    if question_number % question_data.parameters["amount"] == 0:
        new_question()

    question_number_label.update(number=question_number)


def check_answer(user_answer):
    global score

    if user_answer == answer:
        canvas.correct()
        score += 1
        score_number_label.update(score)
    else:
        canvas.wrong()


def true():
    user_answer = "True"
    off_command()

    check_answer(user_answer=user_answer)


def false():
    user_answer = "False"
    off_command()

    check_answer(user_answer=user_answer)


question_bank = []

new_question()

question_number = 0
score = 0

question = ""
answer = ""

root = user_inteface.Root()
root.create()

question_number_label = user_inteface.QuestionNumberLabel()
question_number_label.create()

score_number_label = user_inteface.ScoreNumberLabel()
score_number_label.create()

canvas = user_inteface.QuestionCanvas()
canvas.create()

true_button = user_inteface.TrueButton()
true_button.create()
true_button.command(command=true)

false_button = user_inteface.FalseButton()
false_button.create()
false_button.command(command=false)

next_button = user_inteface.NextButton()
next_button.create()
next_button.command(command=next_question)

next_question()

root.exist()
