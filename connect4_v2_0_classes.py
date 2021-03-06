class GameTable:
    alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # creation of a class variable dictionary containing signs of letters to edit each variations signs
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

    # creation of a class variable dictionary containing signs of numbers to edit each variations signs
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
    
    x_win = False
    o_win = False

    table_print_count = 0

    def __init__(self, lines, columns, name):
        self.lines = int(lines)
        self.columns = max(int(columns), len(GameTable.alphabet_str))
        self.name = name

        # initialize dicts as instance variables
        self.dict = {}
        for col in range(self.columns):
            self.dict[col] = [[] for j in range(self.lines)]
        self.table = {}

    def sign_editor(self, word):
        print(" " + "_" * 9 * len(word) + " ")
        print("|" + " " * 9 * len(word) + "|")
        for i in range(1, 8):
            word_to_print="|"
            for char in word.upper():
                if char.isnumeric() == True:
                    word_to_print += GameTable.numbers_dict["line_" + str(i) + "_" + char]
                else:
                    word_to_print += GameTable.alphabet_dict["line_" + str(i) + "_" + char]
            print(word_to_print + "|")
        print("|" + "_" * 9 * len(word) + "|")

    def edit_column(self, line = 0, column = 0, checker = "a"):
        string1 = self.table["line_" + str(line + 1)]
        string2 = self.table["line_" + str(line)]
        string3 = self.table["line_" + str(line - 1)]
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
        elif checker == "o":
            if column == 0:
                string1 = string1[:7] + "---" + string1[10:]
                string2 = string2[:6] + "(   )" + string2[11:]
                string3 = string3[:7] + "---" + string3[10:]
            else:
                col = (column - 1) * 12 + 20
                string1 = string1[:col - 1] + "---" + string1[col + 2:]
                string2 = string2[:col - 2] + "(   )" + string2[col + 3:]
                string3 = string3[:col - 1] + "---" + string3[col + 2:]
        self.table["line_" + str(line + 1)] = string1
        self.table["line_" + str(line)] = string2
        self.table["line_" + str(line - 1)] = string3

    def table_editor(self):
        GameTable.table_print_count += 1 # si different de 0 la partie a commencer
        # store the bottom line of each row
        for i in range(1, self.lines * 5 + 1 ,5):
            temp_line = "line_" + str(i)
            self.table[temp_line] = "  |___________|" + self.columns * "___________|"

        # fill each row
        for i in range(2, self.lines * 5 + 1, 1):
            temp_line = "line_" + str(i)
            if temp_line in self.table.keys():
                continue
            self.table[temp_line] = "  |           |" + self.columns * "           |"

        # update each row with the corresponding number
        j = 1
        for i in range(3, self.lines * 5 + 1, 5):
            temp_line = "line_" + str(i)
            temp_string = self.table[temp_line]
            self.table[temp_line] = str(j) + temp_string[1:]
            j += 1

        # add the botom line to add a letter to the corresponding column
        for i in range(1, self.columns):
            self.table["line_0"] = "        A      " + "      " + GameTable.alphabet_str[i] + "      "
        print(self.table)

    def sign_printer(self):
        # print the first lines of the frame
        print(" " + "_" * 9 * len(self.name) + " ")
        print("|" + " " * 9 * len(self.name) + "|")

        # loop through each lines of the alphabet dict and each letter of the name
        for i in range(1, 8):
            word_to_print = "|"
            for letter in self.name.upper():
                word_to_print += GameTable.alphabet_dict["line_" + str(i) + "_" + letter]
            print(word_to_print + "|")

        # print the last line of the frame    
        print("|" + "_" * 9 * len(self.name) + "|")
        
    def columncheck(self, column, checker):
        column_list = self.dict[column]
        for i in range(len(column_list)):
            if column_list[i] == []:
                column_list[i].append(checker)
                line_in_table = 3 + i * 5
                self.edit_column(self.table, line_in_table, column, checker)
                break
        self.dict[column] = column_list

    def play(self, player):
        col = input(player + " please choose a column: ")
        col_num = GameTable.alphabet_string.find(col.upper())
        while self.dict[col_num][5] != []:
            col = input("Column full, please choose another one: ")
            col_num = GameTable.alphabet_str.find(col.upper())
        self.columncheck(col_num, player.checker)

    def vertical_win(self):
        for i in range(self.columns):
            count_x = 0
            count_o = 0
            for j in range(self.lines - 4 + 1):
                if self.dict.get(j)[i] == "x":
                    count_x += 1
                if self.dict.get(j)[i] == "o":
                    count_o += 1
            if count_x == 4:
                GameTable.x_win = True
            if count_o == 4:
                GameTable.o_win = True

    def diag_right_win(self):
        for i in range(self.columns - 4 + 1):
            count_x = 0
            count_o = 0
            for j in range(self.lines - 4 + 1):
                for k in range(4):
                    if self.dict.get(i+k)[j+k] == "x":
                        count_x += 1
                    if self.dict.get(i+k)[j+k] == "o":
                        count_o += 1
                    if count_x == 4:
                        GameTable.x_win = True
                    if count_o == 4:
                        GameTable.o_win = True

    def diag_left_win(self):
        for i in range(self.columns - 4, self.columns):
            count_x = 0
            count_o = 0
            for j in range(self.lines - 4 + 1):
                for k in range(4):
                    if self.dict.get(i-k)[j-k] == "x":
                        count_x += 1
                    if self.dict.get(i-k)[j-k] == "o":
                        count_o += 1
                    if count_x == 4:
                        GameTable.x_win = True
                    if count_o == 4:
                        GameTable.o_win = True

    def horizontal_win(self):
        for j in range(self.lines):
            count_x = 0
            count_o = 0
            for i in range(self.columns - 4 + 1):
                if self.dict.get(i)[j] == "x":
                    count_x += 1
                if self.dict.get(i)[j] == "o":
                    count_o += 1
            if count_x == 4:
                GameTable.x_win = True
            if count_o == 4:
                GameTable.o_win = True
                
    
class Player:
    def __init__(self, name, checker):
        self.name = name
        self.checker = checker

class Popout(GameTable):
    pass