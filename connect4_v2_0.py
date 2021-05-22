# import class file
import connect4_v2_0_classes as c4c

# welcome variable
welcome = """\n\n-------------------------------------------------------------------------------------------
----------------------------------------- WELCOME -----------------------------------------
-------------------------------------------------------------------------------------------\n\n"""

# player initialization
print("\n\nThis is a 2 player game:")
player_1_name = input("Player 1 name: ")
player_1_checker = input(player_1_name + ", please choose your checker (X or O):")
while player_1_checker.lower() != "x":
    if player_1_checker.lower() == "o":
        player_2_checker = "x"
        break
    print("Please choose X or O only")
    player_1_checker = input("  --->  ")
if player_1_checker.lower() == "x":
    player_2_checker = "o"
player_1 = c4c.Player(player_1_name, player_1_checker)

player_2_name = input("Player 2 name: ")
player_2 = c4c.Player(player_2_name, player_2_checker)
