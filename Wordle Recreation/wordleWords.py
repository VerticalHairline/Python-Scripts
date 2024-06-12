import os
import random
import string

cwd = os.getcwd()
file = open('C://Users//aiden//Desktop//Python Scripts//Wordle Recreation//.txt files//sgb-words.txt')

words = file.readlines()

def getWord():
    randomInt = random.randint(0, len(words))
    wordle = words[randomInt].strip()
    return wordle

wordList = [x.strip() for x in words]

file.close()
    
