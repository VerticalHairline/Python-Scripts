# I have too many people to write graduation cards to so I am going to automate it instead

import os
import random

textFile = '\senders.txt'

def addGifts():
    gifts = {}

    file = open(os.getcwd() + textFile)

    giftsList = file.readlines()

    for x in range(0, len(giftsList), 2):
        gifts[giftsList[x].strip()] = giftsList[x+1].strip()

    return gifts

def writeLetter(gifts):
    letterList = {}
    for person in gifts:
        letter = (f'\nDear {person},\n\n            Thanks so much for your thoughtful graduation gift. The {gifts[person]}really does mean a lot.')
        if gifts[person] == ('money' or 'Money'):
            letter = letter + randomCashJoke()
        letter = letter + " Thank you also for your prayers and support as I made my way through High School, it made more of a difference than you could know. I'm super excited for this next chapter in my life, and will keep you updated as to when I make it big in the world of computer science. \n\n                                                                                                                   Sincerely, Aiden\n"

        letterList[person] = letter
    
    return letterList
        
        

def randomCashJoke():
    match random.randint(1,3):
        case 1:
            return " The cash you sent will go towards many bowls of ramen, I'm sure."
        case 2:
            return " The money you sent will be used wisely, probably on many cups of coffee."
        case 3:
            return " The cash you sent will be very helpful; I'll be broke as, well, a college student."

letterList = writeLetter(addGifts())
api_message = list(letterList.values())


'''while True:
    person = input("Whose letter do you want to write? (type 'any' for a random one and 'amount' to see amount remaining)")

    if person == 'amount':
        amountLeft = 0

        for letter in letterList:
            if letterList[letter] != 'written':
                amountLeft = amountLeft + 1

        print(f"you have {amountLeft} letters left to write")

    if person == 'any':
        questionLetter = ''

        for letter in letterList:
            if letterList[letter] != 'written':
                print("\n\n" + letterList[letter] + "\n\n")
                questionLetter = letter
                break
                
        while True:
            validation = input("Done? (y) This will remove the letter from the list ")
            if validation == 'y':
                letterList[questionLetter] = 'written'
                break
            else:
                print("enter 'y' to continue")

    if person != 'any' and person != 'amount':
        if letterList[person]:
            print("you have already written this card")

    if person in letterList and letterList[person] != 'written':
        print("\n\n" + letterList[person] + "\n\n")
        while True:
            validation = input("Done? (y) This will remove the letter from the list ")
            if validation == 'y':
                letterList[person] = 'written'
                break
            else:
                print("enter 'y' to continue")

    if person != 'any' and person != 'amount':
        if letterList[person] != 'written' and person not in letterList:
            print(f'please enter a valid person name, check the {textFile} file for exact syntax')'''
