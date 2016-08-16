import tkinter as tk
from tkinter import ttk
import sqlite3
import addition_file as add_py
import subtraction_file as sub_py
import multiplication_file as mul_py
import division_file as div_py


LARGE_FONT = ("Verdana", 12)
##Base code for main window and calling to exercises##
class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self, default="nånting.ico")
        tk.Tk.wm_title(self, "Math trainer")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        name_entry_label  = tk.Label(text="Enter your name: ")
        self.name_entry = tk.Entry()
        name_entry_label.pack()
        self.name_entry.pack()

        ##Creating the Menu##
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Addition",
                             command=lambda: self.call_exercise("add"))
        filemenu.add_command(label="Subtraction",
                             command=lambda: self.call_exercise("sub"))
        filemenu.add_command(label="Multiplication",
                             command=lambda: self.call_exercise("mul"))
        filemenu.add_command(label="Division",
                             command=lambda: self.call_exercise("div"))
        filemenu.add_separator()
        filemenu.add_command(labe="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        highscore_menu = tk.Menu(menubar, tearoff=0)
        highscore_menu.add_command(label="Addition",
                             command=lambda: HighscoreList("addition_highscore"))
        highscore_menu.add_command(label="Subtraction",
                             command=lambda: HighscoreList("subtraction_highscore"))
        highscore_menu.add_command(label="Multiplication",
                             command=lambda: HighscoreList("multiplication_highscore"))
        highscore_menu.add_command(label="Division",
                             command=lambda: HighscoreList("division_highscore"))
        menubar.add_cascade(labe="Highscore", menu=highscore_menu)

        tk.Tk.config(self, menu=menubar)
        
        ##Displaying startpage##
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        ##Creating hightscore list DB##
        self.highscore_create()
            

        
    def call_exercise(self, exercise):
        self.username = str(self.name_entry.get())
        if exercise == "add":
            add_py.Addition(self.username)
        elif exercise == "sub":
            sub_py.Subtraction(self.username)
        elif exercise == "mul":
            mul_py.Multiplication(self.username)
        elif exercise == "div":
            div_py.Division(self.username)

    ##Creating highscore files if not present##
    def highscore_create(self):
        highscore_conn = sqlite3.connect("highscore.db")
        highscore_curs = highscore_conn.cursor()
        highscore_curs.execute("CREATE TABLE IF NOT EXISTS addition_highscore(username TEXT, score INTEGER)")
        highscore_curs.execute("CREATE TABLE IF NOT EXISTS subtraction_highscore(username TEXT, score INTEGER)")
        highscore_curs.execute("CREATE TABLE IF NOT EXISTS multiplication_highscore(username TEXT, score INTEGER)")
        highscore_curs.execute("CREATE TABLE IF NOT EXISTS division_highscore(username TEXT, score INTEGER)")
        highscore_conn.commit
        highscore_curs.close()
        highscore_conn.close()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Choose what you want to do in the menubar",
                          font=LARGE_FONT)
        label.pack(pady=10, padx=10)

##Presenting the highscore list##
class HighscoreList():
    def __init__(self, exercise):
        hs_conn = sqlite3.connect("highscore.db")
        hs_curs = hs_conn.cursor()
        hs_curs.execute("SELECT * FROM "+exercise+" ORDER BY score DESC LIMIT 10")
        self.data = hs_curs.fetchall()
        self.list_to_display = []
        self.create_highscore_list(exercise)

    def create_highscore_list(self, exercise):
        for row in self.data:
            list_to_display.append(row)
            print(self.list_to_display)
            self.highscore_window(exercise)

    def highscore_window(self, exercise):
        div_win = tk.Tk()
        div_win.title(exercise)
        canvas = tk.Canvas()
        

app = MainWindow()
app.mainloop()
