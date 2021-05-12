class XAndO:
    #X sign
    def x_sign(self):
        self.line_X_1 = "\\ /"
        self.line_X_2 = " X  "
        self.line_X_3 = "/ \\"

    #O sign, line_O_1 repeated at the bottom
    def o_sign(self):
        self.line_O_1 = " ----- "
        self.line_O_2 = "(     )"

class TableConnect4:
    #connect 4 table creation, 3 line_empty_case + 1 line_6 to _1 between each line_underscore
    line_empty_case = "   |           |           |           |           |           |           |           |   "
    line_underscore = "   |___________|___________|___________|___________|___________|___________|___________|   "
    line_6 = " 6 |           |           |           |           |           |           |           |   "
    line_5 = " 5 |           |           |           |           |           |           |           |   "
    line_4 = " 4 |           |           |           |           |           |           |           |   "
    line_3 = " 3 |           |           |           |           |           |           |           |   "
    line_2 = " 2 |           |           |           |           |           |           |           |   "
    line_1 = " 1 |           |           |           |           |           |           |           |   "
    line_letters = "         A           B           C           D           E           F           G         "