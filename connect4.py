# import sleep to show output for some time period
from time import sleep

# import functions and classes
import connect4_functions as c4f
import connect4_classes as c4c

# clear screen
c4f.clear()

# print welcome function
c4f.welcome()

# sleep for 2 seconds after printing output
sleep(2)

# now call function we defined above
c4f.clear()

# call the connect 4 sign function
c4f.connect4_sign()

# player initialization
print("\n\nThis is a 2 player game, please enter the name of the players.")
player_1 = input("Player 1 name: ")
player_2 = input("player 2 name: ")
print("\n\n")
print(player_1 + ", please choose your piece (x or o):")
print("             \\ /            ---     ")
print("              X      or   (     )   ")
print("             / \\            ---     ")
player_1_piece = input("  --->  ")
while (player_1_piece.lower() != "x"):
    if player_1_piece.lower() == "o":
        player_2_piece = "x"
        break
    print("Please choose x or o only")
    player_1_piece = input("  --->  ")
if player_1_piece.lower() == "x":
    player_2_piece = "o"

c4f.clear()
c4f.connect4_sign()

for i in range(7):
    for j in range(6):
        pass