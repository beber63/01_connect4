connect4_dict = {}
for col in range(7):
    connect4_dict[col] = [[] for j in range(6)]
print(connect4_dict)
temp = connect4_dict[2]
print(temp)
temp2 = temp[5]
print(temp2)

# creation of an empty dict to store all the lines in the connect 4 table
connect4_table = {}

# store the bottom line of each row
for i in range(1,31,5):
    temp_line = "line_" + str(i)
    connect4_table[temp_line] = "  |___________|___________|___________|___________|___________|___________|___________|"

# fill each row
for i in range(2,31,1):
    temp_line = "line_" + str(i)
    if temp_line in connect4_table.keys():
        continue
    connect4_table[temp_line] = "  |           |           |           |           |           |           |           |"

# update each row with the corresponding number
j = 1
for i in range(3,31,5):
    temp_line = "line_" + str(i)
    temp_string = connect4_table[temp_line]
    connect4_table[temp_line] = str(j) + temp_string[1:]
    j += 1

# add the botom line to add a letter to the corresponding column
connect4_table["line_0"] = "        A           B           C           D           E           F           G      "

# print the table with the lines in inversed order
# for i in range(30,-1,-1):
#     print(connect4_table["line_" + str(i)])

dict_A = {"line_1": "    #    ",
          "line_2": "   # #   ",
          "line_3": "   # #   ",
          "line_4": "  #####  ",
          "line_5": "  #   #  ",
          "line_6": " #     # ",
          "line_7": " #     # "}

dict_B = {"line_1": " ######  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " ######  ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": " ######  "}

dict_C = {"line_1": "  ###### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " #       ",
          "line_5": " #       ",
          "line_6": " #       ",
          "line_7": "  ###### "}

dict_D = {"line_1": " #####   ",
          "line_2": " #    #  ",
          "line_3": " #     # ",
          "line_4": " #     # ",
          "line_5": " #     # ",
          "line_6": " #    #  ",
          "line_7": " #####   "}

dict_E = {"line_1": " ####### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " ####    ",
          "line_5": " #       ",
          "line_6": " #       ",
          "line_7": " ####### "}

dict_F = {"line_1": " ####### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " ####    ",
          "line_5": " #       ",
          "line_6": " #       ",
          "line_7": " #       "}

dict_G = {"line_1": "  ###### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " #   ### ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": "  #####  "}

dict_H = {"line_1": " #     # ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " ####### ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": " #     # "}

dict_I = {"line_1": "  #####  ",
          "line_2": "    #    ",
          "line_3": "    #    ",
          "line_4": "    #    ",
          "line_5": "    #    ",
          "line_6": "    #    ",
          "line_7": "  #####  "}

dict_J = {"line_1": "  ###### ",
          "line_2": "     #   ",
          "line_3": "     #   ",
          "line_4": "     #   ",
          "line_5": " #   #   ",
          "line_6": " #   #   ",
          "line_7": "  ###    "}

dict_K = {"line_1": " #     # ",
          "line_2": " #    #  ",
          "line_3": " #   #   ",
          "line_4": " ####    ",
          "line_5": " #   #   ",
          "line_6": " #    #  ",
          "line_7": " #     # "}

dict_L = {"line_1": " #       ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " #       ",
          "line_5": " #       ",
          "line_6": " #       ",
          "line_7": " ####### "}

dict_M = {"line_1": " #     # ",
          "line_2": " ##   ## ",
          "line_3": " # # # # ",
          "line_4": " #  #  # ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": " #     # "}

dict_N = {"line_1": " #     # ",
          "line_2": " ##    # ",
          "line_3": " # #   # ",
          "line_4": " #  #  # ",
          "line_5": " #   # # ",
          "line_6": " #    ## ",
          "line_7": " #     # "}

dict_O = {"line_1": "  #####  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " #     # ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": "  #####  "}

dict_P = {"line_1": " ######  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " ######  ",
          "line_5": " #       ",
          "line_6": " #       ",
          "line_7": " #       "}

dict_Q = {"line_1": "   ###   ",
          "line_2": "  #   #  ",
          "line_3": " #     # ",
          "line_4": " #     # ",
          "line_5": " #   # # ",
          "line_6": "  #   #  ",
          "line_7": "   ### # "}

dict_R = {"line_1": " ######  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " ######  ",
          "line_5": " #   #   ",
          "line_6": " #    #  ",
          "line_7": " #     # "}

dict_S = {"line_1": "  ###### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": "  #####  ",
          "line_5": "       # ",
          "line_6": "       # ",
          "line_7": " ######  "}

dict_T = {"line_1": " ####### ",
          "line_2": "    #    ",
          "line_3": "    #    ",
          "line_4": "    #    ",
          "line_5": "    #    ",
          "line_6": "    #    ",
          "line_7": "    #    "}

dict_U = {"line_1": " #     # ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " #     # ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": "  #####  "}

dict_V = {"line_1": " #     # ",
          "line_2": " #     # ",
          "line_3": "  #   #  ",
          "line_4": "  #   #  ",
          "line_5": "   # #   ",
          "line_6": "   # #   ",
          "line_7": "    #    "}

dict_W = {"line_1": " #     # ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": " #  #  # ",
          "line_5": " #  #  # ",
          "line_6": " # # # # ",
          "line_7": "  #   #  "}

dict_X = {"line_1": " #     # ",
          "line_2": "  #   #  ",
          "line_3": "   # #   ",
          "line_4": "    #    ",
          "line_5": "   # #   ",
          "line_6": "  #   #  ",
          "line_7": " #     # "}

dict_Y = {"line_1": " #     # ",
          "line_2": "  #   #  ",
          "line_3": "   # #   ",
          "line_4": "    #    ",
          "line_5": "   #     ",
          "line_6": "  #      ",
          "line_7": " #       "}

dict_Z = {"line_1": " ####### ",
          "line_2": "      #  ",
          "line_3": "     #   ",
          "line_4": "    #    ",
          "line_5": "   #     ",
          "line_6": "  #      ",
          "line_7": " ####### "}

dict_0 = {"line_1": "  #####  ",
          "line_2": " #    ## ",
          "line_3": " #   # # ",
          "line_4": " #  #  # ",
          "line_5": " # #   # ",
          "line_6": " ##    # ",
          "line_7": "  #####  "}

dict_1 = {"line_1": "    #    ",
          "line_2": "   ##    ",
          "line_3": "  # #    ",
          "line_4": "    #    ",
          "line_5": "    #    ",
          "line_6": "    #    ",
          "line_7": "  #####  "}

dict_2 = {"line_1": "  #####  ",
          "line_2": " #     # ",
          "line_3": " #    #  ",
          "line_4": "    ##   ",
          "line_5": "   ##    ",
          "line_6": "  #      ",
          "line_7": " ####### "}

dict_3 = {"line_1": " ######  ",
          "line_2": "       # ",
          "line_3": "       # ",
          "line_4": "   ####  ",
          "line_5": "       # ",
          "line_6": "       # ",
          "line_7": " ######  "}

dict_4 = {"line_1": " #       ",
          "line_2": " #       ",
          "line_3": " #    #  ",
          "line_4": " ####### ",
          "line_5": "      #  ",
          "line_6": "      #  ",
          "line_7": "      #  "}

dict_5 = {"line_1": " ####### ",
          "line_2": " #       ",
          "line_3": " #       ",
          "line_4": " ######  ",
          "line_5": "       # ",
          "line_6": "       # ",
          "line_7": " ######  "}

dict_6 = {"line_1": "   ####  ",
          "line_2": "  #      ",
          "line_3": " #       ",
          "line_4": " # ####  ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": "  #####  "}

dict_7 = {"line_1": " ####### ",
          "line_2": " #    #  ",
          "line_3": "     #   ",
          "line_4": "   ###   ",
          "line_5": "   #     ",
          "line_6": "  #      ",
          "line_7": " #       "}

dict_8 = {"line_1": "  #####  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": "  #####  ",
          "line_5": " #     # ",
          "line_6": " #     # ",
          "line_7": "  #####  "}

dict_9 = {"line_1": "  #####  ",
          "line_2": " #     # ",
          "line_3": " #     # ",
          "line_4": "  ###### ",
          "line_5": "       # ",
          "line_6": "       # ",
          "line_7": "  #####  "}