import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
##Start page to show when program is started##
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
