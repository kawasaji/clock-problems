import math
import os

def type_one(hour, minute):
    number = abs(11 * minute - 60 * hour) / 2
    if number > 180:
        number = 360 - number
    return number

os.system("cls")

while True:

    hour = int(input("enter hour ~# "))
    minute = int(input("enter minute ~# "))
    number = type_one(hour, minute)
    print(number)