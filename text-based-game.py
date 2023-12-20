from typing import Type

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
    
    
room = GreatHall()
print(room.enter())



