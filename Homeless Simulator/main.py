import random
import time
import json
import os

print("██╗░░██╗░█████╗░███╗░░░███╗███████╗██╗░░░░░███████╗░██████╗░██████╗")
print("██║░░██║██╔══██╗████╗░████║██╔════╝██║░░░░░██╔════╝██╔════╝██╔════╝")
print("███████║██║░░██║██╔████╔██║█████╗░░██║░░░░░█████╗░░╚█████╗░╚█████╗░")
print("██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░██║░░░░░██╔══╝░░░╚═══██╗░╚═══██╗")
print("██║░░██║╚█████╔╝██║░╚═╝░██║███████╗███████╗███████╗██████╔╝██████╔╝")
print("╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═════╝░╚═════╝░")
print("")
print("░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░")
print("██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝")
print("░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print("██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print("╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")

print("")
print(" --- Disclaimer ---")
print("This game is meant to be educational and show the troubles homeless people have to face,")
print("This game is meant to encourage positive action and charity. And promote awareness of homelessness")
print(" --- Disclaimer ---")
accept = input("Are you ok with the contents of this game? (y or n) ")
if accept == "y":
    accepted = True
else:
    accepted = False
    exit()

projectVersion = "0.0.1"

baseFiles = {}

allLocations = {}
locationToFilePath = {}
currentLocation = "DevTesting"
currentIndex = ""
spot = 0
saveName = ""
forts = {"Restaurant": {"Behind Restaurant": 1}}

playerStats = {"Health": 10, "Hunger": 25, "Money": 0, "Inventory": []}
worldStats = {"Time": 8, "TrueTime": 0}

def basicLoadSystem():
    print("Do you already have a save?")
    saveYes = input("(y or n) ")
    if saveYes == "y":
        global saveName
        saveName = input("What is the name of your save? ")
        with open (saveName + ".json", 'r') as savedata:
            save = json.load(savedata)
            global worldStats
            global playerStats
            global currentLocation
            global spot
            global currentIndex
            global baseFiles
            global projectVersion
            if projectVersion != save.get("ProjectVersion"):
                print("Invalid Save File! (Project Version Is Different To Current Version!)")
                exit()
            worldStats = save.get("worldStats")
            playerStats = save.get("playerStats")
            currentLocation = save.get("CurrentLocation")
            spot = save.get("CurrentSpot")
            currentIndex = save.get("CurrentIndex")
            baseFiles = save.get("BaseFiles")
            with open('locationsSettings.json', "r+") as locationSettings:
                locationData = json.load(locationSettings)
                for i in locationData:
                    curDataSet = locationData.get(i)
                    locationToFilePath[curDataSet.get("Name")] = curDataSet.get("FileName")
                    allLocations[curDataSet.get("Index")] = curDataSet.get("Name")
    else:
        with open('locationsSettings.json', "r+") as locationSettings:
            locationData = json.load(locationSettings)
            for i in locationData:
                curDataSet = locationData.get(i)
                if curDataSet.get("DefaultLocation") == True:
                    print("Loading Up!")
                    currentLocation = curDataSet.get("Name")
                    currentIndex = curDataSet.get("Index")
                locationToFilePath[curDataSet.get("Name")] = curDataSet.get("FileName")
                allLocations[curDataSet.get("Index")] = curDataSet.get("Name")
        print("Starting a new game without loading variables")

def FindLocation(location):
    with open('locationsSettings.json', "r+") as file:
        loaded = json.load(file)
        return loaded.get(location)

def trueTime():
    if worldStats['Time'] == 24:
        worldStats['Time'] = 0
def Actions(location):
    time.sleep(1)
    ### Variables
    global spot
    global currentLocation
    global currentIndex
    move = False
    steal = False
    fight = False
    search = False
    scraps = False
    completed = False
    ### Spot Setting
    if spot == 0:
        spot = location.get("Spots")[0]
    ### Listing Everything
    print("===============")
    print(f"It's currently {worldStats.get('Time')}:00 Oclock!")
    print("You are at " + spot)
    print("You can : ")
    if len(location.get("Spots")) > 1:
        print("*Move Between Spots")
        for i in location.get("Spots"):
            print("- " + i)
        move = True
    for i in location.get(spot).get("Actions"):
        print("*" + i)
    if baseFiles[location.get("Name")][spot]["Fort"]["Tier"] >= 1:
        print("*Sleep")
    print("*Inventory")
    print("*Travel")
    print("*Exit (Saves!)")
    action = input("What would you like to do? ")
    print("====================================")
    ### Movement Section
    if action.lower() == "move":
        moveTo = input("Where would you like to go? ")
        for spotLoco in location.get("Spots"):
            if moveTo == spotLoco:
                playerStats['Hunger'] -= 1
                print("That costed 1 hunger!")
                print(f"You now have {playerStats['Hunger']} Hunger")
                completed = True
                worldStats['Time'] += 1
                worldStats['TrueTime'] += 1
                trueTime()
                print(f"Its now {worldStats['Time']}:00 Oclock!")
                spot = spotLoco
                return
        if completed == False:
            print("Thats not a location!")
            return
    elif action.lower() == "beg":
        if "Beg" in location.get(spot).get("Actions"):
            beg = location.get(spot).get("Beg")
            print("You begged!")
            begKey = random.choice(list(beg.keys()))
            print(f"You went from {playerStats['Money']} to {playerStats['Money'] + beg.get(begKey)} dollars!")
            print(begKey)
            playerStats['Money'] += beg.get(begKey)
            print("But that action cost you 1 hunger!")
            playerStats['Hunger'] -= 1
            print(f"You now have {playerStats['Hunger']} Hunger!")
            worldStats['Time'] += 1
            worldStats['TrueTime'] += 1
            trueTime()
            print(f"Its now {worldStats['Time']}:00 Oclock!")
            return
    elif action.lower() == "search":
        if "Search" in location.get(spot).get("Actions") and "Dumpster" in location.get(spot):
            print("You search the nearby Dumpster!")
            dumpster = location.get(spot).get("Dumpster")
            dumpsterKey = random.choice(list(dumpster.keys()))
            dumpsterValue = dumpster.get(dumpsterKey)
            print(f"You found {dumpsterKey}!")
            if isinstance(dumpsterValue, int):
                print(f"You went from {playerStats['Money']} to {playerStats['Money'] + dumpsterValue} dollars!")
                playerStats['Money'] += dumpsterValue
            else:
                playerStats['Inventory'].append({dumpsterKey: dumpsterValue})
            playerStats['Hunger'] -= 0.5
            print(f"You now have {playerStats['Hunger']} Hunger!")
            worldStats['Time'] += 1
            worldStats['TrueTime'] += 1
            trueTime()
            print(f"Its now {worldStats['Time']}:00 Oclock!")
        else:
            print("You can't do that here!")
        return
    elif action.lower() == "inventory":
        print(f"You have")
        print(f"*{playerStats['Money']} Dollars")
        print(f"*{playerStats['Health']} Health")
        print(f"*{playerStats['Hunger']} Hunger")
        print("These are all the items you have!")
        for i in playerStats['Inventory']:
            for i2 in i.keys():
              print(f"*{i2}")
        invUse = input("Would you like to use any items (y or n)? ")
        if invUse == "y":
            itemSelect = input("Which Item Would you like to use? ")
            doneUsage = False
            for i in playerStats['Inventory']:
                if itemSelect in i.keys():
                    if i.get(itemSelect) == "food" and doneUsage == False:
                        doneUsage = True
                        print(f"You ate {itemSelect}!")
                        print("It gave you one hunger!")
                        playerStats['Hunger'] += 1
                        print(f"You now have {playerStats['Hunger']} Hunger")
                        playerStats['Inventory'].remove(i)
                    elif i.get(itemSelect) == "structure" and doneUsage == False:
                        doneUsage = True
                        if location.get(spot).get("Fort").get("Buildable") == True:
                            fortTier = location.get(spot).get("Fort").get("Tier")
                            if fortTier == 0:
                                print("Constructing A Tier 1 Fort!")
                                playerStats['Inventory'].remove(i)
                                global forts
                                forts[currentLocation][spot] = 1
                                print("Fort Constructed!")
                        else:
                            print(location.get(spot).get("Fort").get("Reason"))
        return
    elif action.lower() == "travel":
        print("You can travel to : ")
        locationData = []
        with open("locationsSettings.json", "r+") as locationSettings:
            locationData = json.load(locationSettings)
            for i in locationData:
                print(f"*{locationData.get(i).get("Name")}")
        whereto = input("Where would you like to go? ")
        if whereto == locationData.get(i).get("Name"):
            currentLocation = locationData.get(i).get("Name")
            currentIndex = locationData.get(i).get("Index")
            spot = 0
            playerStats['Hunger'] -= 1
            print("That costed 1 hunger!")
            print(f"You now have {playerStats['Hunger']} Hunger")
            completed = True
            worldStats['Time'] += 1
            worldStats['TrueTime'] += 1
            trueTime()
            print(f"Its now {worldStats['Time']}:00 Oclock!")
        else:
            print("Thats not a location!")

    elif action.lower() == "sleep":
        print("You are now going to sleep for 4 hours!")
        worldStats['Time'] += 4
        worldStats['TrueTime'] += 4
        trueTime()
        print(f"Its now {worldStats['Time']}:00 Oclock!")
        playerStats['Hunger'] -= 6 / baseFiles[location.get("Name")][spot]["Fort"]["Tier"]
        print(f"That costed you {6 / baseFiles[location.get("Name")][spot]["Fort"]["Tier"]} hunger!")
        print(f"You're now at {playerStats['Hunger']} hunger!")
        print("You restored some health!")
        newHealth = random.randrange(0, 6)
        playerStats['Health'] += newHealth
        print(f"You gained {newHealth} Health and are now at {playerStats['Health']}")
    elif action.lower() == "exit":
        endGame()
    return

def basicSavingSystem():
    with open("locationsSettings.json", "r+") as locationSettings:
        locationData = json.load(locationSettings)
        for i in locationData:
            baseFiles[locationData.get(i).get("Name")] = locationData.get(i)
            if locationData.get(i).get("Name") in forts:
                fortDataset = list(forts.get(locationData.get(i).get("Name")).keys())
                baseFiles[locationData.get(i).get("Name")][fortDataset[0]]["Fort"]["Tier"] = forts.get(locationData.get(i).get("Name")).get(fortDataset[0])
    saveName = input("What is the name of your save? ")
    print("Formating Save Data")
    saveStats = {"worldStats": worldStats,
                 "ProjectVersion": projectVersion,
                 "playerStats": playerStats,
                 "CurrentLocation": currentLocation,
                 "CurrentSpot": spot,
                 "CurrentIndex": currentIndex,
                 "BaseFiles": baseFiles
                 }
    saveFormat = json.dumps(saveStats, indent=2)
    if os.path.isfile('./' + saveName + ".json"):
        with open(saveName + ".json", "r+") as savefile:
            savefile.truncate(0)
            savefile.write(saveFormat)
    else:
        with open(saveName + ".json", "x") as savefile:
            savefile.write(saveFormat)

def endGame():
    shouldSave = input("Would you like to save? (y or n) ")
    if shouldSave == "y":
        basicSavingSystem()
        exit()
    else:
        print("Good Bye!")
        exit()

basicLoadSystem()

while playerStats['Hunger'] > 0:
    if accepted == True and playerStats['Health'] > 0:
        Actions(FindLocation(currentLocation))
    elif playerStats['Health'] <= 0:
        print("You died!")
        exit()
    else:
        print("Goodbye! ... No Refunds")
        exit()

if playerStats['Hunger'] <= 0:
    print("You starved to death!")
    exit()
