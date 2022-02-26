# class MacrosCalculator:
#     def __init__(self, weight):
#         self.weight = weight
#
# entry = MacrosCalculator(56)
# print(entry.weight)

from tkinter import *

window = Tk()
window.geometry("400x400")

value1 = StringVar(window, "1")
value2 = StringVar(window, "3")

values1= {"Female" : "1", "Male" : "2"}

values2 = {
            "Sedentary (little or no exercise)" : "2",
            "Lightly active (light exercise/sports 1-3 days/week)" : "3",
            "Moderately active (moderate exercise/sports 3-5 days/week)" : "4",
            "Very active (hard exercise/sports 6-7 days a week)" : "5",
            "If you are extra active (very hard exercise/sports & a physical job)" : "6"
          }


intro = Label(window, text="Macros calculator")

label1 = Label(window, text = "Insert your weight")
entry1 = Entry(window)
label2 = Label(window, text = "Insert your height")
entry2 = Entry(window)
label3 = Label(window, text = "Insert your age")
entry3 = Entry(window)
label4 = Label(window, text = "Select: ")


label5 = Label(window, text = "Select: ")

intro.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
label4.pack()

for (text, value) in values1.items():
    Radiobutton(window, text = text, variable = value1, value = value).pack()

for (text, value) in values2.items():
    Radiobutton(window, text = text, variable = value2, value = value).pack()

window.mainloop()