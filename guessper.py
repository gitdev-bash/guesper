#!/usr/bin/env python3

import random


# define generatecards
def generatecards(maxnum, isRandom):
    if maxnum.isdigit() == False:
        print("ONLY NUMBERS!")
        return
    cardlist = []
    for card in range(len(bin(int(maxnum)).replace("0b", ""))):
        cardlist.append([])
    for num in range(1, int(maxnum) + 1):
        binnumrev = bin(int(num)).replace("0b", "")
        binnum = binnumrev[::-1]
        for x in range(len(binnum)):
            if binnum[x] == "1":
                cardlist[x].append(num)
    if isRandom:
        for sublist in range(len(cardlist)):
            random.shuffle(cardlist[sublist])
    return cardlist


# define askq
def askq(cardlist):
    cardnum = 0
    print("Enter the numbers in front of the lines if line has the number.")
    for card in cardlist:
        cardnum += 1
        print(str(cardnum) + ". " + str(card))
        print("")
    return input(":")


# define calculatenum
def calculatenum(idlist):
    num = 0
    for exp in idlist.replace(" ", "").split(","):
        num += 2 ** (int(exp) - 1)
    return num


print("Please enter the maximum posible number.")
while True:
    print(
        "Your number is "
        + str(calculatenum(askq(generatecards(input("max num?:"), True))))
    )
