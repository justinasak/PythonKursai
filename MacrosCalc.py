from tkinter import *
from tkinter import messagebox, ttk
import MacrosCalculator as mc
import Goal as gl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///macros.db')
Session = sessionmaker(bind=engine)
session = Session()

class MacrosCalc(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.value1 = StringVar(self, 5)
        self.value2 = StringVar(self, 1.2)
        self.value3 = StringVar(self, 0)
        self.result = None

        values1 = {"Female": -161, "Male": 5}

        values2 = {
            "Sedentary (little or no exercise)": 1.2,
            "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
            "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
            "Very active (hard exercise/sports 6-7 days a week)": 1.725,
            "If you are extra active (very hard exercise/sports & a physical job)": 1.9
        }

        values3 = {"Lose weight": -500,
                   "Maintain the same weight": 0,
                   "Gain weight": 500}

        vcmd = (self.register(self.validate_entry), "%P")
        self.label1 = Label(self, text="Insert your weight (kg):")
        self.entry1 = Entry(self, validate="key", validatecommand=vcmd)
        self.label2 = Label(self, text="Insert your height (cm):")
        self.entry2 = Entry(self, validate="key", validatecommand=vcmd)
        self.label3 = Label(self, text="Insert your age:")
        self.entry3 = Entry(self, validate="key", validatecommand=vcmd)
        self.label4 = Label(self, text="Select your gender: ")
        self.label5 = Label(self, text="Select your activity level: ")
        self.label6 = Label(self, text="Select your goal: ")
        self.button1 = Button(self, text="Calculate", command=self.check_entries)
        self.bind("<Return>", lambda event: self.check_entries())
        self.label7 = Label(self, text="Your current kcal goal: ")

        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()
        self.label4.pack()

        for (text, value) in values1.items():
            Radiobutton(self, text=text, variable=self.value1, value=value).pack()

        self.label5.pack()

        for (text, value) in values2.items():
            Radiobutton(self, text=text, variable=self.value2, value=value).pack()

        self.label6.pack()

        for (text, value) in values3.items():
            Radiobutton(self, text=text, variable=self.value3, value=value).pack()

        self.button1.pack()

    def validate_entry(self, input):
        if input == "":
            return True
        try:
            input1 = float(input)
        except ValueError:
            return False
        return 0.00 <= input1 <= 300

    def check_entries(self):
        if float(self.entry1.get()) < 15:
            messagebox.showerror("Error", "Minimum weight is 15 kg")
        elif float(self.entry2.get()) < 50:
            messagebox.showerror("Error", "Minimum height is 50 cm")
        elif float(self.entry3.get()) < 18:
            messagebox.showerror("Error", "Calculator not recommended for minors")
        else:
            self.calculate()

    def calculate(self):
        weight = float(self.entry1.get())
        height = float(self.entry2.get())
        age = float(self.entry3.get())
        gender = float(self.value1.get())
        alvl = float(self.value2.get())
        goal = float(self.value3.get())
        calculation = mc.MacrosCalculator(weight, height, age, gender, alvl, goal)
        self.result = calculation.calculatebmr()
        answer = messagebox.askquestion("Recommended kcal",
                                        f"Your recommended amount per day is {self.result} kcal. Do you want to save it?")
        if answer == 'no':
            pass
        else:
            self.save()

    def save(self):
        goal = gl.Goal(float(self.result))
        session.add(goal)
        session.commit()
        messagebox.showinfo("Success", "Successfully saved")