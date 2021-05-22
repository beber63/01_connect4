from os import system, name

# clear function definition
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# connect 4 sign function
def connect4_sign():
    print(" _________________________________________________________________________________________ ")
    print("|                                                                                         |")
    print("|     ######   ######   #      #  #      #  #######   ######  #######         #      #    |")
    print("|    #        #      #  ##     #  ##     #  #        #           #            #      #    |")
    print("|    #        #      #  # #    #  # #    #  #        #           #            #      #    |")
    print("|    #        #      #  #  #   #  #  #   #  ####     #           #      ###   ########    |")
    print("|    #        #      #  #   #  #  #   #  #  #        #           #                   #    |")
    print("|    #        #      #  #    # #  #    # #  #        #           #                   #    |")
    print("|     ######   ######   #     ##  #     ##  #######   ######     #                   #    |")
    print("|_________________________________________________________________________________________|")
    print("                                                                                  beber63 ©")

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
