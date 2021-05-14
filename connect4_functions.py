# import only system from os
from os import system, name

# clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# welcome function
def welcome():
    print("\n\n-------------------------------------------------------------------------------------------")
    print("----------------------------------------- WELCOME -----------------------------------------")
    print("-------------------------------------------------------------------------------------------\n\n")

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

def columncheck(my_dict, column, checker):
    column_list = my_dict.get(column)
    if column_list[5] != []:
        print("Column full, please choose another one")
    for i in column_list:
        if column_list[i] == []:
            column_list[i].append[checker]
            #use function to add checker in the column
            break
    my_dict[column] = column_list
    return my_dict

def edit_column(line, column, checker):
    pass