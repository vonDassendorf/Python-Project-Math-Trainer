import tkinter as tk
from tkinter import ttk
import random


class Addition():

    def __init__(self, username):
        self.ran_term1 = random.randint(0,10)      
        self.ran_term2  = random.randint(0,10)
        self.exercise_str = str(self.ran_term1)+'+'+str(self.ran_term2)
        self.points = 0
        self.username = username
        self.addition_window()

    def addition_window(self):
        add_win = tk.Tk()
        add_win.title("Addition")
        canvas = tk.Canvas()
        self.lbl1 = ttk.Label(add_win, text="Assignment: "+self.exercise_str)
        self.add_ent = ttk.Entry(add_win, width=5)
        self.add_btn = ttk.Button(add_win, text="Check Answer", command=self.callback)
        self.lbl2 = ttk.Label(add_win, text="")
        self.lbl3 = ttk.Label(add_win, text="Points: "+str(self.points))

        self.lbl1.grid(row=0, column=0)
        self.add_ent.grid(row=0, column=1)
        self.add_btn.grid(row=1, column=1)
        self.lbl2.grid(row=2, column=0)
        self.lbl3.grid(row=3, column=0)

        self.add_ent.focus()
        self.add_ent.bind("<Return>", lambda e: self.callback())
        
        add_win.mainloop()

    def callback(self):
        try:
            entry_str = str(self.add_ent.get())
            entry_int = int(entry_str)
            exercise_result = self.ran_term1+self.ran_term2
            if entry_int == exercise_result:
                self.lbl2.configure(text="Correct!")
                self.points += 1
            else:
                self.add_to_highscore()
                self.lbl2.configure(text="Incorrect, answer is " + str(exercise_result))
                self.points = 0
            self.lbl3.configure(text="Points: "+str(self.points))
            if self.points <= 10:
                self.ran_term1 = random.randint(1,10)
                self.ran_term2 = random.randint(1,10)
            if self.points > 10:
                self.ran_term1 = random.randint(1,50)
                self.ran_term2 = random.randint(1,100)
            elif self.points > 20:
                self.ran_term1 = random.randint(1,100)
                self.ran_term2 = random.randint(1,100)
            elif self.points > 50:
                self.ran_term1 = random.randint(1,500)
                self.ran_term2 = random.randint(1,500)
            elif self.points > 100:
                self.ran_term1 = random.randint(1,1000)
                self.ran_term2 = random.randint(1,1000)
            self.exercise_str = str(self.ran_term1)+"+"+str(self.ran_term2)
            self.lbl1.configure(text="Assignment: "+self.exercise_str)
            self.add_ent.delete(0, 'end')
            self.add_ent.focus()
        except ValueError:
            print("Please enter an integer")

    def add_to_highscore(self):
        self.highscore_dict = {}
        self.highscore_list_file = open("highscore_addition.txt", "w")
        self.highscore_dict[self.username] = self.points
        self.highscore_list_file.write(str(self.highscore_dict)+"\n")
        self.highscore_list_file.close()
        
