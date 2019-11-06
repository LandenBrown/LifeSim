import random
from src import IllnessClass
from src import BirthDefects
from src import Relationship
from src import EventsClass
from src import Job
from src import Property

# name collections
####Male
firstNameCollectionMale = ["Trevor", "Landen", "Alex", "Brandon", "Cory", "Joshua", "Barry", "Mike", "Michael", "Jerry",
                           "Greg", "Aaron", "James", "David", "Gary", "Geary",
                           "Justin", "Carl", "Karl", "Adolf", "Benito", "Harry", "Max", "Colby", "Eric", "Matthew",
                           "Tim", "Timothy", "Adam", "AJ", "Jackson", "Jack", "Tony",
                           "George", "William", "Will", "Grant", "Alexander", "Allen", "Jim", "Dwight", "Ashton"]

lastNameCollection = ["Alvarez", "Brown", "Smith", "Cole", "Marsden", "Wise", "Wiseman", "Fitz", "Fitzgerald", "Fors",
                      "Four", "Fore", "Red", "Prost", "Jackson", "Mussolini", "Killin",
                      "Ashely", "Donnay", "Smith", "Cal", "Derr", "Machammer", "Dawi", "Hinchora", "Irons", "Dehmani",
                      "Gambler", "Crickette", "Stone", "Allan", "Williams", "Ashton",
                      "Madison"]

####Female
firstNameCollectionFemale = ["Tiffany", "Tricia", "Beth", "Bethany", "Ashely", "Haley", "Ash", "Amy", "Kindred",
                             "Leanna", "Ashlyn", "Emily", "Alex", "Alexandria", "Taylor", "Tay",
                             "Brittany", "Kayla", "Kayli", "Rebecca", "Beka", "Mary", "Kaylin", "Carley", "Sarah",
                             "Leya", "Sandra", "Sunny", "Harman", "Bella", "Maddie", "Madison",
                             "Jacky", "Jacuqeline", "Jaya", "Alyssa", "Victoria", "Vicky", "Zimma", "Ashton"]




#Property Collections - Each one of theses needs to be added to the proplist in getRandomPropertyList
#name, sqf, value, growth, amountOwed, isPaidOff, happinessDecay
withParents_Property = Property.Property("With Parents", 0, 0, 0, 0, 0, 0)
homeless_Property = Property.Property("Homeless", 0, 0, 0, 0, True, 5)
homesteadApartments_Property = Property.Property("Homestead Apartments - 1 Bedroom", 900, 850, 0, 0, 0, 0)
homesteadApartments2_Property = Property.Property("Homestead Apartments - 2 Bedroom", 1200, 975, 0, 0, 0, 0)
hiddenSpringsHouse_Property = Property.Property("Hidden Springs House", 1800, 175000, 1, 175000, False, 0)
hiddenSpringsHouse2_Property = Property.Property("Hideen Springs PentHouse", 2700, 290000, 1, 290000, False, 0)
hiddenSpringsHouse3_Property = Property.Property("Hidden Springs Mansion", 5900, 850000, 1, 850000, False, 0)
blackWaterHouse_Property = Property.Property("Blackwater House", 2000, 200000, 1, 200000, False, 0)
blackWaterHouse2_Property = Property.Property("Blackwater Manor", 2300, 275000, 1, 275000, False, 0)


# illness collections - name, healthDecay, happinessDecay, cureChance, cureCost
# "You are suffering from a" -----
aHeadache = IllnessClass.Illness("A Headache", 0, 1, 100, 50)
skinWarts = IllnessClass.Illness("Skin Warts", 0, 2, 98, 30)
skinInfection = IllnessClass.Illness("A Skin Infection", 1, 1, 40, 300)
commonCold = IllnessClass.Illness("The Common Cold", 1, 0, 95, 90)
theFlu = IllnessClass.Illness("Influenza", 2, 1, 90, 150)
pinWorms = IllnessClass.Illness("Pinworms", 1, 3, 80, 20)
ringWorm = IllnessClass.Illness("Ring Worm", 2, 2, 85, 200)
chickenPox = IllnessClass.Illness("Chicken Pox", 3, 1, 90, 50)
cancer = IllnessClass.Illness("Cancer", 8, 4, 10, 6500)
# ---------
illnessCollection = [commonCold, chickenPox, cancer]

# Birth Defects collections
cleftLip = BirthDefects.BirthDefect("Cleft Lip", 0, .5, True, 4000, 3)
downSyndrome = BirthDefects.BirthDefect("Down Syndrome", 1, random.randint(0, 5), False, None, None)
# ---------
birthDefectCollection = [cleftLip, downSyndrome]

# Car condition collections
# event collections


#FAMILY EVENTS ######
familyevent_lowsev = EventsClass.Event("Parental Discipline", "You broke the rules", "Family_Event", "Comply", "Rebel", 3, 2)
familyevent_medsev = EventsClass.Event("Parental Discipline", "You broke the rules", "Family_Event", "Comply", "Rebel", "Option one result", "Option two result")
familyevent_highsev = EventsClass.Event("Parental Discipline", "You broke the rules", "Family_Event", "Comply", "Rebel", "Option one result", "Option two result")
#SOCIAL  EVENTS ######
socialevent_lowsev = EventsClass.Event("Bully", "Someone is bullying you", "Social_Event", "Retaliate", "Ignore", 3, 3)

allEvents = [familyevent_lowsev,familyevent_medsev,familyevent_highsev]
lowSevEvents = [familyevent_lowsev, socialevent_lowsev]
medSevEvents = []
highSevEvents = []

# Relationships collections
father = Relationship.Relationship("", 50, "", "Father", "")
mother = Relationship.Relationship("", 50, "", "Mother", "")
significantOther = Relationship.Relationship("", 50, "", "Significant Other", None)
scandalPerson = Relationship.Relationship("", 50, "", "Mistress", None)


# education Collections


########Jobs collections
#(self, name, salary, educationRequired, intelligenceRequired, looksRequired, healthRequired, promotionJob, promotionTime)

#Fast Food jobs
fastFood_cook = Job.Job("Fast Food Cook", 6000, None, 0, 0, 20, None, 0)
fastFood_cashier = Job.Job("Fast Food Cashier", 7500, None, 30, 0, 20, None, 0)
fastFood_manager = Job.Job("Fast Food Manager", 12000, None, 38, 0, 20, None, 0)
fastFood_owner = Job.Job("Fast Food Restaurant Owner", 20000, None, 0, 0, 20,  None, 0)

#Political Jobs
political_governor = Job.Job("Governor", 35000, "Bachelors in Social Science", 0, 70, 20,  None, 0)
political_senator = Job.Job("Senator", 55000, "Masters in Social Science", 0, 70, 20,  None, 0)
political_congressman = Job.Job("Congressman", 80000, "Masters in Social Science", 0, 75, 20, None, 0)
politial_potus = Job.Job("President of the United States", 200000, "Masters in Social Science", 0, 90, 40, None, 0)

#IT Jobs
it_helpdesk = Job.Job("IT Help Desk", 14000, None, 65, 0, 20,  None, 0)
it_administrator = Job.Job("IT Administrator", 30000, None, 70, 0, 20,  None, 0)
it_architect = Job.Job("IT Architect", 50000, None, 70, 0, 20,  None, 0)
it_manager = Job.Job("IT Manager", 75000, "Bachelors in Computer Science", 70, 0, 20,  None, 0)
it_ciso = Job.Job("Chief Information Security Officer", 150000, "Masters in Computer Science", 75, 0, 20,  None, 0)

#Taxi
taxi_driver = Job.Job("Taxi Driver", 10000, None, 0, 0, 20,  None, 0)
taxi_dispatch = Job.Job("Taxi Dispatch", 15000, None, 30, 0, 20,  None, 0)
taxi_owner = Job.Job("Taxi Company Owner", 45000, None, 40, 0, 20,  None, 0)

#Scientist
scientist_labtech = Job.Job("Research Lab Tech", 40000, "Bachelors in Chemistry", 60, 0, 50,  None, 0)
scientist_analyst = Job.Job("Research Analyst", 55000, "Bachelors in Chemistry", 65, 0, 50,  None, 0)
scientist_labmanager = Job.Job("Research Lab Manager", 95000, "Masters in Chemistry", 70, 0, 50, None, 0)
scientist_labowner = Job.Job("Research Lab Owner", 150000, "Masters in Chemistry", 70, 0, 50,  None, 0)


def setJobPromotions():
    #fast food
    fastFood_cook.promotionJob = fastFood_cashier
    fastFood_cashier.promotionJob = fastFood_manager
    fastFood_manager.promotionJob = fastFood_owner
    #political
    political_governor.promotionJob = political_senator
    political_senator.promotionJob = political_congressman
    political_congressman.promotionJob = politial_potus
    #it
    it_helpdesk.promotionJob = it_administrator
    it_administrator.promotionJob = it_architect
    it_architect.promotionJob = it_manager
    it_manager.promotionJob = it_ciso
    #taxi
    taxi_driver.promotionJob = taxi_dispatch
    taxi_dispatch.promotionJob = taxi_owner
    #science
    scientist_labtech.promotionJob = scientist_analyst
    scientist_analyst.promotionJob = scientist_labmanager
    scientist_labmanager.promotionJob = scientist_labowner

def getRandomJobList():
    # select 5 jobs, 4 random but always have fast food starter available
    # aids in "Job Hunt" feeling
    joblist = [fastFood_cashier, fastFood_manager, fastFood_owner, politial_potus, political_congressman, political_senator,
               political_governor, it_ciso, it_manager, it_architect, it_helpdesk, it_administrator, taxi_owner, taxi_dispatch,
               taxi_driver, scientist_labowner, scientist_labmanager, scientist_analyst, scientist_labtech]
    jobcount = len(joblist)
    jobarray = []
    while len(jobarray) != 4:
        randomjob = random.randint(1, jobcount)
        jobarray.append(joblist[randomjob-1])
    jobarray.append(fastFood_cook)
    return jobarray

def getRandomPropertyList():
    # select 5 jobs, 4 random but always have fast food starter available
    # aids in "Job Hunt" feeling
    proplist = [blackWaterHouse2_Property, blackWaterHouse_Property, homesteadApartments_Property,
                hiddenSpringsHouse_Property, hiddenSpringsHouse2_Property, hiddenSpringsHouse3_Property,
                homesteadApartments2_Property] # Fill this array with the all properties that could ever be available
    propcount = len(proplist)
    proparray = []
    while len(proparray) != 4:
        randomprop = random.randint(1, propcount)
        proparray.append(proplist[randomprop-1])
    proparray.append(homesteadApartments_Property)   #Edit this to add the permanent property
    return proparray




# Create Female Names
def getRandomFirstNameFemale():
    arrayCount = len(firstNameCollectionFemale)
    randomArray = random.randint(1, arrayCount)
    name = firstNameCollectionFemale[randomArray - 1]
    return name


def getRandomFirstNameMale():
    arrayCount = len(firstNameCollectionMale)
    randomArray = random.randint(1, arrayCount)
    name = firstNameCollectionMale[randomArray - 1]
    return name


def getRandomLastName():
    arrayCount = len(lastNameCollection)
    randomArray = random.randint(1, arrayCount)
    name = lastNameCollection[randomArray - 1]
    return name


# Get Ilnesses
def getRandomIllness():
    arrayCount = len(illnessCollection)
    randomArray = random.randint(1, arrayCount)
    illness = illnessCollection[randomArray - 1]
    return illness

def getLowSevEvent(i):
    arrayCount = len(lowSevEvents)
    randomArray = random.randint(1, arrayCount)
    event = lowSevEvents[randomArray-1]
    event.createEvent(i)


def getBirthDefects():
    getdefect1 = False
    getdefect2 = False
    defectlist = []
    contract = random.randint(1, 100)
    if contract > 5:  # will change to greater number for a smaller chance
        getdefect1 = True
    contract2 = random.randint(1, 100)
    # if contract2 > 5: # will make this an even smaller nunber  DISABLING THIS SO YOU CAN ONLY GET 1 BIRTH DEFECT.
    # getdefect2 = True
    if getdefect1 == True:
        randomdefect = random.randint(0, (len(birthDefectCollection) - 1))
        defectlist.append(birthDefectCollection[randomdefect])
        print("You contracted a birth defect")
    else:
        print("No birth defects")
    # if getdefect2 == True:
    # randomdefect = random.randint(0, (len(birthDefectCollection) - 1))
    # defectlist.append(birthDefectCollection[randomdefect])
    # print("You contracted a birth defect")
    return defectlist


def getInitialRelationships(player):
    player.relationships = [father, mother]
    fatherLast = getRandomLastName()
    motherLast = getRandomLastName()
    areMarried = random.randint(1, 2)
    if areMarried == 1:
        player.relationships[0].name = getRandomFirstNameMale() + " " + fatherLast
        player.relationships[1].name = getRandomFirstNameFemale() + " " + motherLast
        gender = random.randint(1, 2)
        if gender == 1:
            player.name = getRandomFirstNameMale()
        if gender == 2:
            player.name = getRandomFirstNameFemale()
        whichParents = random.randint(1, 2)
        if whichParents == 1:
            player.name = player.name + " " + fatherLast
        if whichParents == 2:
            player.name = player.name + " " + motherLast

        parentStatus = random.randint(1, 3)
        if parentStatus == 1:
            player.relationships[0].status = "Low Income"
            player.relationships[1].status = "Low Income"
            print("You are born by a split couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")
        if parentStatus == 2:
            player.relationships[0].status = "Mid Income"
            player.relationships[1].status = "Mid Income"
            print("You are born by a split couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")
        if parentStatus == 3:
            player.relationships[0].status = "High Income"
            player.relationships[1].status = "High Income"
            print("You are born by a split couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")
    if areMarried == 2:
        lastName = getRandomLastName()
        player.relationships[0].name = getRandomFirstNameMale() + " " + lastName
        player.relationships[1].name = getRandomFirstNameFemale() + " " + lastName
        gender = random.randint(1, 2)
        if gender == 1:
            player.name = getRandomFirstNameMale()
        if gender == 2:
            player.name = getRandomFirstNameFemale()
        player.name = player.name + " " + lastName
        parentStatus = random.randint(1, 3)
        if parentStatus == 1:
            player.relationships[0].status = "Low Income"
            player.relationships[1].status = "Low Income"
            print("You are born by a married couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")
        if parentStatus == 2:
            player.relationships[0].status = "Mid Income"
            player.relationships[1].status = "Mid Income"
            print("You are born by a married couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")
        if parentStatus == 3:
            player.relationships[0].status = "High Income"
            player.relationships[1].status = "High Income"
            print("You are born by a married couple: " + player.relationships[0].name + " and " + player.relationships[
                1].name + ", They are a " + player.relationships[0].status + " family.")

    return player.relationships
