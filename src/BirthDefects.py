class BirthDefect:
    def __init__(self, name, intelligenceDecay, healthDecay, treatable, treatmentCost, treatmentRounds):
        self.name = name
        self.intelligenceDecay = intelligenceDecay
        self.healthDecay = healthDecay
        self.treatmentCost = treatmentCost
        self.treatmentRounds = treatmentRounds
        self.treatable = treatable