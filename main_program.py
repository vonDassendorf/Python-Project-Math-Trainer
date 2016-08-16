import tkinter as tk
from tkinter import ttk
import multiplication_file as mul_py
import addition_file as add_py
import subtraction_file as sub_py
import division_file as div_py


LARGE_FONT = ("Verdana", 12)
##Base code for main window and to show the desired page##
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

        tk.Tk.config(self, menu=menubar)        
        
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
            

        
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



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Choose what you want to do in the menubar",
                          font=LARGE_FONT)
        label.pack(pady=10, padx=10)


class HighscoreList():
    def __init__(self, exercise):
        ##Creating and loading the Highscore list##
        self.highscore_list_file = open("highscore.txt", "r")

app = MainWindow()
app.mainloop()
