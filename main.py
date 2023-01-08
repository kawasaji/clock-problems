import math
import os
from colorama import init, Fore
from colorama import Back
from colorama import Style

def type_one(hour, minute):
    number = abs(11 * minute - 60 * hour) / 2
    if number > 180:
        return 360 - number
    else:
        return number

os.system("cls")

while True:

    hour = int(input(Fore.BLUE + "enter hour ~# " + Fore.GREEN))
    minute = int(input(Fore.BLUE + "enter minute ~# " + Fore.GREEN))
    number = type_one(hour, minute)
    print(Fore.MAGENTA + str(number))