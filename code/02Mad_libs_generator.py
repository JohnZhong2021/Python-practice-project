# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:32:07 2021

@author: JohnZhong
"""

#Mad libs generator 2021/10/12
print("Tell us something about you and we can create a story just for you!")
print("Let's begin!")
noun1 = input("Enter a pet: ")
noun2 = input("Enter a noun: ")
if noun1 in ["dog", "DOG", "Dog"]:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said wan wan wan" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
elif noun1 in ["cat", "CAT", "Cat"]:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said miao miao miao" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
elif noun1 in ["Duck", "DUCK", "Duck", "Goose", "GOOSE", "goose"]:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said quack quack quack" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
elif noun1 in ["Bird", "BIRD", "bird"]:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said chir chir chir" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
elif noun1 in ["pig", "PIG", "Pig"]:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said oink oink oink" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
else:
    story = "Five little " + noun1 + "s" + " went out oneday" + "\nOver the " + noun2 + " " + "and far away" + "\nMother " + noun1 + " " + "said hmn hmn hmn" + "\nBut only four little " + noun1 + "s" + " came back"
    print(story)
