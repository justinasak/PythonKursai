import tkinter
from tkinter import messagebox, ttk
from Food import Food as fd
from Goal import Goal as gl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///macros.db')
Session = sessionmaker(bind=engine)
session = Session()

class Progress(tkinter.Frame):
    def __init__(self, container):
        super().__init__()

        allfood = session.query(fd).all()
        goal = session.query(gl).get(1)

        ttk.Label(self, text = "Daily Caloric Requirement").grid(row=0, column=1)
        ttk.Label(self, text=goal.bmr).grid(row=1, column=1)

        ttk.Label(self, text = "Macronutrients Distribution").grid(row=2, column=1)
        ttk.Label(self, text = "Carbohydrate").grid(row=3, column=0)
        ttk.Label(self, text=f"{goal.bmr * 0.5 / 4} g").grid(row=4, column=0)
        ttk.Label(self, text=f"{goal.bmr * 0.5} kcal").grid(row=5, column=0)
        ttk.Label(self, text = "Protein").grid(row=3, column=1)
        ttk.Label(self, text=f"{goal.bmr * 0.2 / 4} g").grid(row=4, column=1)
        ttk.Label(self, text=f"{goal.bmr * 0.2} kcal").grid(row=5, column=1)
        ttk.Label(self, text="Fat").grid(row=3, column=2)
        ttk.Label(self, text=f"{goal.bmr * 0.3 / 9} g").grid(row=4, column=2)
        ttk.Label(self, text=f"{goal.bmr * 0.3} kcal").grid(row=5, column=2)

        # for food in allfood:
        #     ttk.Label(self, text= f"{food.description}, {food.category}").pack()

