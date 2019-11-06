from threading import Thread
import random, time, math
from src import PersonClass, Collections
import tkinter

globalInput = 0
debugToggle = True
nextTurn = "d"
eventCD = 0



def idleTime():
    time.sleep(1)



person1 = PersonClass.Person(None, None, None, None, None, None, None, None, None,
                             None, None, None, None, None, None, None, None, None,
                             None, None, 0, 1, [], [], False, 0, 0, 0, 0, 0, None,
                             False, None, None)

def debugCode(x):
    if debugToggle:
        print("DEBUG: " + str(x));
        nextTurn = "d"
        person1.debug = True


def createCharacter(x):
    x.relationships = Collections.getInitialRelationships(x)
    debugCode("Name: " + x.name)
    x.happiness = random.randint(50, 100)
    debugCode("Happiness: " + str(x.happiness))
    x.age = 0
    x.money = 0
    x.intelligence = random.randint(15, 100)
    debugCode("Intelligence: " + str(x.intelligence))
    x.health = random.randint(1, 100)
    debugCode("Health: " + str(x.health))
    x.actionLimit = 5
    debugCode("ActionLimit: " + str(x.actionLimit))
    x.currentActions = x.actionLimit
    debugCode(("Current actions match ActionLimit"))
    x.birthDefects = Collections.getBirthDefects()
    x.looks = 0
    x.eventCooldown = 90
    return x


def checkEventStatus(x):
    if debugToggle != True:
        debugCode("Checking event status...")
        print("Event Cooldown: " + str(x.eventCooldown))
        newnum = random.randint(1, 100)
        x.eventCooldown = x.eventCooldown - 1
        print("New Event: " + str(newnum))
        if newnum > x.eventCooldown:
            debugCode("Generating new event...")
            eventSeverity = random.randint(1, 100)
            if eventSeverity > 0 and eventSeverity < 66:
                debugCode("Generating new low severity event...")
                print("We are now starting a low sev event.")
                Collections.getLowSevEvent(x)
                x.eventCooldown = 90
            if eventSeverity > 66 and eventSeverity < 90:
                debugCode("Generating new medium severirty event...")
                print("We are now starting a med sev event.")
                x.eventCooldown = 95
            if eventSeverity > 90:
                debugCode("Generating new high severity event....")
                print("We are now starting a high sev event.")
                x.eventCooldown = 99
        if newnum < x.eventCooldown:
            print("Event cooldown is greater than new event")
    else:
        debugCode("Skipping event creation...")
        x.eventCooldown = 10000


def showActionMenu(character):
    character.checkAge()
    pinput = "some sheet"
    educationchoices = None
    if character.job == None:
        jobstatus = "explore job opportunities"
    else:
        jobstatus = "work"

    # THIS IS A STRANGE FUNCTION BECUASE I'M NOT REALLY SURE WHICH OF MY CURRENT DEFINED ENGINE PROCESSES IT SHOULD
    # BELONG TO........ FLESHING OUT EDUCATION CHOICES
    if character.currenteducation == "Elementary School":
        educationchoices = ["Play with your friends", "Memorize your homework"]
    if character.currenteducation == "Middle School":
        educationchoices = ["Flirt and talk with friends", "Study for class"]
    if character.currenteducation == "High School":
        educationchoices = ["Skip class and play sports", "Focus on your studies"]
    if character.currenteducation == None:
        educationchoices = None

    # FLESHING OUT HEALTH CHOICES
    if character.illness != None and character.cureAttemptByTurn > 0:
        illnesschoice = "Type 'doctor' to see the doctor"
    else:
        illnesschoice = None
    # FLESHING OUT LIFE CHOICES - THIS IS GOING TO NEED SOME SERIOUS WORK
    if character.age < 16:
        lifechoices = ["Play with your father", "Play with your mother",
                       "Take your vitamins"]  # will have to determine which of these are available given on family death etc - UGH!
    if character.age > 16:
        lifechoices = ["Spend time with your father", "Spend time with your mother",
                       "Meal Prep & Eat Healthy"]  # will have to determine which of these are available given on family death etc - UGH!
    # FLESHING OUT JOB CHOICES
    if character.age >= 16:
        jobchoices = "Type 'job' to " + jobstatus
    else:
        jobchoices = None

    # FLESHING OUT PROPERTY CHOICES
    if character.age >= 16:
        propertychoices = "Type 'prop' to see your property options"
    else:
        propertychoices = None


        ############## STARTING WHILE LOOP
    while pinput != "exit":
        print("Actions menu: (type 'exit' to leave this menu)")

        # Getting availability of action menu   ####### THIS WILL CAUSE CRASHING IF NOT PLANNED WELL

        if educationchoices != None:
            print("Type 'ed' for your Education Choices")
        if illnesschoice != None:
            print(illnesschoice)
        if jobchoices != None:
            print(jobchoices)
        if propertychoices != None:
            print(propertychoices)
        print("Type 'life' for your Life Choices")


        ###    REQURING USER INPUT NOW
        pinput = input()
        ####### SEPARATING FLOW

        if pinput == "ed":
            print("Would you like to " + educationchoices[0] + " or " + educationchoices[1] + "? Enter '1' or '2'")
            pinput2 = input()
            if pinput2 == "1":
                print("You decided to " + educationchoices[0])
                character.looks = character.looks + 1
                character.useAction()
            if pinput2 == "2":
                print("You decide to " + educationchoices[1])
                character.intelligence = character.intelligence + 1
                character.useAction()

        if pinput == "doctor":
            character.visitDoctorIllness()
            character.useAction()

        if pinput == "life":
            print("Would you like to " + lifechoices[0] + ", " + lifechoices[1] + " or " + lifechoices[
                2] + "? Enter '1','2', or '3'")
            pinput2 = input()
            if pinput2 == "1":
                print("You decided to " + lifechoices[0])
                character.relationships[0].relationshipvalue = character.relationships[0].relationshipvalue + 5
                idleTime()
                print("You now have " + str(character.relationships[0].relationshipvalue) + "/100 relationship points")
                character.useAction()
                idleTime()
            if pinput2 == "2":
                print("You decided to " + lifechoices[1])
                character.relationships[1].relationshipvalue = character.relationships[1].relationshipvalue + 5
                idleTime()
                print("You now have " + str(character.relationships[1].relationshipvalue) + "/100 relationship points")
                character.useAction()
                idleTime()
            if pinput2 == "3":
                print("You decide to " + lifechoices[2])
                character.isHealthyTurns = character.isHealthyTurns + 4
                print("You are now healthy")
        if pinput == "job":
            character.useAction()
            jobinput = ""
            if jobstatus == "explore job opportunities":
                debugCode("Job status is explore job opportunities")
                openjobs = Collections.getRandomJobList()
                while jobinput != "exit":
                    idleTime()
                    print("Open Jobs: 1." + openjobs[0].name + " 2." + openjobs[1].name + " 3." + openjobs[2].name
                      + " 4." + openjobs[3].name + " 5." + openjobs[4].name)
                    print("Enter 1-5 to view more about these jobs, enter 'exit' to exit")
                    jobinput = input()
                    def jobDecision(x):
                        print("A " + openjobs[x].name + " requires:")
                        if isinstance(openjobs[x].educationRequired, str):
                            print("A " + openjobs[x].educationRequired)
                        if openjobs[x].intelligenceRequired != None:
                            print("Intelligence: " + str(openjobs[x].intelligenceRequired))
                        if openjobs[x].looksRequired != None:
                            print("Looks: " + str(openjobs[x].looksRequired))
                        if openjobs[x].healthRequired != None:
                            print("Health: " + str(openjobs[x].healthRequired))
                        if character.education == openjobs[x].educationRequired:
                            debugCode("Passed education requirement")
                            idleTime()
                            if character.intelligence >= openjobs[x].intelligenceRequired:
                                debugCode("Passed intelligence requirement")
                                idleTime()
                                if character.health >= openjobs[x].healthRequired:
                                    debugCode("Passed health requirement")
                                    if character.looks >= openjobs[x].looksRequired:
                                        debugCode("Passed looks requirement")
                                        print("You qualify, would you like to apply for this job? Type 'yes' or 'no'")
                                        applyinput = input()
                                        if applyinput == "yes":
                                            gotjob = random.randint(1, 3)
                                            if gotjob == 3:
                                                print("""The company has decided not to move forward in the interview process. 
                                                Good luck on future attempts buddy""")
                                            else:
                                                print("Congratulations! They would like to offer you the job making " + str(openjobs[x].salary * 2) + " a year!")
                                                character.job = openjobs[x]
                                                character.timeAtJob = 0
                                        if applyinput == "no":
                                            print("You chose not to apply")
                                    else:
                                        print("You don't have the required social skills for this position!")
                                else:
                                    print("You aren't healthy enough for this position!")
                            else:
                                print("You don't have the required intelligence for this position!")
                        else:
                            print("You don't have the required education for this position!")

                    if jobinput == "1":
                        jobDecision(0)
                    if jobinput == "2":
                        jobDecision(1)
                    if jobinput == "3":
                        jobDecision(2)
                    if jobinput == "4":
                        jobDecision(3)
                    if jobinput == "5":
                        jobDecision(4)
                    break


            if jobstatus == "work":
                workstatus = ""
                while workstatus != "exit":
                    print("Would you like to 1. Ask for a promotion 2. Check how many months you've worked at your current job 3. Quit your job")
                    workstatus = input()
                    if workstatus == "1":
                        idleTime()
                        print("You walk into your boss' office and sit down with confidence and take a seat")
                        idleTime()
                        print("You explain to him that you have been doing alot more than your peers lately and would like to be recognized for it")
                        if character.job.promotionJob is not None:
                            if character.timeAtJob >= character.job.promotionJob.promotionTime:
                                idleTime()
                                print("'All Right' your boss says. You've been here awhile and you're doing great things. I'm promoting you to "
                                    + character.job.promotionJob.name + ". Your new salary will be $" + str(character.job.promotionJob.salary) + ".")
                                character.job = character.job.promotionJob
                                character.timeAtJob = 0
                                break
                            else:
                                idleTime()
                                print("'Look, you just haven't been here long enough for me to justify a promotion now.' Your boss says.")
                                break
                        else:
                            print("You are currently in the highest position in this career field!")
                            break
                    if workstatus == "2":
                        print("You have worked at your current job for " + str(character.timeAtJob) + " months.")
                        idleTime()
                        break
                    if workstatus == "3":
                        print("You walk into your boss' office with a scowl and smirk. You're tired of his shit and this dead end job.")
                        idleTime()
                        print("Sir, suck my ass. I quit")
                        idleTime()
                        print("Stunned, your boss stands up from his desk with a bewildered look on his face. You promptly walk out, never to return")
                        character.job = None
                        character.timeAtJob = 0
                        idleTime()
                        break


        if pinput == "prop":
            character.useAction()
            print("You have chosen to view property options")
            debugCode("Generating property list...")
            availableproperty = Collections.getRandomPropertyList()
            debugCode("Property list generated...")
            propinput = ""
            while propinput != "exit":
                idleTime()
                print("Open Jobs: 1." + availableproperty[0].name + " 2." + availableproperty[1].name + " 3." + availableproperty[2].name
                      + " 4." + availableproperty[3].name + " 5." + availableproperty[4].name)
                print("Enter 1-5 to view more about these properties, enter 'exit' to exit")
                propinput = input()
                def propertyDecision(x):
                    print("This home is being sold for: $" + str(availableproperty[x].value))
                    print("The square footage is: " + str(availableproperty[x].sqf))
                    print("The average bi-annual growth is: " + str(availableproperty[x].growth) + "%")
                    idleTime()
                    print("Would you like to purchase this home? Enter 'yes' or 'no'")
                    buyornot = input()
                    if buyornot == 'yes':
                        if character.money >= availableproperty[x].value:
                            print("Congratulations on your new home!")
                            character.property = availableproperty[x]
                        else:
                            print("I'm sorry Sir, you don't seem to have the funds to purchase this home... Think smaller?")
                    idleTime()

                if propinput == '1':
                    propertyDecision(0)
                if propinput == '2':
                    propertyDecision(1)
                if propinput == '3':
                    propertyDecision(2)
                if propinput == '4':
                    propertyDecision(3)
                if propinput == '5':
                    propertyDecision(4)



        if pinput == "exit":
            debugCode("I am supposed to exit")
        break


def checkActions(character):
    print("Please enter 'm' to see your current available actions, otherwise enter 'd' to continue.")
    pinput = input()
    if pinput == "m":
        showActionMenu(character)
    # person1.visitDoctor()
def checkJobDetails(character):
    if character.job != None:
        character.timeAtJob = character.timeAtJob + 1
        character.money = character.money + character.job.salary
        debugCode("Time at job increased and character paid salary")
def checkPropertyDetails(character):
    debugCode("Nothing")
    if character.age < 18:
        character.property = Collections.withParents_Property
    if character.age == 18:
        print("Your parents have kicked you out. Now would be a good time to visit a property manager.")
        character.property = Collections.homeless_Property
        debugCode("Set property to homeless!################################")
    if character.property != None:
        character.money = character.money - character.property.value




def intervalCheck(character):
    debugCode("Calculating Health")
    if debugToggle:
        character.health = 100
        character.intelligence = 100
        character.happiness = 100
    character.cureAttemptByTurn = 3
    character.calculateHealth()
    character.calculateIntelligence()
    character.checkAge()
    checkEventStatus(character)
    checkJobDetails(character)
    checkPropertyDetails(character)
    character.calculateStatDependencies()
    character.calculateRelationshipValues()
    character.currentActions = character.actionLimit
    debugCode("Conducting calculations and examinations......")
    if person1.illness != None:
        print("You are currently suffering from " + person1.illness.name)
    if character.currenteducation != None:
        print("You are currently in: " + character.currenteducation)
    else:
        print("You are currently not enrolled In any education program.")


debugCode("testing debug code...")

##Starting Eninge

debugCode("Starting LifeSim engine...")

currentMonth = 0

debugCode("Testing create character....")
createCharacter(person1)
Collections.setJobPromotions()
print("Welcome to life: " + person1.name)

debugCode("Starting while Loop........")

# intervalCheck(person1)

while globalInput != "2":
    print("6 MONTHS HAS GONE BY.....")
    print("Age: " + str(person1.age))
    print("Health: " + str(person1.health))
    print("Intelligence: " + str(person1.intelligence))
    print("Actions: " + str(person1.currentActions) + "/" + str(person1.actionLimit))
    print("Healthy: " + str(person1.isHealthy))
    print("Money: " + str(person1.money))
    print("Happiness: " + str(person1.happiness))
    # intervalCheck(person1)
    # checkActions(person1)
    if person1.currentActions > 0:
        print("Please enter 'm' to see your current available actions, otherwise enter " + nextTurn + " to continue.")
    if person1.currentActions <= 0:
        print("Please enter " + nextTurn + " to continue")
    pinput = input()
    if pinput == "m" and person1.currentActions > 0:
        showActionMenu(person1)
    if pinput == "m" and person1.currentActions <= 0:
        print("You are out of actions for this turn!")
    if pinput == nextTurn:
        person1.age = person1.age + .5
        intervalCheck(person1)
        continue
