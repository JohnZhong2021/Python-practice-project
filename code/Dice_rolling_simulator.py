# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:01:47 2021

@author: JohnZhong
"""
import random
user_input = input("Please press Enter to start rolling the dice! ")
dice_number_count = 0
dice_number_total = []
while user_input != "end":
    dice_number = random.randint(1, 6)
    dice_number_total.append(dice_number)
    dice_number_count += 1
    print("\nThe dice number is:", dice_number)
    user_input = input("You can keep rolling the dice by pressing Enter!\
 You can also stop trying by typing end!")
print("\nThe game is over!Thanks for playing!")    
print("\n*****\nTotal rolling number:", dice_number_count)
#print(dice_number_total)
print("Best rolling:", max(dice_number_total),"\n*****")
