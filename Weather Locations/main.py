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

with open('restaurantstats.json', 'r') as file:
    restaurant = json.load(file)

allLocations = {"A1": "Restaurant", "A2": "Toy Shop", "B1": "Metro", "B2": "Street"}
locationToFile = {"Restaurant": restaurant}
currentLocation = "Restaurant"

def FindLocation(location):
    return locationToFile.get(location)

def Actions(location):
    move = False
    steal = False
    fight = False
    search = False
    scraps = False
    spot = location.get("Spots")[0]
    print("===============")
    print("You are at " + spot)
    print("You can : ")
    if len(location.get("Spots")) > 1:
        print("*Move Between Spots")
        for i in location.get("Spots"):
            print("- " + i)
        move = True
    for i in location.get(spot).get("Actions"):
        print("*" + i)

Actions(FindLocation(currentLocation))