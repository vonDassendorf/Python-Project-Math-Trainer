from tkinter import *
import random

ran1 = random.randint(0,10)      
ran2 = random.randint(0,10)
exercise_str = str(ran1)+'+'+str(ran2)
points = 0


def addition():
    add_win = Tk()
    add_win.title("Addition")
    canvas = Canvas()
    lbl1 = Label(add_win, text="Assignment: "+exercise_str)
    add_ent = Entry(add_win, width=5)
    add_btn = Button(add_win, text="Check Answer", command=callback)
    lbl2 = Label(add_win, text="")
    lbl3 = Label(add_win, text="Points: "+str(points))

    lbl1.grid(row=0, column=0)
    add_ent.grid(row=0, column=1)
    add_btn.grid(row=1, column=1)
    lbl2.grid(row=2, column=0)
    lbl3.grid(row=3, column=0)
    add_win.mainloop()

def callback():
    global ran1
    global ran2
    global exercise_str
    global exercise
    global math_list
    global randmath
    global add_ent
    try:
        entry_str = str(add_ent.get())
        entry_int = int(entry_str)
        equation = ran1+ran2
        if entry_int == exercise:
            lbl2.configure(text="Correct!")
            global points
            points += 1
        else:
            lbl2.configure(text="Incorrect, answer is " + str(exercise))
            points = 0
        lbl3.configure(text="Points: "+str(points))
        randmath = random.choice(math_list)
        ran1 = random.randint(1,10)
        ran2 = ran2_func()
        equation_str = str(ran1)+randmath+str(ran2)
        lbl1.configure(text="Assignment: "+exercise_str)
        ent.delete(0, 'end')
    except ValueError:
        print("Please enter a integer")
