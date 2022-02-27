from tkinter import *
from tkinter import messagebox, ttk
import Food as fd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text as sa_text

engine = create_engine('sqlite:///macros.db')
Session = sessionmaker(bind=engine)
session = Session()

class AddFood(ttk.Frame):
    def __init__(self, container=[]):
        super().__init__()
        #self.configure(background="#b2e0a4")
        labelA = ttk.Label(self, text = "Add Food")
        labelA.configure(font=("Helvetica", 18, "bold"))
        labelA.pack()

        vcmd = (self.register(self.validate_entry), "%P")

        self.value1 = StringVar(self, 1)
        self.values1 = {"Breakfast": 1, "Lunch": 2, "Dinner" : 3, "Snack" : 4}
        self.label = Label(self, text = "Category")
        self.label1 = Label(self, text="Description")
        self.entry1 = Entry(self)
        self.label6 = Label(self, text="Nutrition facts per 100g")
        self.label6.configure(font=("Helvetica", 16, "bold"))
        self.label2 = Label(self, text="Calories (kcal)")
        self.entry2 = Entry(self, validate="key", validatecommand=vcmd)
        self.label3 = Label(self, text="Fat (g)")
        self.entry3 = Entry(self, validate="key", validatecommand=vcmd)
        self.label4 = Label(self, text="Carbohydrate (g)")
        self.entry4 = Entry(self, validate="key", validatecommand=vcmd)
        self.label5 = Label(self, text="Protein (g)")
        self.entry5 = Entry(self, validate="key", validatecommand=vcmd)
        self.label7 = Label(self, text="Portion (g)")
        self.label7.configure(font=("Helvetica", 16, "bold"))
        self.entry7 = Entry(self, validate="key", validatecommand=vcmd)
        self.button1 = Button(self, text="Add", command=self.save)

        self.label.pack()
        for (text, value) in self.values1.items():
            Radiobutton(self, text=text, variable=self.value1, value=value).pack()
        self.label1.pack()
        self.entry1.pack()
        self.label6.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()
        self.label4.pack()
        self.entry4.pack()
        self.label5.pack()
        self.entry5.pack()
        self.label7.pack()
        self.entry7.pack()
        self.button1.pack()

    def save(self):
        food = fd.Food(self.entry1.get(), self.value1.get(), float(self.entry2.get()),
                       float(self.entry3.get()), float(self.entry4.get()),
                       float(self.entry5.get()), float(self.entry7.get()))
        session.add(food)
        session.commit()
        messagebox.showinfo("Success", "Successfully added")
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry7.delete(0, 'end')

    def validate_entry(self, input):
        if input == "":
            return True
        try:
            input1 = float(input)
        except ValueError:
            return False
        return 0.00 <= input1 <= 500000

