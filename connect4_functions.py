# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# clear function
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
    print("|     ######   ######   #      #  #      #  #######   ######     #                   #    |")
    print("|_________________________________________________________________________________________|\n\n")