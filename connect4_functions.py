import connect4_v2_0_classes as c4c
from os import system, name

alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_string = "0123456789"
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

numbers_dict = {"line_1_0": "  #####  ",
                "line_2_0": " #    ## ",
                "line_3_0": " #   # # ",
                "line_4_0": " #  #  # ",
                "line_5_0": " # #   # ",
                "line_6_0": " ##    # ",
                "line_7_0": "  #####  ",

                "line_1_1": "    #    ",
                "line_2_1": "   ##    ",
                "line_3_1": "  # #    ",
                "line_4_1": "    #    ",
                "line_5_1": "    #    ",
                "line_6_1": "    #    ",
                "line_7_1": "  #####  ",

                "line_1_2": "  #####  ",
                "line_2_2": " #     # ",
                "line_3_2": " #    #  ",
                "line_4_2": "    ##   ",
                "line_5_2": "   ##    ",
                "line_6_2": "  #      ",
                "line_7_2": " ####### ",

                "line_1_3": " ######  ",
                "line_2_3": "       # ",
                "line_3_3": "       # ",
                "line_4_3": "   ####  ",
                "line_5_3": "       # ",
                "line_6_3": "       # ",
                "line_7_3": " ######  ",

                "line_1_4": " #       ",
                "line_2_4": " #       ",
                "line_3_4": " #    #  ",
                "line_4_4": " ####### ",
                "line_5_4": "      #  ",
                "line_6_4": "      #  ",
                "line_7_4": "      #  ",

                "line_1_5": " ####### ",
                "line_2_5": " #       ",
                "line_3_5": " #       ",
                "line_4_5": " ######  ",
                "line_5_5": "       # ",
                "line_6_5": "       # ",
                "line_7_5": " ######  ",

                "line_1_6": "   ####  ",
                "line_2_6": "  #      ",
                "line_3_6": " #       ",
                "line_4_6": " # ####  ",
                "line_5_6": " #     # ",
                "line_6_6": " #     # ",
                "line_7_6": "  #####  ",

                "line_1_7": " ####### ",
                "line_2_7": " #    #  ",
                "line_3_7": "     #   ",
                "line_4_7": "   ###   ",
                "line_5_7": "   #     ",
                "line_6_7": "  #      ",
                "line_7_7": " #       ",

                "line_1_8": "  #####  ",
                "line_2_8": " #     # ",
                "line_3_8": " #     # ",
                "line_4_8": "  #####  ",
                "line_5_8": " #     # ",
                "line_6_8": " #     # ",
                "line_7_8": "  #####  ",

                "line_1_9": "  #####  ",
                "line_2_9": " #     # ",
                "line_3_9": " #     # ",
                "line_4_9": "  ###### ",
                "line_5_9": "       # ",
                "line_6_9": "       # ",
                "line_7_9": "  #####  "}

# clear function definition
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def player_initialization():
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
    return player_1, player_2

def edit_column(my_dict_table, line, column, checker):
    string1 = my_dict_table["line_" + str(line + 1)]
    string2 = my_dict_table["line_" + str(line)]
    string3 = my_dict_table["line_" + str(line - 1)]
    if checker == "x":
        if column == 0:
            string1 = string1[:7] + "\\ / " + string1[11:]
            string2 = string2[:8] + "X" + string2[9:]
            string3 = string3[:7] + "/ \\ " + string3[11:]
        else:
            col = (column - 1) * 12 + 20
            string1 = string1[:col - 1] + "\\ / " + string1[col + 3:]
            string2 = string2[:col] + "X" + string2[col + 1:]
            string3 = string3[:col - 1] + "/ \\ " + string3[col + 3:]
    else:
        if column == 0:
            string1 = string1[:7] + "---" + string1[10:]
            string2 = string2[:6] + "(   )" + string2[11:]
            string3 = string3[:7] + "---" + string3[10:]
        else:
            col = (column - 1) * 12 + 20
            string1 = string1[:col - 1] + "---" + string1[col + 2:]
            string2 = string2[:col - 2] + "(   )" + string2[col + 3:]
            string3 = string3[:col - 1] + "---" + string3[col + 2:]
    my_dict_table["line_" + str(line + 1)] = string1
    my_dict_table["line_" + str(line)] = string2
    my_dict_table["line_" + str(line - 1)] = string3
    return my_dict_table

def columncheck(my_dict, my_dict_table, column, checker):
    column_list = my_dict[column]
    for i in range(len(column_list)):
        if column_list[i] == []:
            column_list[i].append(checker)
            line_in_table = 3 + i * 5
            edit_column(my_dict_table, line_in_table, column, checker)
            break
    my_dict[column] = column_list
    return my_dict

def play(player, checker, my_dict, my_dict_table):
    col = input(player + " please choose a column: ")
    column_converter = "ABCDEFG"
    col_num = column_converter.find(col.upper())
    while my_dict[col_num][5] != []:
        col = input("Column full, please choose another one: ")
        column_converter = "ABCDEFG"
        col_num = column_converter.find(col.upper())
    columncheck(my_dict, my_dict_table, col_num, checker)

def sign_editor(word):
    for i in range(1, 8):
        word_to_print=""
        for letter in word.upper():
            word_to_print += alphabet_dict["line_" + str(i) + "_" + letter]
        print(word_to_print)