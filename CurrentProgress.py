import tkinter
from tkinter import messagebox, ttk

class Progress(tkinter.Frame):
    def __init__(self, container):
        super().__init__()

        self.labelA = ttk.Label(self, text = "Current Progress")
        self.labelA.pack()

