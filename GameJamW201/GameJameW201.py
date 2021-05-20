# Created by fame
# MAE + FA
# Weekly Game Jam
#
# Github
#

import tkinter as tk
import random
from tkinter import messagebox


# Constants
HEIGHT = 600
WIDTH = 600
Title = "Welcome to Bad Connection W201"
colors = ['blue', 'green', 'red', 'yellow', 'white']
left_options = ["a", "b", "c", "d", "e"]
right_options = ["1", "2", "3", "4", "5"]
time = 60
MarkerRadius = 20

# Game Logic Variables
left_color_list = []
right_color_list = []
left_selection = None
right_selection = None
left_circle = []
right_circle = []

# Window
top = tk.Tk()
top.title("Bad Connection")
top.resizable(width=False, height=False)
top.geometry(str(WIDTH) + 'x' + str(HEIGHT))
top.iconphoto(False, tk.PhotoImage(file='badco.png'))

surface = tk.Canvas(top, bg="grey", height=HEIGHT, width=WIDTH)

text = surface.create_text(WIDTH / 2, 50, text="Game Jam 201 Bad Connection", font=('Helvetica', '20', 'bold'))
timer = surface.create_text(HEIGHT / 2, WIDTH / 2, text="Timer goes here", font=('Helvetica', '16'))
left_selection_shower = surface.create_text(100, HEIGHT - 20, text="Left Selection goes here", font=('Helvetica', '10'))
right_selection_shower = surface.create_text(WIDTH - 100, HEIGHT - 20, text="Right Selection goes here",
                                             font=('Helvetica', '10'))


def tick():
    global time
    time -= 1

    surface.itemconfigure(timer, text=time)
    # print(time)
    if time == 0:
        messagebox.showerror("oooohhhh", "Time over : You loose the game")
        top.quit()
    else:
        surface.after(1000, tick)


def key(event):

    for x in range(0, 5):
        if event.char == left_options[x]:
            global left_selection
            left_selection = left_color_list[x]
            surface.itemconfigure(left_selection_shower, text=left_options[x])

    for r in range(0, 5):
        if event.char == right_options[r]:
            global right_selection
            right_selection = right_color_list[r]
            surface.itemconfigure(right_selection_shower, text=right_options[r])

    if left_selection is not None and right_selection is not None:

        if left_selection == right_selection:

            correct_circles = list(set(surface.find_withtag("circle")) & set(surface.find_withtag(left_selection)))

            for correct in correct_circles:
                create_highlight_circle(find_center(correct), left_selection)
                #surface.create_line(100, 100 * index, WIDTH - 100, 100 * i, width=5, fill=left_selection)

            if left_selection in colors:
                colors.remove(left_selection)

                if not colors:
                    messagebox.showinfo("YEAH", "You won the game")
                    top.quit()


def get_next_left_letter(t):
    picked_letter = left_options[t]
    return picked_letter


def get_left_random_color():
    picked_color = random.choice(colors)
    global left_color_list
    left_color_list.append(picked_color)
    colors.remove(picked_color)
    return picked_color


def get_right_random_color():
    picked_color = random.choice(colors)
    global right_color_list
    right_color_list.append(picked_color)
    colors.remove(picked_color)
    return picked_color


def click_object(event):
    print('Got object click', event.x, event.y, event.widget)
    print(event.widget.find_closest(event.x, event.y))


def clicked_on_draw_surface(event):
    print("clicked at", event.x, event.y)


def find_center(id):
    pos = surface.coords(id)
    yrel = (pos[2]-pos[0])/2
    xrel = (pos[3]-pos[1])/2

    yabs = yrel + pos[1]
    xabs = xrel + pos[0]

    return xabs, yabs


def create_highlight_circle(pos, color):
    x = pos[0]
    y = pos[1]

    x0 = x - MarkerRadius
    y0 = y - MarkerRadius
    x1 = x + MarkerRadius
    y1 = y + MarkerRadius

    surface.create_oval(x0, y0, x1, y1, outline="black", width=MarkerRadius)


def create_circle_in_color(x, y, r, color, side):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return surface.create_oval(x0, y0, x1, y1, fill=color, outline="black", width=4, tags=(color, "circle", side))


for i in range(1, 6):
    temp_color = get_left_random_color()
    create_circle_in_color(100, 100 * i, 20, temp_color, "left")
    surface.create_line(100, 100 * i, WIDTH / 2, random.randrange(100, HEIGHT - 100), fill=temp_color, width=2, tags=("line", temp_color))
    surface.create_text(50, 100 * i, text=get_next_left_letter(i - 1), font=('Helvetica', '16'))

colors = ['blue', 'green', 'red', 'yellow', 'white']

for i in range(1, 6):
    temp_color = get_right_random_color()
    create_circle_in_color(WIDTH - 100, 100 * i, 20, temp_color, "right")
    surface.create_line(WIDTH - 100, 100 * i, WIDTH / 2, random.randrange(100, HEIGHT - 100), fill=temp_color, width=2, tags=("line", temp_color))
    surface.create_text(WIDTH - 50, 100 * i, text=i, font=('Helvetica', '16'))

colors = ['blue', 'green', 'red', 'yellow', 'white']

surface.tag_bind(text, '<Button-1>', click_object)
surface.bind("<Button-1>", clicked_on_draw_surface)
top.bind("<Key>", key)

surface.pack()
surface.after(1, tick)
top.mainloop()

