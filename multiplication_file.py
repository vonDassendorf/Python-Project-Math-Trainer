import tkinter as tk
from tkinter import ttk
import random


class Multiplication():

    def __init__(self, username):
        self.ran_term1 = random.randint(0,10)      
        self.ran_term2  = random.randint(0,10)
        self.exercise_str = str(self.ran_term1)+'*'+str(self.ran_term2)
        self.points = 0
        self.username = username
        self.multiplication_window()

    def multiplication_window(self):
        mul_win = tk.Tk()
        mul_win.title("multiplication")
        canvas = tk.Canvas()
        self.lbl1 = ttk.Label(mul_win, text="Assignment: "+self.exercise_str)
        self.mul_ent = ttk.Entry(mul_win, width=5)
        self.mul_btn = ttk.Button(mul_win, text="Check Answer", command=self.callback)
        self.lbl2 = ttk.Label(mul_win, text="")
        self.lbl3 = ttk.Label(mul_win, text="Points: "+str(self.points))

        self.lbl1.grid(row=0, column=0)
        self.mul_ent.grid(row=0, column=1)
        self.mul_btn.grid(row=1, column=1)
        self.lbl2.grid(row=2, column=0)
        self.lbl3.grid(row=3, column=0)

        self.mul_ent.focus()
        self.mul_ent.bind("<Return>", lambda e: self.callback())
        
        mul_win.mainloop()

    def callback(self):
        try:
            entry_str = str(self.mul_ent.get())
            entry_int = int(entry_str)
            exercise_result = self.ran_term1*self.ran_term2
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
                self.ran_term1 = random.randint(1,10)
                self.ran_term2 = random.randint(1,20)
            elif self.points > 20:
                self.ran_term1 = random.randint(1,20)
                self.ran_term2 = random.randint(1,20)
            elif self.points > 50:
                self.ran_term1 = random.randint(1,50)
                self.ran_term2 = random.randint(1,100)
            elif self.points > 100:
                self.ran_term1 = random.randint(1,100)
                self.ran_term2 = random.randint(1,100)
            self.exercise_str = str(self.ran_term1)+"*"+str(self.ran_term2)
            self.lbl1.configure(text="Assignment: "+self.exercise_str)
            self.mul_ent.delete(0, 'end')
            self.mul_ent.focus()
        except ValueError:
            self.lbl2.config(text="Please enter an integer")

    def add_to_highscore(self):
        highscore_conn = sqlite3.connect("highscore.db")
        highscore_curs = highscore_conn.cursor()
        entry = (self.username, self.points)
        highscore_curs.execute("SELECT * FROM multiplication_highscore ORDER BY score ASC")
        highscore_curs.execute("INSERT OR REPLACE INTO multiplication_highscore (username, score) VALUES (?,?)", entry)
        highscore_conn.commit()
        highscore_curs.close()
        highscore_conn.close()
