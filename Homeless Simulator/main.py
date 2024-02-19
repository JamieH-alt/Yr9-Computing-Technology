import random
import time
import json

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


with open('restaurantstats.json', 'r') as file:
    restaurant = json.load(file)

allLocations = {"A1": "Restaurant", "A2": "Toy Shop", "B1": "Metro", "B2": "Street"}
locationToFile = {"Restaurant": restaurant}
currentLocation = "Restaurant"
currentIndex = "A1"
spot = 0

playerStats = {"Health": 10, "Hunger": 25, "Money": 0, "Inventory": []}
worldStats = {"Time": 8, "TrueTime": 0}

def FindLocation(location):
    return locationToFile.get(location)

def trueTime():
    if worldStats['Time'] == 24:
        worldStats['Time'] = 0

def Actions(location):
    time.sleep(1)
    ### Variables
    global spot
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
    print("*Inventory")
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
            for i in playerStats['Inventory']:
                if itemSelect in i.keys():
                    if i.get(itemSelect) == "food":
                        print(f"You ate {itemSelect}!")
                        print("It gave you one hunger!")
                        playerStats['Hunger'] += 1
                        print(f"You now have {playerStats['Hunger']} Hunger")
        return
    return

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
