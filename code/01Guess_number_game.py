import random


def get_num_guess(int1, int2):
    number_generate = random.randint(int1, int2)
    return number_generate


def get_user_guess(int1, int2):
    print("------------\nThe number is between: ", int1, "-", int2, "\n-------------")
    while True:
        try:
            user_input = int(input("Please try a number: "))
            if user_input in range(int1, int2 + 1):
                return user_input
            else:
                print("The number is out of range, please give another try!")
        except(ValueError, SyntaxError):
            print("Invalid data, please enter a number!")


def get_guess_count(number_generate, user_input, int1, int2):
    j = 1
    while number_generate != user_input:
        if user_input > number_generate:
            print("\nWrong guess! The number is too large!")
            user_input = get_user_guess(int1, int2)
        elif user_input < number_generate:
            print("\nWrong guess! The number is too small!")
            user_input = get_user_guess(int1, int2)
        j += 1
    print("\n*****\nBingo! Congratulations! You are right!!")
    return j


n1 = 1
n2 = 100
number_guess = get_num_guess(n1, n2)
user_guess = get_user_guess(n1, n2)
guess_count = get_guess_count(number_guess, user_guess, n1, n2)
print("Your guess count is:", guess_count, "\n*****")
