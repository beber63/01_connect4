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
    for i in range(6):
        if my_dict.get(column) == []:
            my_dict.get(column) = checker