import tkinter
from tkinter import messagebox, ttk, Button
from Goal import Goal as gl
from Food import Food as fd
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text as sa_text

engine = create_engine('sqlite:///macros.db')
Session = sessionmaker(bind=engine)
session = Session()

class Progress(tkinter.Frame):
    def __init__(self, container):
        super().__init__()

        try:
            goal_id = session.query(func.max(gl.id)).scalar()
            goal = session.query(gl).get(goal_id)
            self.add_attributes(goal)
        except AttributeError:
            top_frame = tkinter.Frame(self)
            top_frame.grid(row=0, column=0)
            ttk.Label(top_frame, text="To see the progress you need to calculate the goal using macros calculator", font=("Helvetica", 18, "bold")).grid(row=0, column=2)

    def add_attributes(self, goal):
        top_frame = tkinter.Frame(self)
        top_frame.grid(row=0, column=0)
        foods_frame = tkinter.Frame(self)
        foods_frame.grid(row=1, column=0)

        ttk.Label(top_frame, text = "Daily Caloric Requirement",font=("Helvetica", 16, "bold")).grid(row=0, column=2)
        ttk.Label(top_frame, text=f"{round(goal.bmr,2)} kcal").grid(row=1, column=2)

        ttk.Label(top_frame, text = "Macronutrients Distribution", font=("Helvetica", 16, "bold")).grid(row=2, column=2)
        ttk.Label(top_frame, text = "Carbohydrate").grid(row=3, column=1)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.5 / 4, 2)} g").grid(row=4, column=1)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.5, 3)} kcal").grid(row=5, column=1)
        ttk.Label(top_frame, text = "Protein").grid(row=3, column=2)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.2 / 4, 2)} g").grid(row=4, column=2)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.2, 2)} kcal").grid(row=5, column=2)
        ttk.Label(top_frame, text="Fat").grid(row=3, column=3)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.3 / 9, 2)} g").grid(row=4, column=3)
        ttk.Label(top_frame, text=f"{round(goal.bmr * 0.3, 2)} kcal").grid(row=5, column=3)

        categories = [ "Breakfast Total",
                       "Lunch Total",
                       "Dinner Total",
                       "Snacks Total"]

        values = [1, 2, 3, 4]

        x=1
        y = 0
        for category in categories:
            ttk.Label(foods_frame, text=category, font=("Helvetica", 15, "bold")).grid(row=y, column=1)
            y=y+5
        for value in values:
            ttk.Label(foods_frame, text="Carbohydrate").grid(row=x+1, column=0)
            carbohydrates = round(session.query(func.sum(fd.carbs)).filter(fd.category==value).scalar(),2)
            ttk.Label(foods_frame, text=f"{carbohydrates} g").grid(row=x+2, column=0)
            ttk.Label(foods_frame, text=f"{carbohydrates*4} kcal").grid(row=x+3, column=0)

            ttk.Label(foods_frame, text="Protein").grid(row=x+1, column=1)
            proteins = round(session.query(func.sum(fd.protein)).filter(fd.category==value).scalar(),2)
            ttk.Label(foods_frame, text=f"{proteins} g").grid(row=x+2, column=1)
            ttk.Label(foods_frame, text=f"{proteins * 4} kcal").grid(row=x+3, column=1)

            ttk.Label(foods_frame, text="Fat").grid(row=x+1, column=2)
            fats = round(session.query(func.sum(fd.fat)).filter(fd.category==value).scalar(),2)
            ttk.Label(foods_frame, text=f"{fats} g").grid(row=x+2, column=2)
            ttk.Label(foods_frame, text=f"{round(fats * 9,2)} kcal").grid(row=x+3, column=2)
            x=x+5

        label_rem = ttk.Label(foods_frame, text="Remaining Calories/Amounts Distribution")
        label_rem.configure(font=("Helvetica", 16, "bold"))
        label_rem.grid(row=20, column=1)

        ttk.Label(foods_frame, text="Carbohydrate").grid(row=21, column=0)
        total_carbs = round(session.query(func.sum(fd.carbs)).scalar(), 2)
        rem_carbs = round(goal.bmr * 0.5 / 4 - total_carbs, 2)
        ttk.Label(foods_frame, text=f"{rem_carbs} g").grid(row=22, column=0)
        ttk.Label(foods_frame, text=f"{rem_carbs * 4} kcal").grid(row=23, column=0)

        ttk.Label(foods_frame, text="Protein").grid(row=21, column=1)
        total_proteins = round(session.query(func.sum(fd.protein)).scalar(), 2)
        rem_protein = round(goal.bmr * 0.2 / 4 - total_proteins, 2)
        ttk.Label(foods_frame, text=f"{rem_protein} g").grid(row=22, column=1)
        ttk.Label(foods_frame, text=f"{rem_protein * 4} kcal").grid(row=23, column=1)

        ttk.Label(foods_frame, text="Fat").grid(row=21, column=2)
        total_fats = round(session.query(func.sum(fd.fat)).scalar(), 2)
        rem_fat = round(goal.bmr * 0.3 / 9 - total_fats, 2)
        ttk.Label(foods_frame, text=f"{rem_fat} g").grid(row=22, column=2)
        ttk.Label(foods_frame, text=f"{rem_fat * 9} kcal").grid(row=23, column=2)

