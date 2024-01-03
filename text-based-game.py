import re
from pyfiglet import Figlet

light = True
location = None
orcs = False

class Character:
    inventory = ()
    def __init__(self, name):
        self.name = name

class Room:
    def __init__(self, name, description, item=False):
        self.name = name
        self.description = description
        self.item = item

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

    def go(self, direction):
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
        continue
    else:
        print(
            "The heavy stone doors open slowly, revealing nothing but dense darkness. Do you enter?"
        )
        while True:
            answer = input("> ").strip().lower()
            if answer != "yes":
                break
        break
    
while True:
    location.enter()
    command = input("\n> ").strip().lower()
    location.actions(command)






