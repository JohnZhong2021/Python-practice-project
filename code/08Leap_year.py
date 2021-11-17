# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:45:11 2021

@author: JohnZhong
"""

def is_leap_year(year_num):
    year_num = int(year_num)
    remainder = year_num % 4
    if remainder == 0:
        return True
    else:
        return False

while True:
    try:
        year_num = int(input("Please input a year: "))
        if type(year_num) == int:
            break
    except(ValueError, SyntaxError):
        print("Wrong year format, please give another yaer!")


if is_leap_year(year_num):
    print("Year", year_num, "is a leap year")
else:
    print("Year", year_num, "isn't a leap year")