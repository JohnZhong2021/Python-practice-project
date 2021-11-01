# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:17:39 2021

@author: JohnZhong
"""

def email_user(mail):
    i = 0
    for char in mail:
        if char == "@":
           break
        else:
           i += 1
    user_name = mail[0: i]
    return user_name
def email_domain(mail):
    i = 0
    for char in mail:
        if char == "@":
           break
        else:
           i += 1
    domain_name = mail[i+1: ]
    return domain_name
x = input("Please input an email address:\n")
print("The user name is:", email_user(x))
print("The domain name is:", email_domain(x))