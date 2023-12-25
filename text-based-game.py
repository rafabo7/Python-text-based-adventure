light = False
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
        return f"You have entered the {self.name}. \n{self.description}"
    
    def look(self):
        return self.description
    def search(self):
        if self.item == False:
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
            item= True 
        )
        if light :
            self.description = "In the dim light of the torch, you can see that the hall divides into several paths: a narrow passage to the left, a wide corridor to the right, and stairs leading down to the forward end."
    
    def go(self, direction):
        global location
        if direction == "right":
            location = great_hall
            return location
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
location.action("go right")
print(location)    
print(location.enter())



