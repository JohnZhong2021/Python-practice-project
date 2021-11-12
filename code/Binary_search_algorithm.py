
"""
Have you ever heard the proverb, “finding a needle in a haystack.” This program is designed to do just that- by using a binary search algorithm.
You can create a list of random numbers between 0 to 100, with every succeeding number having a difference of 2 between them.
When the user inputs a random number, the program will check if that number is included in the list. It will do so by creating two halves of the list.
If the program finds the number in the first half of the list, it will eliminate the other half and vice versa. The search will continue until the program finds
the number input of the user or until the subarray size becomes 0 (this means that the number is not in the list).
This python project idea will help you create an implement an algorithm that searches for an element in a list.
"""

number_list = []
i = 0
while i <=100 :
    number_list.append(i)
    i += 2
#print(len(number_list))
user_num = int(input("Please input an integer:\n"))
def binary_search(user_num):
    check_list = number_list
    while len(check_list) >= 2:
        mid_point_index = int((len(check_list) + 1) / 2 - 1)
        # print("\nThe mid_point_index is:",mid_point_index)
        # print(check_list)
        # print("The element of mid_point is:",check_list[mid_point_index])
        # print("The amount of check_list:",len(check_list))
        if user_num > check_list[mid_point_index]:
            check_list = check_list[mid_point_index+1:]
        elif user_num < check_list[mid_point_index]:
            check_list = check_list[:mid_point_index+1]
        elif user_num == check_list[mid_point_index]:
            print("The number is in the list.")
            break
    #print("The last check list:", check_list)
    if len(check_list) == 1:
        if user_num == check_list[0]:
            print("The number is in the list.")
        else:
            print("The number isn't in the list.")
binary_search(user_num)
