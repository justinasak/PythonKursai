from tkinter import *
from tkinter import messagebox
import MacrosCalculator as mc

def validate_entry(input):
    if input == "":
        return True
    try:
        input1 = float(input)
    except ValueError:
        return False
    return 0.00 <= input1 <= 300

def check_entries():
    if float(entry1.get()) < 15:
        messagebox.showerror("Error", "Minimum weight is 15 kg")
    elif float(entry2.get()) < 50:
        messagebox.showerror("Error", "Minimum height is 50 cm")
    elif float(entry3.get()) < 18:
        messagebox.showerror("Error", "Calculator not recommended for minors")
    else:
        calculate()

def calculate():
    weight = float(entry1.get())
    height = float(entry2.get())
    age = float(entry3.get())
    gender = float(value1.get())
    alvl = float(value2.get())
    goal = float(value3.get())
    calculation = mc.MacrosCalculator(weight, height, age, gender, alvl, goal)
    result = calculation.calculatebmr()
    answer = messagebox.askquestion("Recommended kcal", f"Your recommended amount per day is {result} kcal. Do you want to continue?")
    if answer == 'yes':
        # save to db or sth similar
        pass
    else:
        pass

window = Tk()
window.title("Macros Calculator")
window.geometry("500x530")

value1 = StringVar(window, 5)
value2 = StringVar(window, 1.2)
value3 = StringVar(window, 0)
result = ""

values1 = {"Female" : -161, "Male" : 5}

values2 = {
            "Sedentary (little or no exercise)" : 1.2,
            "Lightly active (light exercise/sports 1-3 days/week)" : 1.375,
            "Moderately active (moderate exercise/sports 3-5 days/week)" : 1.55,
            "Very active (hard exercise/sports 6-7 days a week)" : 1.725,
            "If you are extra active (very hard exercise/sports & a physical job)" : 1.9
          }

values3 = {"Lose weight" : -500,
           "Maintain the same weight" : 0,
           "Gain weight" : 500}

vcmd = (window.register(validate_entry), "%P")
label1 = Label(window, text = "Insert your weight (kg):")
entry1 = Entry(window, validate = "key", validatecommand=vcmd)
label2 = Label(window, text = "Insert your height (cm):")
entry2 = Entry(window, validate = "key", validatecommand=vcmd)
label3 = Label(window, text = "Insert your age:")
entry3 = Entry(window, validate = "key", validatecommand=vcmd)
label4 = Label(window, text = "Select your gender: ")
label5 = Label(window, text = "Select your activity level: ")
label6 = Label(window, text = "Select your goal: ")
button1 = Button(window, text = "Calculate", command=check_entries)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()

for (text, value) in values1.items():
    Radiobutton(window, text = text, variable = value1, value = value).pack()

label5.pack()

for (text, value) in values2.items():
    Radiobutton(window, text = text, variable = value2, value = value).pack()

label6.pack()

for (text, value) in values3.items():
    Radiobutton(window, text = text, variable = value3, value = value).pack()

button1.pack()

window.mainloop()