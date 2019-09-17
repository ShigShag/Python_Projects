class Person:

    def __init__(self, name, personality, issitting, robotowned):
        self.name = name
        self.personality = personality
        self.isSitting = issitting
        self.robotOwned = robotowned

    def sit_down(self):
        self.isSitting = True

    def sit_up(self):
        self.isSitting = False


class Robot:

    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is: " + self.name)


r1 = Robot("Tom", "red", 56)
r2 = Robot("Henry", "blue", 35)

r1.introduce_self()
r2.introduce_self()

p1 = Person("Alice", "aggressive", False, "r2")
p2 = Person("Becky", "talkative", True, "r1")

