class Table:
    alphabet_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, lines, columns, name):
        self.lines = lines
        self.columns = max(columns, len(Table.alphabet_str))
        self.name = name

        connect4_table = {}
        # store the bottom line of each row
        for i in range(1, self.lines * 5 + 1 ,5):
            temp_line = "line_" + str(i)
            connect4_table[temp_line] = "  |___________|" + self.columns * "___________|"
        # fill each row
        for i in range(2, self.lines * 5 + 1, 1):
            temp_line = "line_" + str(i)
            if temp_line in connect4_table.keys():
                continue
            connect4_table[temp_line] = "  |           |" + self.columns * "           |"
        # update each row with the corresponding number
        j = 1
        for i in range(3, self.lines * 5 + 1, 5):
            temp_line = "line_" + str(i)
            temp_string = connect4_table[temp_line]
            connect4_table[temp_line] = str(j) + temp_string[1:]
            j += 1
        # add the botom line to add a letter to the corresponding column
        for i in range(1, self.columns):
            connect4_table["line_0"] = "        A      " + "      " + Table.alphabet_str[i] + "      "
        
        connect4_dict = {}
        # make a normal dictionnary that represents the board
        # easier to check the winning conditions and to pilot the graphical version of the board 
        for col in range(self.columns):
            connect4_dict[col] = [[] for j in range(self.lines)]

    def __repr__(self):
        "You are playing {} game.".format(self.name)
    
class Player:
    def __init__(self, name, checker):
        self.name = name
        self.checker = checker