# Created by fame
# MAE + FA
# Weekly Game Jam 201


import random
import tkinter as tk

# Constants
HEIGHT = 300
WIDTH = 550
Title = "Welcome to Clones W202"

# Make Windows 10 High DPI Aware
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(True)
except ImportError:
    pass

# Window
top = tk.Tk()
top.title(Title)
top.resizable(width=False, height=False)
top.geometry(str(WIDTH) + 'x' + str(HEIGHT))
# top.iconphoto(False, tk.PhotoImage(file='quizz.png'))

questions = []
answers = []
solutions = []
complete = []
refresh_questions = True


def get_quizz_components():
    count = 0
    with open('questions.ini', 'r') as file:
        line = file.readline()
        while line:
            if count == 0:
                questions.append(line)
                complete.append(line)
                count += 1
                line = file.readline()
            elif count == 5:
                solutions.append(line)
                complete.append(line)
                count = 0
                line = file.readline()
            else:
                answers.append(line)
                complete.append(line)
                count += 1
                line = file.readline()
    #print("Number of questions " + str(len(questions)))

    question_picked = random.choice(questions)

    indexposition = complete.index(question_picked)

    answers_picked = complete[indexposition + 1:indexposition + 5]
    solution_picked = answers[questions.index(question_picked)]

    return question_picked, answers_picked, solution_picked


def checkanswers(sentanswer, correctsolution, points):
    if sentanswer[0] == correctsolution[0]:
        #print("Correnct Answer")
        points += 1
        current_questions, current_answers, current_solutions = get_quizz_components()
        buildgui(current_questions, current_answers, current_solutions, points)
        if points >= 10:
            pass
            #print('You won')

    else:
        points -= 1
        #print("wrong answer")
        if points <= -10:
            pass
            #print('you lost')


def buildgui(now_questions, now_answers, now_solutions, points):
    for child in top.winfo_children():
        child.destroy()

    GameQuestion = tk.Label(top, text=now_questions)
    GameQuestion.grid(column=0, row=1)

    Answer1 = tk.Button(top, text=now_answers[0], command=lambda: checkanswers(now_answers[0], now_solutions, points))
    Answer1.grid(column=0, row=2)

    Answer2 = tk.Button(top, text=now_answers[1], command=lambda: checkanswers(now_answers[1], now_solutions, points))
    Answer2.grid(column=0, row=3)

    Answer3 = tk.Button(top, text=now_answers[2], command=lambda: checkanswers(now_answers[2], now_solutions, points))
    Answer3.grid(column=1, row=2)

    Answer4 = tk.Button(top, text=now_answers[3], command=lambda: checkanswers(now_answers[3], now_solutions, points))
    Answer4.grid(column=1, row=3)


def main():
    points = 0
    GameTitle = tk.Label(top, text=Title)
    GameTitle.grid(column=0, row=0)

    PointsDisplayer = tk.Label(top, text="Current score: " + str(points))
    PointsDisplayer.grid(column=0, row=4)

    current_questions, current_answers, current_solutions = get_quizz_components()
    buildgui(current_questions, current_answers, current_solutions, points)
    top.mainloop()


if __name__ == "__main__":
    main()
