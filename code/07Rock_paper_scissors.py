# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 19:40:19 2021

@author: JohnZhong
"""

from random import choice
def user_input():
    user_input = input("Let's play rock paper and scissors with the computer!\n\
\nR for rock\nP for paper\nS for scissors\n")
    return user_input

def check_user_move(user_input):
    if user_input in ["r", "R", "rock", "Rock", "ROCK"]:
        return "r"
    elif user_input in ["p", "P", "paper", "Paper", "PAPER"]:
        return "p"
    elif user_input in ["s", "S", "Scissors", "scissors", "SCISSORS"]:
        return "s"
    else:
        return "Invalid input! Please check..."

def decide_winner(computer_move, user_move):
    if computer_move == user_move:
        return "It's a tie"
    elif computer_move == "s" and user_move == "p":
        return "Computer wins"
    elif computer_move == "s" and user_move == "r":
        return "You win"
    elif computer_move == "r" and user_move == "s":
        return "Computer wins"
    elif computer_move == "r" and user_move == "p":
        return "You win"
    elif computer_move == "p" and user_move == "r":
        return "Computer wins"
    elif computer_move == "p" and user_move == "s":
        return "You win"

def score_keeper(result_per_move):
    computer_sore = 0
    user_score = 0
    if result_per_move == "Computer wins":
        computer_sore += 1
    elif result_per_move == "You win":
        user_score += 1
    return [computer_sore, user_score]

i = 0
computer_final_score = 0
user_final_score = 0
while i <= 5:
    computer_move = choice(['r', 'p', 's'])
    user_move = check_user_move(user_input())
    decide_winner(computer_move, user_move)
    result_per_move = decide_winner(computer_move, user_move)
    computer_final_score += score_keeper(result_per_move)[0]
    user_final_score += score_keeper(result_per_move)[1]
    i += 1
if computer_final_score > user_final_score:
    print("\nSorry you lose...better luck next time")
    print("\nThe computer score is:", computer_final_score)
    print("Your score is:", user_final_score)
elif computer_final_score < user_final_score:
    print("\nCongretulations! You are the winner!!!")
    print("\nThe computer score is:", computer_final_score)
    print("Your score is:", user_final_score)
else:
    print("\nIt's a tie")
    print("\nThe computer score is:", computer_final_score)
    print("Your score is:", user_final_score)






