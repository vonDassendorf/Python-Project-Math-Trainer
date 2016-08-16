import tkinter as tk
from tkinter import ttk
import random


class Division():

    def __init__(self, username):
        self.ran_term1 = random.randint(0,10)      
        self.ran_term2  = random.randint(0,10)
        self.exercise_str = str(self.ran_term1)+'/'+str(self.ran_term2)
        self.points = 0
        self.username = username
        self.division_window()

    def division_window(self):
        div_win = tk.Tk()
        div_win.title("Addition")
        canvas = tk.Canvas()
        self.lbl1 = ttk.Label(div_win, text="Assignment: "+self.exercise_str)
        self.div_ent = ttk.Entry(div_win, width=5)
        self.div_btn = ttk.Button(div_win, text="Check Answer", command=self.callback)
        self.lbl2 = ttk.Label(div_win, text="")
        self.lbl3 = ttk.Label(div_win, text="Points: "+str(self.points))

        self.lbl1.grid(row=0, column=0)
        self.div_ent.grid(row=0, column=1)
        self.div_btn.grid(row=1, column=1)
        self.lbl2.grid(row=2, column=0)
        self.lbl3.grid(row=3, column=0)
        div_win.mainloop()

    def callback(self):
        try:
            entry_str = str(self.div_ent.get())
            entry_int = float(entry_str)
            exercise_result = int((self.ran_term1/self.ran_term2 * 100) + 0.5) / 100.0 #returns 2 decimals
            if entry_int == exercise_result:
                self.lbl2.configure(text="Correct!")
                self.points += 1
                self.add_to_highscore()
            else:
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
            self.exercise_str = str(self.ran_term1)+"/"+str(self.ran_term2)
            self.lbl1.configure(text="Assignment: "+self.exercise_str)
            self.div_ent.delete(0, 'end')
        except ValueError:
            print("Please enter an integer")

    def add_to_highscore(self):
        self.highscore_dict = {}
        self.highscore_list_file = open("highscore_division.txt", "w")
        self.highscore_dict[self.username] = self.points
        self.highscore_list_file.write(str(self.highscore_dict)+"\n")
        self.highscore_list_file.close()
        
