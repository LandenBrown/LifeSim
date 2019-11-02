import random
from src import Collections
import time



class Person:
    def __init__(self, name, profession, intelligence, money, car, property, mother,
                 father, siblings, happiness, location, age, currenteducation, education,
                 health, illness, cureAttemptByTurn, looks, actionLimit, currentActions, healthDecay,
                 intelligenceDecay, birthDefects, relationships, isHealthy, isHealthyTurns, eventCooldown,
                 strength, strengthDecay, happinessDecay, job, debug, timeAtJob, timeAtJobHolder):
        self.name = name
        self.profession = profession
        self.intelligence = intelligence
        self.money = money
        self.car = car
        self.property = property
        self.mother = mother
        self.father = father
        self.siblings = siblings
        self.happiness = happiness
        self.location = location
        self.age = age
        self.currenteducation = currenteducation
        self.education = education
        self.health = health
        self.illness = illness
        self.cureAttemptByTurn = cureAttemptByTurn
        self.looks = looks
        self.actionLimit = actionLimit
        self.currentActions = currentActions
        self.healthDecay = healthDecay
        self.intelligenceDecay = intelligenceDecay
        self.birthDefects = birthDefects
        self.relationships = relationships
        self.isHealthy = isHealthy
        self.isHealthyTurns = isHealthyTurns
        self.eventCooldown = eventCooldown
        self.strength = strength
        self.strengthDecay = strengthDecay
        self.happinessDecay = happinessDecay
        self.job = job
        self.debug = debug
        self.timeAtJob = timeAtJob
        self.timeAtJobHolder = timeAtJobHolder


    def calculateHealth(self):
        if self.isHealthyTurns > 0:
            self.isHealthy = True
            self.isHealthyTurns = self.isHealthyTurns - 1
        else:
            self.isHealthy = False
        if self.illness == None:
            healthChance = random.randint(1, 80)
            if self.isHealthy == False:
                if healthChance > self.health:
                    self.illness = Collections.getRandomIllness()
                    print("You have contracted " + self.illness.name)
                    self.health = self.health - self.healthDecay
        else:
            self.health = self.health - self.illness.healthDecay
            self.happiness = self.happiness - self.illness.happinessDecay
            if self.health <= 0:
                print("You have died")
                exit()
        if self.happiness <= 0:
            print("Your life is ruined by bad decisions, you feel everyone is out to get you, you can't get a break, but you'll make one. You kill yourself.")
            exit()

    def calculateIntelligence(self):
        if self.age < 16:
            self.intelligenceDecay = 0
        elif self.age >= 16:
            self.intelligenceDecay = 1
        self.intelligence = self.intelligence - self.intelligenceDecay

    def calculateBirthDefects(self):
        if len(self.birthDefects) == 1:
            self.healthDecay = self.healthDecay - self.birthDefects[0]
        elif len(self.birthDefects) == 2:
            self.healthDecay = self.healthDecay - (self.birthDefects[0] + self.birthDefects[1])

    def checkAge(self):
        self.actionLimit = 5
        if self.age >= 5:
            print("You just started elementary school.")
            self.currenteducation = "Elementary School"
            self.actionLimit = 5
        elif self.age >= 11:
            print("You just started middle school")
            self.currenteducation = "Middle School"
            self.actionLimit = 6
        elif self.age >= 14:
            print("You just started highschool")
            self.currenteducation = "High School"
            self.actionLimit = 7
        elif self.age >= 18:
            print("You just graduated highschool. You can now enroll in college or join the military.")
            self.currenteducation = "Not Enrolled"
            self.actionLimit = 8
        elif self.age >= 22:
            print("You just finished undergrad school, you can go to grad school.")

    def visitDoctorIllness(self):
        if self.cureAttemptByTurn > 0:
            self.cureAttemptByTurn = self.cureAttemptByTurn - 1
            print("you only have " + str(self.cureAttemptByTurn) + " attempts left, now!")
            if self.age < 18:
                if self.relationships[0].status == "Low Income":
                    doctorchance = random.randint(1, 5)
                    if doctorchance == 1:
                        print("Your parents decide to take you to treatment for " + self.illness.name)
                        print("It costed them $" + str(self.illness.cureCost))
                        curechance = random.randint(1, 100)
                        if curechance < self.illness.cureChance:
                            print("You have cured " + self.illness.name)
                            self.illness = None
                        else:
                            print(
                                "The doctors provided the best treatment possible, but they were unable to come to a cure.")
                            # Add doctor variation of skill and cost
                            # add the amount of treatments needs to cure a specific disease/illness
                    else:
                        print(
                            "Your parents could not afford to take you to the doctor. Low Income! They are devastated.")
                if self.relationships[0].status == "Mid Income":
                    doctorchance = random.randint(1, 3)
                    if doctorchance == 1:
                        print("Your parents decide to take you to treatment for " + self.illness.name)
                        print("It costed them $" + str(self.illness.cureCost))
                        curechance = random.randint(1, 100)
                        if curechance < self.illness.cureChance:
                            print("You have cured " + self.illness.name)
                            self.illness = None
                        else:
                            print(
                                "The doctors provided the best treatment possible, but they were unable to come to a cure.")
                            # Add doctor variation of skill and cost
                            # add the amount of treatments needs to cure a specific disease/illness
                    else:
                        print(
                            "Your parents could not afford to take you to the doctor. Mid Income! They are devastated.")
                if self.relationships[0].status == "High Income":
                    doctorchance = random.randint(1, 2)
                    if doctorchance == 1:
                        print("Your parents decide to take you to treatment for " + self.illness.name)
                        print("It costed them $" + str(self.illness.cureCost))
                        curechance = random.randint(1, 100)
                        if curechance < self.illness.cureChance:
                            print("You have cured " + self.illness.name)
                            self.illness = None
                        else:
                            print(
                                "The doctors provided the best treatment possible, but they were unable to come to a cure.")
                            # Add doctor variation of skill and cost
                            # add the amount of treatments needs to cure a specific disease/illness
                    else:
                        print(
                            "Your parents could not afford to take you to the doctor. High Income!They are devastated.")
            elif self.age >= 18:
                print("It will cost " + str(self.illness.cureCost) + " to cure " + self.illness.name)
                print("Would you like to attempt to cure? y/n")
                pinput = input()
                if pinput == "y":
                    if self.money >= self.illness.cureCost:
                        curechance = random.randint(1, 100)
                        if curechance < self.illness.cureChance:
                            print("You have cured " + self.illness.name)
                    else:
                        print("You do not have the money to go through treatment")
                        # add potential financing
        else:
            print("You don't have any more cure attempts this turn! Hope ya don't die!")
        time.sleep(1)

    def useAction(self):
        self.currentActions = self.currentActions - 1
        print("You used an action")
        print("you have " + str(self.currentActions) + " actions left out of " + str(self.actionLimit))

    def calculateStatDependencies(self):
        # no idea where to start here

        # Ensuring that decay doesn't enter negative nunbers
        if self.happinessDecay < 0:
            self.happinessDecay = 0
        if self.strengthDecay < 0:
            self.strengthDecay
        if self.healthDecay < 0:
            self.healthDecay
        if self.intelligenceDecay < 0:
            self.intelligenceDecay = 0

        self.happinessDecay = (self.property.happinessDecay)
        self.happiness = self.happiness - self.happinessDecay
        
