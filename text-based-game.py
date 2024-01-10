# import re
from pyfiglet import Figlet
import sys

light = False
location = None
orcs = False

class Character:
    inventory = []
    def __init__(self, name):
        self.name = name

    def use(self, item, inventory=inventory):
        global light
        # Checking for item and item in the inventory
        if not item:
            return print("Use what?")
        elif item not in inventory:
            return print(f"You don't have a {item}")
        
        # Torch funcionality
        if (item == 'torch') and (light == False):
            light = True
            global location
            location.description = location.lightdescription
            return print("You have lit the torch, now you can see what's around you... sort of.")
        elif (item == 'torch') and light:
            return print('The torch is already lit.')

class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item

    # Default methods for the rooms
        
    def actions(self, input):
        
        try:
            if input == 'look':
                location.look()
            elif input.startswith("go"):
                location.go(input[3:])
            elif input == "search":
                location.search()
            elif input.startswith("use"):
                character.use(input[4:])
            elif input == "open":
                location.open()
            else: 
                print("Now is not the time to be doing that")
        except AttributeError:
            return print("Now is not the time to be doing that.")
        

    def enter(self):
        if isinstance(location, TreasureDoor):
            return print(f"You stand before a {location.description}")
        return print(f"\nYou have entered the {self.name}. \n{self.description}") 
    
    def look(self):
        return print(self.description)
    # This search() method is called when the childs objects are initiate with item = False
    def search(self):
        return print("There's nothing of interest around here")


class Hall(Room):
    def __init__(self):
        super().__init__(
            name= "Hall",
            description= "A small room gives you the quietest and gloomiest welcome, a deathly silence. The door is closed behind you, there is no turning back, you are alone in total darkness...",
            item= "torch" 
        )
        self.lightdescription = "In the dim light of the torch, you can see that the hall divides into several paths: a narrow passage to the left, a wide corridor to the right, and stairs leading down to the forward end."
    
    

    def go(self, direction):
        global light
        global location
        if not light:
            print("You cannot see where to go in this darkness")
        elif not direction:
            print("Go where?")
        else:
            if direction == "right":
                location = great_hall
                location.enter()
            elif direction == "left" or direction == "forward":
                print(f"You try to go {direction} but it seems the path has collapsed...")
            else:
                print("You cannot go that way")
    def search(self):
        if not self.item:
            print("There is nothing of interest around here.")
        else:
            character.inventory.append(self.item)
            print(f"You stepped on something... You found a {self.item} lying in the ground, next to your feet.\n*'{self.item}' was added to your invetory*")
            self.item = False        
    
class GreatHall(Room):
    def __init__(self):
        super().__init__(
            name="Great Hall",
            description="Ahead of you stretches a great hall filled with columns so high that the light from your torch cannot reach their ends. The floor is littered with broken weapons and debris, the remnants of a great battle...",
            item=True
        )
    def go(self, direction):
        global location
        if direction == "back":
            location = hall
            location.enter()
        elif direction == "left" or direction == "right":
            print(f"You walk a few steps to the {direction} but the hall doesn't seem to have an end through this way")
        elif direction == "forward":
            if orcs == True:
                location = treasure_door
                location.enter()
            else:
                print(f"You walk a few steps {direction} but the hall doesn't seem to have an end through this way")

    def search(self):
        if not self.item:
            return print("There is nothign of interest around here")
        
        print("As you sift through the rubbish around you, you stumble upon a large suit of metal armour that is rolling across the floor, making a deafening noise in the stillness of the hall.\n")
        print("Someone or something has awaken and it comes for you. The drums rumble... dumdamdum... dumdadum...\n")
        global orcs
        orcs = True
        answer = input("What will you do?\n\n> ").lower().strip()

        if answer != "hide":
            print("\nThat did not work at all. A huge horde of orcs captured you and dragged you into the depths. No one will ever hear from you again...\nYou are indeed lost in Moria.")
            sys.exit("\n\nCongratulations! You have discovered the ending 1/2!\n\n")
        else:
            self.item = False
            return print("You manage to hide under the rubble as a horde of orcs passes by from the forward end of the hall, raging and roaring. They run and run, lost in the dark vastness of the Great Hall.\n")
        
class TreasureDoor(Room):
    def __init__(self):
        super().__init__(
            name="Wooden Door",
            description="a sturdy wooden door with a large iron knocker, full of beautiful engravings."
            )
    def open(self):
        print(f"You take the knob of the door and start pulling. You pull and pull until a crack in the door opens and you can fit through.")
        while True:
            answer = input("Do you enter?\n\n> ")
            if answer == "yes":
                print("\nYou pass through the small opening in the door and enter a darker room with a strong smell of metal. Lifting the torch, you see that it is full of treasure, which is now yours as the orcs have abandoned the scene.\nUnfortunately our greed prevents you from leaving the treasures you can't carry, and you decide to stay and watch over them... forever.\nYou are indee lost in Moria.")
                sys.exit("\n\nCongratulations! You have found the ending 2/2.\n\n")
            elif answer == "no":
                location.enter()
                break
    
    def go(self, direction):
        global location
        if direction == "forward":
            print("There is a door in front of you...")
        elif direction == "left" or direction == "right":
            print(f"You walk a few steps {direction} but the hall doesn't seem to have an end through this way")
        elif direction == "back":
            location = great_hall
            print("You are back to the Great Hall")


        




# Declaring the rooms       
hall = Hall()
great_hall = GreatHall()
treasure_door = TreasureDoor()

# Introduction: title, tutorial and first riddle
f = Figlet(font='slant')
print(f.renderText('Lost in Moria'))
print(
    "Welcome to Lost in Moria, a text-based adventure game built while I was learning Python.\nAs a text-based adventure, you're expected to enter what your character will do in the form of text.  \nThis game accepts simple comands like 'go', 'search', 'look', 'use + (item)' and others related to the situations that might occur. If there is a typo in your command, the game will most likely not understand it.\nThis symbol ('> ') indicates when you are expected to enter a command, if you don't see this symbol it probably means that the program is loading or the game is finished.\nHave fun and good luck!"
    )
print("You can start writing your characters name, for example...")
character = Character(input("\n> "))
print(f"\nWelcome {character.name}.")
print(
    "You stand before the famous Doors of Durin... they appear to be locked, but an Elvish engraving presents you with a well-known riddle:"
)
print(
    "Pedo mellon a minno... Say friend an enter..."
)

while True:
    answer = input("> ").strip().lower()
    if answer != "mellon":
        print(
            "Nothing happens... the wind howls..."
        )
        continue
    else:
        print(
            "The heavy stone doors open slowly, revealing nothing but dense darkness. Do you enter?"
        )
        break
while True:
    answer = input("> ").strip().lower()
    if answer == "yes":
        break
    else:
        print(
            "Fine... whenever you are ready..."
        )

# The main game
# The game starts at the hall
location = hall



while True:
    # Main loop: print the room with enter() and wait for user input
    location.enter()
    # Secondary loop: all the action the action that happens in a room. Breaks with the correct 'go (direction)'
    while True:
        command = input("\n> ").strip().lower()
        location.actions(command)






