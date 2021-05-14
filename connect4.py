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
print(player_1 + ", please choose your checker type (x or o):")
print("             \\ /            ---     ")
print("              X      or   (     )   ")
print("             / \\            ---     ")
player_1_checker = input("  --->  ")
while (player_1_checker.lower() != "x"):
    if player_1_checker.lower() == "o":
        player_2_checker = "x"
        break
    print("Please choose x or o only")
    player_1_checker = input("  --->  ")
if player_1_checker.lower() == "x":
    player_2_checker = "o"

c4f.clear()
c4f.connect4_sign()

connect4_dict = {}
for col in ["A", "B", "C", "D", "E", "F", "G"]:
    connect4_dict[col] = [[] for j in range(6)]

connect4_table = {}
lines_list = ["line_" + str(i) for i in range(1, 31)]
for line in lines_list:
    pass #connect4_table[line] = 

line_30 = "  |           |           |           |           |           |           |           |"
line_29 = "  |           |           |           |           |           |           |           |"
line_28 = "6 |           |           |           |           |           |           |           |"
line_27 = "  |           |           |           |           |           |           |           |"
line_26 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_25 = "  |           |           |           |           |           |           |           |"
line_24 = "  |           |           |           |           |           |           |           |"
line_23 = "5 |           |           |           |           |           |           |           |"
line_22 = "  |           |           |           |           |           |           |           |"
line_21 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_20 = "  |           |           |           |           |           |           |           |"
line_19 = "  |           |           |           |           |           |           |           |"
line_18 = "4 |           |           |           |           |           |           |           |"
line_17 = "  |           |           |           |           |           |           |           |"
line_16 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_15 = "  |           |           |           |           |           |           |           |"
line_14 = "  |           |           |           |           |           |           |           |"
line_13 = "3 |           |           |           |           |           |           |           |"
line_12 = "  |           |           |           |           |           |           |           |"
line_11 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_10 = "  |           |           |           |           |           |           |           |"
line_9 = "  |           |           |           |           |           |           |           |"
line_8 = "2 |           |           |           |           |           |           |           |"
line_7 = "  |           |           |           |           |           |           |           |"
line_6 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_5 = "  |           |           |           |           |           |           |           |"
line_4 = "  |           |           |           |           |           |           |           |"
line_3 = "1 |           |           |           |           |           |           |           |"
line_2 = "  |           |           |           |           |           |           |           |"
line_1 = "  |___________|___________|___________|___________|___________|___________|___________|"
line_0 = "        A           B           C           D           E           F           G      "