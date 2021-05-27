# import class file
import connect4_v2_0_classes as c4c
# import function file
import connect4_functions as c4f

# creation of the boolean variable to turn True if a wiining condition is met
x_win = False
o_win = False

# welcome variable
welcome = """
\n\n-------------------------------------------------------------------------------------------
----------------------------------------- WELCOME -----------------------------------------
-------------------------------------------------------------------------------------------\n\n"""
print(welcome)

# gane initialization
print("What game would you like to play?\n\n")

# user have to choose which variation of connect4 to play
list_of_games = ["Connect-4", "PopOut", "Pop 10", "5-in-a-row", "Power Up"]
selection = -1
while selection not in range(len(list_of_games)):
    for game in list_of_games:
        print(str(list_of_games.index(game) + 1) + "- " + game)
    selection = int(input("\n>> ")) - 1

player_1, player_2 = c4f.player_initialization()

# once the user chose the game the specific game sequence starts
if selection == 0:

    # clear the terminal
    c4f.clear()

    # print the definition of the game
    print("""
\n\nConnect Four (also known as Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four,
and Gravitrips in the Soviet Union) is a two-player connection board game, in which the players choose
a color and then take turns dropping colored discs into a seven-column, six-row vertically suspended grid.
The pieces fall straight down, occupying the lowest available space within the column.
The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of
one's own discs. Connect Four is a solved game. The first player can always win by playing the right moves.\n\n""")

    # ask for some specific connect4 game input
    lines = input("Choose the number of lines (4 to 8) -> ")
    columns = input("Choose the number of columns (4 to 7) -> ")

    # initialize the connect4 table
    connect_4 = c4c.TableConnect4(lines, columns)
    table_connect_4 = connect_4.table()
    table_connect_4_dict = connect_4.dict()

    # while loop to keep the users playing as long as the winning condition is not met (add a break if the board
    # is filled and nobody won)
    while (x_win == False) or (o_win ==  False):

        # loop the 2 players
        player_list = [player_1, player_2]
        for player in player_list:
            # clear the terminal
            c4f.clear()

            # call for the connect4 sign
            c4f.connect4_sign()

            # print the connect4 table
            for i in range(lines * 5,-1,-1):
                print(table_connect_4["line_" + str(i)])
            print("\n")

            # print a reminder of each user's checker
            print(player_list[0] + "'s checker is: " + player_1.checker)
            print(player_list[1] + "'s checker is: " + player_2.checker + "\n")

            # player_1 plays
            c4f.play(player, player.checker, table_connect_4, table_connect_4_dict)

    # print the name of the player who won the game
    if x_win == True:
        if player_1.checker == "x":
            print("Congratulation" + player_1.name + "!")
        else:
            print("Congratulation" + player_2.name + "!")
    else:
        if player_1.checker == "o":
            print("Congratulation" + player_1.name + "!")
        else:
            print("Congratulation" + player_2.name + "!")

if selection == 1:

    # clear the terminal
    c4f.clear()

    # print the definition of the game
    print("""
\n\nPopOut starts the same as traditional gameplay, with an empty board and players alternating turns placing 
their own colored discs into the board. During each turn, a player can either add another disc from the top or,
if one has any discs of his or her own color on the bottom row, remove (or "pop out") a disc of one's own color
from the bottom. Popping a disc out from the bottom drops every disc above it down one space, changing their
relationship with the rest of the board and changing the possibilities for a connection.
The first player to connect four of their discs horizontally, vertically, or diagonally wins the game.\n\n""")

if selection == 2:

    # clear the terminal
    c4f.clear()

    # print the definition of the game
    print("""
\n\nBefore play begins, Pop 10 is set up differently from the traditional game. Taking turns, each player places
one of their own color discs into the slots filling up only the bottom row, then moving on to the next row
until it is filled, and so forth until all rows have been filled. Gameplay works by players taking turns
removing a disc of one's own color through the bottom of the board. If the disc that was removed was part
of a four-disc connection at the time of its removal, the player sets it aside out of play and immediately
takes another turn. If it was not part of a "connect four", then it must be placed back on the board through
a slot at the top into any open space in an alternate column (whenever possible) and the turn ends,
switching to the other player. The first player to set aside ten discs of his or her color wins the game.\n\n""")

if selection == 3:

    # clear the terminal
    c4f.clear()

    # print the definition of the game
    print("""
\n\nThe 5-in-a-Row variation for Connect Four is a game played on a 6 high, 9 wide, grid. Hasbro adds two additional
board columns, already filled with player pieces in an alternating pattern, to the left and right sides of their
standard 6 by 7 game board. The game plays similarly to the original Connect Four, except players must now get
five pieces in a row to win. Notice this is still a 42-ply game since the two new columns added to the game
represent twelve game pieces already played, before the start of a game.\n\n""")

if selection == 4:

    # clear the terminal
    c4f.clear()

    # print the definition of the game
    print("""
\n\nIn this variation of Connect Four, players begin a game with one or more specially marked, "Power Checkers" game
pieces, which each player may choose to play once per game. When playing a piece marked with an anvil icon,
for example, the player may immediately pop out all pieces below it, leaving the anvil piece at the bottom
row of the game board. Other marked game pieces include one with a wall icon, allowing a player to play 
a second consecutive non winning turn with an unmarked piece; a "×2" icon, allowing for an unrestricted
second turn with an unmarked piece; and a bomb icon, allowing a player to immediately pop out an opponent's piece.\n\n""")

