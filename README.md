# Python-text-based-adventure

Welcome to **Lost in Moria**.
This is a text-based game, so there are no graphics and it is played by just typing (the right) text.

This is a non-profit for fun project I am building while diving into my knowledge of Python. It is built with object oriented programming principles in mind.

Enjoy it, let me know what I can improve and have fun!

*Technical information*
The code uses classes for different elements like characters, rooms, items etc.,
The classes and the game itself are in the same file because it is expected to be submited as the final project of CS50's Introduction to Progamming with Python.
There is a superclass called Room, which contains default behaviours for the other rooms.
The other rooms are children of Room(), overriding its methods according to their needs.
In this first version, the game itself is an infinite while loop, depending on the player's command, the class methods are called. These methods make changes to the game's global variables, such as location, light or orcs, and are expected to print out the resulting situations for the player's choices.

REQUISITES
Python 3.4 or higher
figlet library
