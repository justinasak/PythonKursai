from tkinter import *
from tkinter import messagebox, ttk
import AddFood as food
import CurrentProgress as cpr
import MacrosCalc as mcalc

class MainApplication(Tk):
    def __init__(self):
        super().__init__()

        self.title("Macros App")
        self.geometry("600x700")
        self.protocol('WM_DELETE_WINDOW', self.exiting)

        self.tab_parent = ttk.Notebook(self)

        self.window = mcalc.MacrosCalc(self.tab_parent)
        self.food_window = food.AddFood(self.tab_parent)
        self.progress_window = cpr.Progress(self.tab_parent)

        self.tab_parent.add(self.window, text="Macros Calculator")
        self.tab_parent.add(self.food_window, text="Add Food")
        self.tab_parent.add(self.progress_window, text="Current progress")

        self.tab_parent.pack(expand=1, fill='both')
        self.bind("<Escape>", lambda event: self.exiting())

        meniu = Menu(self)
        self.config(menu=meniu)
        submeniu = Menu(meniu, tearoff = 0)

        meniu.add_cascade(label="Options", menu=submeniu)
        submeniu.add_command(label="Refresh", command=self.refresh_data)
        submeniu.add_command(label="Exit", command=self.exiting)


    def exiting(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to leave?")
        if answer is True:
            self.destroy()
        else:
            pass

    def delete_data(self):
        answer = messagebox.askyesno("", "Are you sure you want to clear data?")
        if answer is True:
            fd = food.AddFood()
            if fd.delete_food() is True:
                messagebox.showinfo("Success", "Data cleared successfully")
            else:
                messagebox.showinfo("Unsuccess", "Could not clear data")
        else:
            pass

    def refresh_data(self):
        self.destroy()
        self.__init__()


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()




