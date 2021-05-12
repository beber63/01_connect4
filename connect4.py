# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# import functions and classes
import connect4_functions
import connect4_classes

# print out some text
print("\n\n-------------------------------------------------------------------------------------------")
print("----------------------------------------- WELCOME -----------------------------------------")
print("-------------------------------------------------------------------------------------------\n\n")
# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
clear()

# call the connect 4 sign function
connect4_sign()

print("This is a 2 player game, please enter the name of the players.")
player_1 = input("Player 1 name: ")
player_2 = input("player 2 name: ")
print("\n\n")
print(player_1 + ", please choose your piece (x or o):")
print("             \\ /            ---     ")
print("              X      or   (     )   ")
print("             / \\            ---     ")
player_1_piece = input("  --->  ")
clear()
