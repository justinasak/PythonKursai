from tkinter import *
from tkinter import messagebox, ttk
import AddFood as food
import CurrentProgress as cpr
import MacrosCalc as mcalc

class MainApplication(Tk):
    def __init__(self):
        super().__init__()

        self.title("Macros App")
        self.geometry("500x600")

        self.tab_parent = ttk.Notebook(self)

        self.food_window = food.Food(self.tab_parent)
        self.progress_window = cpr.Progress(self.tab_parent)
        self.window = mcalc.MacrosCalc(self.tab_parent)

        self.tab_parent.add(self.food_window, text="Add Food")
        self.tab_parent.add(self.progress_window, text="Current progress")
        self.tab_parent.add(self.window, text="Macros Calculator")

        self.tab_parent.pack(expand=1, fill='both')
        self.bind("<Escape>", lambda event: self.exiting())


    def exiting(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to leave?")
        if answer is True:
            self.destroy()
        else:
            pass

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()




