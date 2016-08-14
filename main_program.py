import tkinter as tk
from tkinter import ttk
import multiplication as mul_py
import addition_file as add_py

##root = Tk()
##root.title("MathProject")
##canvas = Canvas(root)
##lbl1 = Label(root, text="Enter a name:")
##name_entr = Entry()
##lbl2 = Label(root, text="Choose a program to exercise")
##btn_add = Button(root, text="Addition", width=10, command=add_py.addition)
##btn_sub = Button(root, text="Subtraction", width=10)
##btn_mul = Button(root, text="Multiplication", width=10, command=mul_py.multiplication)
##btn_div = Button(root, text="Divition", width=10)
##lbl1.grid(row=0, column=0)
##name_entr.grid(row=0, column=1)
##lbl2.grid(row=1, columnspan=2)
##btn_add.grid(row=2, column=0)
##btn_sub.grid(row=2, column=1)
##btn_mul.grid(row=3, column=0)
##btn_div.grid(row=3, column=1)
##root.mainloop()

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

        ##Creating the Menu##
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Addition", command=add_py.Addition)
        filemenu.add_command(label="Subtraction")
        filemenu.add_command(label="Multiplication",
                             command=lambda:self.show_frame(mul_py.MultiplicationPage))
        filemenu.add_command(label="Division")
        filemenu.add_separator()
        filemenu.add_command(labe="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        tk.Tk.config(self, menu=menubar)        
        
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self,
                          text="Choose what you want to do in the menubar",
                          font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        self.name_entry_box()
        
    def name_entry_box(self):
        name_entry_label  = tk.Label(text="Enter your name: ")
        self.name_entry = tk.Entry()
        name_entry_label.pack()
        self.name_entry.pack()


class HighscoreList():
    def __init__(self, exercise):
        ##Creating and loading the Highscore list##
        self.highscore_list = {'add': {},'sub': {},'div': {},'mul': {}}
        self.highscore_list_file = open("highscore.txt", "w")
        self.highscore_add(exercise)

        ##Adding results to highscore##
    def highscore_add(self, exercise):
        if exercise == "+":
            if len(self.highscore_list['add'].keys()) < 10 and result > min(self.highscore_list,
                                            key=self.highscore_list.get):
                self.highscore_list['add'][username] = points
            elif result > min(self.highscore_list, key=self.highscore_list.get):
                self.highscore_list.pop([min(self.highscore_list,
                                            key=self.highscore_list.get)], None)
                self.highscore_list['add'][username] = points
        

app = MainWindow()
app.mainloop()

#ran1 = random.randint(0,10)

#def ran2_func():
#    if randmath == "-":
#        return random.randint(1,ran1)
#    else:
#        return random.randint(1,10)      

#math_list = ["+","-","*"]
#randmath = random.choice(math_list)
#ran2 = ran2_func()
#equation_str = str(ran1)+randmath+str(ran2)
#points = 0

#def callback():
#    global ran1
#    global ran2
#    global equation_str
#    global equation
#    global math_list
#    global randmath
#    try:
#        entry_str = str(ent.get())
#        entry_int = int(entry_str)
#        equation = eval(str(ran1)+randmath+str(ran2))
#        if entry_int == equation:
#            lbl2.configure(text="Correct!")
#            global points
#            points += 1
#        else:
#            lbl2.configure(text="Incorrect, answer is " + str(equation))
#            points = 0
#        lbl3.configure(text="Points: "+str(points))
#        randmath = random.choice(math_list)
#        ran1 = random.randint(1,10)
#        ran2 = ran2_func()
#        equation_str = str(ran1)+randmath+str(ran2)
#        lbl1.configure(text="Assignment: "+equation_str)
#        ent.delete(0, 'end')
#    except ValueError:
#        print("Please enter a integer")    

#window = Tk()
#window.title("MathProject")
#window.geometry("200x105")
#lbl1 = Label(window, text="Assignment: "+equation_str)
#ent = Entry(window, width=5)
#btn = Button(window, text="Check Answer", command=callback)
#lbl2 = Label(window, text="")
#lbl3 = Label(window, text="Points: "+str(points))

#lbl1.pack()
#ent.pack()
#btn.pack()
#lbl2.pack()
#lbl3.pack()
#window.mainloop()
