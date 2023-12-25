import re

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
    actions = ("search", "look")
    def __init__(self):
        super().__init__(
            name= "Hall",
            description= "A small room gives you the quietest and gloomiest welcome, a deathly silence. The door is closed behind you, there is no turning back, you are alone in total darkness...",
            item= "torch" 
        )
        if light :
            self.description = "In the dim light of the torch, you can see that the hall divides into several paths: a narrow passage to the left, a wide corridor to the right, and stairs leading down to the forward end."
    
    def go(self, direction):
        if not light:
            print("You cannot see where to go in this darkness")
        else:
            global location
            if direction == "right":
                location = great_hall
                print(location.enter())
                
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
print("Welcome to he game. Lets check if this is working. Good luck")
while True:
    location.enter()
    command = input("\n> ").strip().lower()
    if command.startswith("go"):
        action, direction = command.split(" ")
        location.go(direction)
    elif command in location.actions:
        pass






