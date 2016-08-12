from tkinter import *
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


class MainWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_main_window()

    def init_main_window(self):
        self.master.title("Math Trainer")
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)
        file = Menu(main_menu)
        file.add_command(label="Addition", command=add_py.addition)
        file.add_command(label="Subtraction")
        file.add_command(label="Multiplication", command=mul_py.multiplication)
        file.add_command(label="Division")
        main_menu.add_cascade(label="File", menu=file)

root = Tk()
app = MainWindow(root)
root.mainloop()

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
