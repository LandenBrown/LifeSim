import time

class Event:
    def __init__(self, name, description, eventType, optionOne, optionTwo, optionOneResult, optionTwoResult):
        self.name = name
        self.description = description
        self.eventType = eventType
        self.optionOne = optionOne
        self.optionTwo = optionTwo
        self.optionOneResult = optionOneResult
        self.optionTwoResult = optionTwoResult


    def createEvent(self, x):
        print("A new event has occured!")
        time.sleep(1)
        print(self.description)
        time.sleep(1)
        print("Do you choose to " + self.optionOne + " or " + self.optionTwo + "? Enter '1' or '2'")
        pinput = input()
        if pinput == "1":
            if self.eventType == "Family_Event":
                x.relationships[0].relationshipvalue = x.relationships[0].relationshipvalue - self.optionOneResult
                x.relationships[1].relationshipvalue = x.relationships[1].relationshipvalue - self.optionOneResult
                print("Your relationship with your family has grown! Father: " + str(x.relationships[0].relationshipvalue) + " Mother: " + str(x.relationships[1].relationshipvalue))
            if self.eventType == "Social_Event":
                x.strength = x.strength + 5
        if pinput == "2":
            if self.eventType == "Family_Event":
                x.relationships[0].relationshipvalue = x.relationships[0].relationshipvalue + self.optionTwoResult
                x.relationships[1].relationshipvalue = x.relationships[1].relationshipvalue + self.optionTwoResult
                print("Your relationship with your family has decreased! Father: " + str(x.relationships[0].relationshipvalue) + " Mother: " + str(x.relationships[1].relationshipvalue))
            if self.eventType == "Social_Event":
                x.happiness = x.happiness - 10
        time.sleep(1)