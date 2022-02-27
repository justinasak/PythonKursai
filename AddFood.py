from tkinter import *
from tkinter import messagebox, ttk

class Food(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        labelA = ttk.Label(self, text = "Add Food")
        labelA.configure(font=("Helvetica", 18, "bold"))
        labelA.pack()

        value1 = StringVar(self, 1)
        values1 = {"Breakfast": 1, "Lunch": 2, "Dinner" : 3, "Snack" : 4}
        label = Label(self, text = "Category")
        label1 = Label(self, text="Description")
        entry1 = Entry(self)
        label6 = Label(self, text="Nutrition facts per 100g")
        label6.configure(font=("Helvetica", 16, "bold"))
        label2 = Label(self, text="Calories (kcal)")
        entry2 = Entry(self)
        label3 = Label(self, text="Fat (g)")
        entry3 = Entry(self)
        label4 = Label(self, text="Carbohydrate (g)")
        entry4 = Entry(self)
        label5 = Label(self, text="Protein (g)")
        entry5 = Entry(self)
        label7 = Label(self, text="Portion (g)")
        label7.configure(font=("Helvetica", 16, "bold"))
        entry7 = Entry(self)
        button1 = Button(self, text="Save", command=self.save)

        label.pack()
        for (text, value) in values1.items():
            Radiobutton(self, text=text, variable=value1, value=value).pack()
        label1.pack()
        entry1.pack()
        label6.pack()
        label2.pack()
        entry2.pack()
        label3.pack()
        entry3.pack()
        label4.pack()
        entry4.pack()
        label5.pack()
        entry5.pack()
        label7.pack()
        entry7.pack()
        button1.pack()

    def save(self):
        pass
