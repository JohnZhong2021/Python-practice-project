# -*- coding: utf-8 -*-

import random

def get_num_guess(n1, n2):
    number_guess = random.randint(n1, n2)
    return number_guess

def get_user_guess(n1, n2):
    print("The number is between: ", n1, "-", n2)
    while True:
        try:
            user_guess = int(input("Please guess a number: "))
            if user_guess in range(n1, n2):
                return user_guess
                break
            else:
                print("The number is out of range, please give another try!")
        except(ValueError, SyntaxError):
            print("Invalid data, plese enter a number!")

def get_guess_count(number_guess, user_guess):
    j = 1
    while user_guess != number_guess:
        if user_guess > number_guess:
            print("Wrong guess! The number is too large!")
            user_guess = int(input("Please try another number: "))
        elif user_guess < number_guess:
            print("Wrong guess! The number is too small!")
            user_guess = int(input("Please try another number: "))
        j += 1
    print("\n*****\nBingo! Congretulations! You are right!!")
    return j
n1 = 1
n2 =100
number_guess = get_num_guess(n1, n2)
user_guess = get_user_guess(n1, n2)
guess_count = get_guess_count(number_guess, user_guess)
print("Your guess count is", guess_count, "\n*****")