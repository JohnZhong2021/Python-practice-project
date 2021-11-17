# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:22:06 2021

@author: JohnZhong
"""
word_list = ["english", "python", "apple"]
user_input_number = int(input("Please choose a guessing word from number 1-3: "))
word_index = user_input_number - 1

user_guess_letter_total = []

guess_count = 0
while guess_count < 10:
    word_guess = list(word_list[word_index])
    user_guess_letter = input("Please enter your guessed letter: ")
    user_guess_letter_total.append(user_guess_letter)
    guess_count += 1
    def check_word(word_guess, user_guess_letter_total):
        for i in range(len(word_guess)):
           if word_guess[i] not in user_guess_letter_total:
                word_guess[i] = "*"
        return word_guess
    print("The guessed word is",''.join(check_word(word_guess, user_guess_letter_total)))
    if "*" not in word_guess:
        print("\nCongretulations! You win!!!")
        break
if guess_count >=10:
    print("Sorry, you only have 10 times to guess, better luck next time...")
