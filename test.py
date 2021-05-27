# connect4_dict = {}
# for col in range(7):
#     connect4_dict[col] = [[] for j in range(6)]
# print(connect4_dict)
# temp = connect4_dict[2]
# print(temp)
# temp2 = temp[5]
# print(temp2)

# # creation of an empty dict to store all the lines in the connect 4 table
# connect4_table = {}

# # store the bottom line of each row
# for i in range(1,31,5):
#     temp_line = "line_" + str(i)
#     connect4_table[temp_line] = "  |___________|___________|___________|___________|___________|___________|___________|"

# # fill each row
# for i in range(2,31,1):
#     temp_line = "line_" + str(i)
#     if temp_line in connect4_table.keys():
#         continue
#     connect4_table[temp_line] = "  |           |           |           |           |           |           |           |"

# # update each row with the corresponding number
# j = 1
# for i in range(3,31,5):
#     temp_line = "line_" + str(i)
#     temp_string = connect4_table[temp_line]
#     connect4_table[temp_line] = str(j) + temp_string[1:]
#     j += 1

# # add the botom line to add a letter to the corresponding column
# connect4_table["line_0"] = "        A           B           C           D           E           F           G      "

# # print the table with the lines in inversed order
# # for i in range(30,-1,-1):
# #     print(connect4_table["line_" + str(i)])

# dict_A = {"line_1": "    #    ",
#           "line_2": "   # #   ",
#           "line_3": "   # #   ",
#           "line_4": "  #####  ",
#           "line_5": "  #   #  ",
#           "line_6": " #     # ",
#           "line_7": " #     # "}

# dict_B = {"line_1": " ######  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " ######  ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": " ######  "}

# dict_C = {"line_1": "  ###### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " #       ",
#           "line_5": " #       ",
#           "line_6": " #       ",
#           "line_7": "  ###### "}

# dict_D = {"line_1": " #####   ",
#           "line_2": " #    #  ",
#           "line_3": " #     # ",
#           "line_4": " #     # ",
#           "line_5": " #     # ",
#           "line_6": " #    #  ",
#           "line_7": " #####   "}

# dict_E = {"line_1": " ####### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " ####    ",
#           "line_5": " #       ",
#           "line_6": " #       ",
#           "line_7": " ####### "}

# dict_F = {"line_1": " ####### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " ####    ",
#           "line_5": " #       ",
#           "line_6": " #       ",
#           "line_7": " #       "}

# dict_G = {"line_1": "  ###### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " #   ### ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": "  #####  "}

# dict_H = {"line_1": " #     # ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " ####### ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": " #     # "}

# dict_I = {"line_1": "  #####  ",
#           "line_2": "    #    ",
#           "line_3": "    #    ",
#           "line_4": "    #    ",
#           "line_5": "    #    ",
#           "line_6": "    #    ",
#           "line_7": "  #####  "}

# dict_J = {"line_1": "  ###### ",
#           "line_2": "     #   ",
#           "line_3": "     #   ",
#           "line_4": "     #   ",
#           "line_5": " #   #   ",
#           "line_6": " #   #   ",
#           "line_7": "  ###    "}

# dict_K = {"line_1": " #     # ",
#           "line_2": " #    #  ",
#           "line_3": " #   #   ",
#           "line_4": " ####    ",
#           "line_5": " #   #   ",
#           "line_6": " #    #  ",
#           "line_7": " #     # "}

# dict_L = {"line_1": " #       ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " #       ",
#           "line_5": " #       ",
#           "line_6": " #       ",
#           "line_7": " ####### "}

# dict_M = {"line_1": " #     # ",
#           "line_2": " ##   ## ",
#           "line_3": " # # # # ",
#           "line_4": " #  #  # ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": " #     # "}

# dict_N = {"line_1": " #     # ",
#           "line_2": " ##    # ",
#           "line_3": " # #   # ",
#           "line_4": " #  #  # ",
#           "line_5": " #   # # ",
#           "line_6": " #    ## ",
#           "line_7": " #     # "}

# dict_O = {"line_1": "  #####  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " #     # ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": "  #####  "}

# dict_P = {"line_1": " ######  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " ######  ",
#           "line_5": " #       ",
#           "line_6": " #       ",
#           "line_7": " #       "}

# dict_Q = {"line_1": "   ###   ",
#           "line_2": "  #   #  ",
#           "line_3": " #     # ",
#           "line_4": " #     # ",
#           "line_5": " #   # # ",
#           "line_6": "  #   #  ",
#           "line_7": "   ### # "}

# dict_R = {"line_1": " ######  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " ######  ",
#           "line_5": " #   #   ",
#           "line_6": " #    #  ",
#           "line_7": " #     # "}

# dict_S = {"line_1": "  ###### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": "  #####  ",
#           "line_5": "       # ",
#           "line_6": "       # ",
#           "line_7": " ######  "}

# dict_T = {"line_1": " ####### ",
#           "line_2": "    #    ",
#           "line_3": "    #    ",
#           "line_4": "    #    ",
#           "line_5": "    #    ",
#           "line_6": "    #    ",
#           "line_7": "    #    "}

# dict_U = {"line_1": " #     # ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " #     # ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": "  #####  "}

# dict_V = {"line_1": " #     # ",
#           "line_2": " #     # ",
#           "line_3": "  #   #  ",
#           "line_4": "  #   #  ",
#           "line_5": "   # #   ",
#           "line_6": "   # #   ",
#           "line_7": "    #    "}

# dict_W = {"line_1": " #     # ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": " #  #  # ",
#           "line_5": " #  #  # ",
#           "line_6": " # # # # ",
#           "line_7": "  #   #  "}

# dict_X = {"line_1": " #     # ",
#           "line_2": "  #   #  ",
#           "line_3": "   # #   ",
#           "line_4": "    #    ",
#           "line_5": "   # #   ",
#           "line_6": "  #   #  ",
#           "line_7": " #     # "}

# dict_Y = {"line_1": " #     # ",
#           "line_2": "  #   #  ",
#           "line_3": "   # #   ",
#           "line_4": "    #    ",
#           "line_5": "   #     ",
#           "line_6": "  #      ",
#           "line_7": " #       "}

# dict_Z = {"line_1": " ####### ",
#           "line_2": "      #  ",
#           "line_3": "     #   ",
#           "line_4": "    #    ",
#           "line_5": "   #     ",
#           "line_6": "  #      ",
#           "line_7": " ####### "}

# dict_0 = {"line_1": "  #####  ",
#           "line_2": " #    ## ",
#           "line_3": " #   # # ",
#           "line_4": " #  #  # ",
#           "line_5": " # #   # ",
#           "line_6": " ##    # ",
#           "line_7": "  #####  "}

# dict_1 = {"line_1": "    #    ",
#           "line_2": "   ##    ",
#           "line_3": "  # #    ",
#           "line_4": "    #    ",
#           "line_5": "    #    ",
#           "line_6": "    #    ",
#           "line_7": "  #####  "}

# dict_2 = {"line_1": "  #####  ",
#           "line_2": " #     # ",
#           "line_3": " #    #  ",
#           "line_4": "    ##   ",
#           "line_5": "   ##    ",
#           "line_6": "  #      ",
#           "line_7": " ####### "}

# dict_3 = {"line_1": " ######  ",
#           "line_2": "       # ",
#           "line_3": "       # ",
#           "line_4": "   ####  ",
#           "line_5": "       # ",
#           "line_6": "       # ",
#           "line_7": " ######  "}

# dict_4 = {"line_1": " #       ",
#           "line_2": " #       ",
#           "line_3": " #    #  ",
#           "line_4": " ####### ",
#           "line_5": "      #  ",
#           "line_6": "      #  ",
#           "line_7": "      #  "}

# dict_5 = {"line_1": " ####### ",
#           "line_2": " #       ",
#           "line_3": " #       ",
#           "line_4": " ######  ",
#           "line_5": "       # ",
#           "line_6": "       # ",
#           "line_7": " ######  "}

# dict_6 = {"line_1": "   ####  ",
#           "line_2": "  #      ",
#           "line_3": " #       ",
#           "line_4": " # ####  ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": "  #####  "}

# dict_7 = {"line_1": " ####### ",
#           "line_2": " #    #  ",
#           "line_3": "     #   ",
#           "line_4": "   ###   ",
#           "line_5": "   #     ",
#           "line_6": "  #      ",
#           "line_7": " #       "}

# dict_8 = {"line_1": "  #####  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": "  #####  ",
#           "line_5": " #     # ",
#           "line_6": " #     # ",
#           "line_7": "  #####  "}

# dict_9 = {"line_1": "  #####  ",
#           "line_2": " #     # ",
#           "line_3": " #     # ",
#           "line_4": "  ###### ",
#           "line_5": "       # ",
#           "line_6": "       # ",
#           "line_7": "  #####  "}

# import consolemenu as cm

# print("\n\nWhat game would you like to play?\n\n")

# list_of_games = ["Connect-4", "PopOut", "Pop 10", "5-in-a-row", "Power Up"]
# selection = cm.SelectionMenu.get_selection(list_of_games)

# if selection == 0:
#     print("""Connect Four (also known as Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, 
# Drop Four, and Gravitrips in the Soviet Union) is a two-player connection board game, 
# in which the players choose a color and then take turns dropping colored discs into a seven-column, 
# six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available 
# space within the column. The objective of the game is to be the first to form a horizontal, vertical, 
# or diagonal line of four of one's own discs. Connect Four is a solved game. 
# The first player can always win by playing the right moves.""")
# if selection == 1:
#     print("""PopOut starts the same as traditional gameplay, 
# with an empty board and players alternating turns placing 
# their own colored discs into the board. During each turn, a player can either add another disc from the top or,
# if one has any discs of his or her own color on the bottom row, remove (or "pop out") 
# a disc of one's own color from the bottom. Popping a disc out from the bottom drops every disc 
# above it down one space, changing their relationship with the rest of the board and changing the 
# possibilities for a connection. The first player to connect four of their discs horizontally, 
# vertically, or diagonally wins the game.""")
# if selection == 2:
#     print("""Before play begins, Pop 10 is set up differently from the traditional game. 
# Taking turns, each player places one of their own color discs 
# into the slots filling up only the bottom row, 
# then moving on to the next row until it is filled, and so forth until all rows have been filled. 
# Gameplay works by players taking turns removing a disc of one's own color through the bottom of the board.
# If the disc that was removed was part of a four-disc connection at the time of its removal, 
# the player sets it aside out of play and immediately takes another turn. 
# If it was not part of a "connect four", then it must be placed back on the board through 
# a slot at the top into any open space in an alternate column (whenever possible) and the turn ends, 
# switching to the other player. The first player to set aside ten discs of his or her color wins the game.""")
# if selection == 3:
#     print("""The 5-in-a-Row variation for Connect Four is a game played on a 6 high, 9 wide, grid. 
# Hasbro adds two additional board columns, already filled with player pieces in an alternating pattern, 
# to the left and right sides of their standard 6 by 7 game board. 
# The game plays similarly to the original Connect Four, except players must now get five pieces in a row to win. 
# Notice this is still a 42-ply game since the two new columns added to the game represent 
# twelve game pieces already played, before the start of a game.""")
# if selection == 4:
#     print("""In this variation of Connect Four, players begin a game with one or more specially marked, 
# "Power Checkers" game pieces, which each player may choose to play once per game. 
# When playing a piece marked with an anvil icon, for example, 
# the player may immediately pop out all pieces below it, leaving the anvil piece at the bottom row of 
# the game board. Other marked game pieces include one with a wall icon, allowing a player to play 
# a second consecutive non winning turn with an unmarked piece; a "×2" icon, 
# allowing for an unrestricted second turn with an unmarked piece; and a bomb icon, 
# allowing a player to immediately pop out an opponent's piece.""")

# dict_A = {"line_1": "    #    ",
#           "line_2": "   # #   ",
#           "line_3": "   # #   ",
#           "line_4": "  #####  ",
#           "line_5": "  #   #  ",
#           "line_6": " #     # ",
#           "line_7": " #     # "}

# print(dict_A)

alphabet_dict = {"line_1_A": "    #    ",
                 "line_2_A": "   # #   ",
                 "line_3_A": "   # #   ",
                 "line_4_A": "  #####  ",
                 "line_5_A": "  #   #  ",
                 "line_6_A": " #     # ",
                 "line_7_A": " #     # ",

                 "line_1_B": " ######  ",
                 "line_2_B": " #     # ",
                 "line_3_B": " #     # ",
                 "line_4_B": " ######  ",
                 "line_5_B": " #     # ",
                 "line_6_B": " #     # ",
                 "line_7_B": " ######  ",

                 "line_1_C": "  ###### ",
                 "line_2_C": " #       ",
                 "line_3_C": " #       ",
                 "line_4_C": " #       ",
                 "line_5_C": " #       ",
                 "line_6_C": " #       ",
                 "line_7_C": "  ###### ",

                 "line_1_D": " #####   ",
                 "line_2_D": " #    #  ",
                 "line_3_D": " #     # ",
                 "line_4_D": " #     # ",
                 "line_5_D": " #     # ",
                 "line_6_D": " #    #  ",
                 "line_7_D": " #####   ",

                 "line_1_E": " ####### ",
                 "line_2_E": " #       ",
                 "line_3_E": " #       ",
                 "line_4_E": " ####    ",
                 "line_5_E": " #       ",
                 "line_6_E": " #       ",
                 "line_7_E": " ####### ",

                 "line_1_F": " ####### ",
                 "line_2_F": " #       ",
                 "line_3_F": " #       ",
                 "line_4_F": " ####    ",
                 "line_5_F": " #       ",
                 "line_6_F": " #       ",
                 "line_7_F": " #       ",

                 "line_1_G": "  ###### ",
                 "line_2_G": " #       ",
                 "line_3_G": " #       ",
                 "line_4_G": " #   ### ",
                 "line_5_G": " #     # ",
                 "line_6_G": " #     # ",
                 "line_7_G": "  #####  ",

                 "line_1_H": " #     # ",
                 "line_2_H": " #     # ",
                 "line_3_H": " #     # ",
                 "line_4_H": " ####### ",
                 "line_5_H": " #     # ",
                 "line_6_H": " #     # ",
                 "line_7_H": " #     # ",

                 "line_1_I": "  #####  ",
                 "line_2_I": "    #    ",
                 "line_3_I": "    #    ",
                 "line_4_I": "    #    ",
                 "line_5_I": "    #    ",
                 "line_6_I": "    #    ",
                 "line_7_I": "  #####  ",

                 "line_1_J": "  ###### ",
                 "line_2_J": "     #   ",
                 "line_3_J": "     #   ",
                 "line_4_J": "     #   ",
                 "line_5_J": " #   #   ",
                 "line_6_J": " #   #   ",
                 "line_7_J": "  ###    ",

                 "line_1_K": " #     # ",
                 "line_2_K": " #    #  ",
                 "line_3_K": " #   #   ",
                 "line_4_K": " ####    ",
                 "line_5_K": " #   #   ",
                 "line_6_K": " #    #  ",
                 "line_7_K": " #     # ",

                 "line_1_L": " #       ",
                 "line_2_L": " #       ",
                 "line_3_L": " #       ",
                 "line_4_L": " #       ",
                 "line_5_L": " #       ",
                 "line_6_L": " #       ",
                 "line_7_L": " ####### ",

                 "line_1_M": " #     # ",
                 "line_2_M": " ##   ## ",
                 "line_3_M": " # # # # ",
                 "line_4_M": " #  #  # ",
                 "line_5_M": " #     # ",
                 "line_6_M": " #     # ",
                 "line_7_M": " #     # ",

                 "line_1_N": " #     # ",
                 "line_2_N": " ##    # ",
                 "line_3_N": " # #   # ",
                 "line_4_N": " #  #  # ",
                 "line_5_N": " #   # # ",
                 "line_6_N": " #    ## ",
                 "line_7_N": " #     # ",

                 "line_1_O": "  #####  ",
                 "line_2_O": " #     # ",
                 "line_3_O": " #     # ",
                 "line_4_O": " #     # ",
                 "line_5_O": " #     # ",
                 "line_6_O": " #     # ",
                 "line_7_O": "  #####  ",

                 "line_1_P": " ######  ",
                 "line_2_P": " #     # ",
                 "line_3_P": " #     # ",
                 "line_4_P": " ######  ",
                 "line_5_P": " #       ",
                 "line_6_P": " #       ",
                 "line_7_P": " #       ",

                 "line_1_O": "   ###   ",
                 "line_2_O": "  #   #  ",
                 "line_3_O": " #     # ",
                 "line_4_O": " #     # ",
                 "line_5_O": " #   # # ",
                 "line_6_O": "  #   #  ",
                 "line_7_O": "   ### # ",

                 "line_1_R": " ######  ",
                 "line_2_R": " #     # ",
                 "line_3_R": " #     # ",
                 "line_4_R": " ######  ",
                 "line_5_R": " #   #   ",
                 "line_6_R": " #    #  ",
                 "line_7_R": " #     # ",

                 "line_1_S": "  ###### ",
                 "line_2_S": " #       ",
                 "line_3_S": " #       ",
                 "line_4_S": "  #####  ",
                 "line_5_S": "       # ",
                 "line_6_S": "       # ",
                 "line_7_S": " ######  ",

                 "line_1_T": " ####### ",
                 "line_2_T": "    #    ",
                 "line_3_T": "    #    ",
                 "line_4_T": "    #    ",
                 "line_5_T": "    #    ",
                 "line_6_T": "    #    ",
                 "line_7_T": "    #    ",

                 "line_1_U": " #     # ",
                 "line_2_U": " #     # ",
                 "line_3_U": " #     # ",
                 "line_4_U": " #     # ",
                 "line_5_U": " #     # ",
                 "line_6_U": " #     # ",
                 "line_7_U": "  #####  ",

                 "line_1_V": " #     # ",
                 "line_2_V": " #     # ",
                 "line_3_V": "  #   #  ",
                 "line_4_V": "  #   #  ",
                 "line_5_V": "   # #   ",
                 "line_6_V": "   # #   ",
                 "line_7_V": "    #    ",

                 "line_1_W": " #     # ",
                 "line_2_W": " #     # ",
                 "line_3_W": " #     # ",
                 "line_4_W": " #  #  # ",
                 "line_5_W": " #  #  # ",
                 "line_6_W": " # # # # ",
                 "line_7_W": "  #   #  ",

                 "line_1_X": " #     # ",
                 "line_2_X": "  #   #  ",
                 "line_3_X": "   # #   ",
                 "line_4_X": "    #    ",
                 "line_5_X": "   # #   ",
                 "line_6_X": "  #   #  ",
                 "line_7_X": " #     # ",

                 "line_1_Y": " #     # ",
                 "line_2_Y": "  #   #  ",
                 "line_3_Y": "   # #   ",
                 "line_4_Y": "    #    ",
                 "line_5_Y": "   #     ",
                 "line_6_Y": "  #      ",
                 "line_7_Y": " #       ",

                 "line_1_Z": " ####### ",
                 "line_2_Z": "      #  ",
                 "line_3_Z": "     #   ",
                 "line_4_Z": "    #    ",
                 "line_5_Z": "   #     ",
                 "line_6_Z": "  #      ",
                 "line_7_Z": " ####### "}

def sign_editor(word):
    for i in range(1, 8):
        word_to_print=""
        for letter in word.upper():
            word_to_print += alphabet_dict["line_" + str(i) + "_" + letter]
        print(word_to_print)

sign_editor("beber")