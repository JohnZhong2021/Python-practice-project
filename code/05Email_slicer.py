# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:17:39 2021

@author: JohnZhong
"""

class slicer(object):
    def __init__(self, mail):
        self.mail = mail
    def get_slice_num(self):
        i = 0
        for char in self.mail:
            if char == "@":
                break
            else:
                i += 1
        return i
    def get_user_name(self):
        user_name = self.mail[0:self.get_slice_num()]
        return user_name
    def get_domain_name(self):
        domain_name = self.mail[self.get_slice_num()+1:]
        return domain_name
x = slicer(input("Please input an email address:\n"))
print("The user name is:",x.get_user_name())
print("The domain name is:",x.get_domain_name())

