class MacrosCalculator:
    def __init__(self, weight, height, age, gender, alvl, goal):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.alvl = alvl
        self.goal = goal


    def calculatebmr(self):
        print ((10 * self.weight + 6.25 * self.height - 5 * self.age + self.gender) * self.alvl + self.goal)