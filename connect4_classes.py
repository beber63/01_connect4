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

class Connect4Matrix:
    def emptycell(self):
        self.empty_cell = """|           |
        |           |
        |           |
        |           |
        |___________|"""
        return self.empty_cell
    
    def filledcell(self, piece):
        if piece.lower() == "o":
            self.filled_cell = """|           |
            |   -----   |
            |  (     )  |
            |   -----   |
            |___________|"""
        else:
            self.filled_cell = """|           |
            |    \\ /    |
            |     X     |
            |    / \\    |
            |___________|"""
        return self.filled_cell