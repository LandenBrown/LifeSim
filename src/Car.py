import random

class Car:
    def __init__(self, name, worth, condition):
        self.name = name
        self.worth = worth
        self.condition = condition


    def conditionCheck(self):
        conditioonChance = random.randint(1, 100)
        if conditioonChance > self.condition:
            print ("This will evaluate to be a repair")



