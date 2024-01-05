import re
from pyfiglet import Figlet

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
            location = Hall()
            return print("You have lit the torch, now you can see what's around you... sort of.")
        elif (item == 'torch') and light:
            return print('The torch is already lit.')

class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item

    # Default methods for the rooms
    def enter(self):
        return print(f"\nYou have entered the {self.name}. \n{self.description}") 
    
    def look(self):
        return print(self.description)
    def search(self):
        if not self.item:
            return "There's nothing else of interest around here"
        
    
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
        else:
            print("You cannot go that way")

class Hall(Room):
    def __init__(self):
        super().__init__(
            name= "Hall",
            description= "A small room gives you the quietest and gloomiest welcome, a deathly silence. The door is closed behind you, there is no turning back, you are alone in total darkness...",
            item= "torch" 
        )
        if light :
            self.description = "In the dim light of the torch, you can see that the hall divides into several paths: a narrow passage to the left, a wide corridor to the right, and stairs leading down to the forward end."
    
    def actions(self, input):
        
        if input.startswith("go"):
            location.go(input[3:])
        if input == "search":
            location.search()
        if input.startswith("use"):
            character.use(input[4:])

    def go(self, direction):
        global light
        if not light:
            print("You cannot see where to go in this darkness")
        else:
            global location
            if direction == "right":
                location = great_hall
                
            elif direction == "left":
                pass
            elif direction == "forward":
                pass
            else:
                print("You cannot go that way")
    def search(self):
        if self.item == None:
            print("There is nothing here of interest.")
        else:
            character.inventory.append(self.item)
            print(f"You stepped on something... You found a {self.item} lying in the ground, next to your feet.\n*'{self.item}' was added to your invetory*")
            self.item = None


    
character = Character("Robin")    
great_hall = GreatHall()
hall = Hall()

# Game starts at the Hall
location = hall
print(location)
f = Figlet(font='slant')
print(f.renderText('Lost in Moria'))
print(
    "Welcome to Lost in Moria, a text-based adventure game built while I was learning Python.\nAs a text-based adventure, you're expected to enter what your character will do in the form of text. \nThis game accepts some words like 'go', 'search', 'look' and others related to the items you might find during your adventure.\nThis symbol ('> ') indicates when you are expected to enter a command, if you don't see this symbol it probably means that the program is loading or the game is finished.\nHave fun and good luck!"
    )
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

while True:
    location.enter()
    command = input("\n> ").strip().lower()
    location.actions(command)






