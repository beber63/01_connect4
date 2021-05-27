class TableConnect4:
    alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, lines, columns):
        self.lines = int(lines)
        self.columns = max(int(columns), len(TableConnect4.alphabet_str))
        self.connect4_dict = {}
        self.connect4_table = {}

    def dict(self):
        # make a normal dictionnary that represents the board
        # easier to check the winning conditions and to drive the graphical version of the board 
        for col in range(self.columns):
            self.connect4_dict[col] = [[] for j in range(self.lines)]

    def table(self):
        # store the bottom line of each row
        for i in range(1, self.lines * 5 + 1 ,5):
            temp_line = "line_" + str(i)
            self.connect4_table[temp_line] = "  |___________|" + self.columns * "___________|"
        # fill each row
        for i in range(2, self.lines * 5 + 1, 1):
            temp_line = "line_" + str(i)
            if temp_line in self.connect4_table.keys():
                continue
            self.connect4_table[temp_line] = "  |           |" + self.columns * "           |"
        # update each row with the corresponding number
        j = 1
        for i in range(3, self.lines * 5 + 1, 5):
            temp_line = "line_" + str(i)
            temp_string = self.connect4_table[temp_line]
            self.connect4_table[temp_line] = str(j) + temp_string[1:]
            j += 1
        # add the botom line to add a letter to the corresponding column
        for i in range(1, self.columns):
            self.connect4_table["line_0"] = "        A      " + "      " + TableConnect4.alphabet_str[i] + "      "

class Popout(TableConnect4):
    pass

class Player:
    def __init__(self, name, checker):
        self.name = name
        self.checker = checker