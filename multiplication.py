from tkinter import *
import random



def multiplication():
    multiwin = Tk()
    multiwin.title("Mulptiplication exercises")
    multiwin.wm_iconbitmap("mulicon.ico")
    canvas = Canvas(multiwin)
    #lbl1 = Label()
    lbl2 = Label(multiwin,text="Enter your answer")
    answer_entry = Entry(multiwin)
    btn_commit = Button(multiwin, text="Commit answer", width=12)
    #lbl1.grid(row=0,column=0)
    lbl2.grid(row=1,column=0)
    answer_entry.grid(row=1,column=1)
    btn_commit.grid(row=2,column=1)
    multiwin.mainloop()
