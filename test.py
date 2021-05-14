connect4_dict = {}
for col in ["A", "B", "C", "D", "E", "F", "G"]:
    connect4_dict[col] = [[] for j in range(6)]

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
for i in range(30,-1,-1):
    print(connect4_table["line_" + str(i)])