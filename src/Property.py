class Property:
    def __init__(self, name, sqf, value, growth, amountOwed, isPaidOff, happinessDecay):
        self.name = name
        self.sqf = sqf
        self.value = value
        self.growth = growth
        self.amountOwed = amountOwed
        self.isPaidOff = isPaidOff
        self.happinessDecay = happinessDecay


    def growInVlaue(self):
        self.value = self.value * (100*self.growth)