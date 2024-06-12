# A simple function that simulates a football player running down the field; at interval, he has a chance of being tackled

def instructions():
     print("\n"""" ---Welcome to a football game---
-----Designed by Aiden Pickett-----""""\n")
     print("This game simulates a football player running down the field, ""\n""and at each interval (10 yards by default) he"
           " has a chance of being tackled. ""\n""the player starts at the 50 yard line.""\n")
     print("Here are some of the basic commands: "+("\n")*2)
     print("run() will run the simulation""\n")
     print("average() will show the average yardage the runner gets per run""\n")
     print("instructions() will show this screen again""\n")
     print(("\n"*2)+"run more() to view more commands""\n")

instructions()

import random
global progress, rand, gap
progress, rand, gap = [], 25, -10


def run():
     for i in range (50, 0 , gap):
             if i > 0:
                     tackle = random.randint(0,100)
                     if tackle < rand:
                             print("Oh No! He was tackled at the " + str(i) + " yard line")
                             progress.append(50 - i)
                             break
                     else:
                             print("He's at the " + str(i))
     else:
             print("He Scores!")
             progress.append(50)

def average():
     if progress != []:
          average = sum(progress)
          average = average/len(progress)
          print("\n""The player averaged " + str(round(average, 2)) + " yards per run""\n")
          return round(average, 2)
     else:
          print("Try running the simulation first before finding an average.""\n")

def clear():
     global progress
     progress = []
     print("Progress reset""\n")

def runMulti():
     x = int(input("How many times would you like to run the simulation? ""\n"))
     while x > 0:
          run()
          print("\n")
          x-=1

def prob():
     userProb = int(input("What would you like the probability of a tackle to be (in % chance)?""\n"))
     while userProb > 100 or userProb < 0:
              userProb = int(input("Please enter a valid percentage between 0 and 100""\n"))
     else:
          global rand
          rand = userProb

def increment():
     userInc = int(input("What yardage increment would you like to use? ""\n"))
     while 50.0 % userInc != 0:
          userInc = int(input("Please select a yardage increment that is divisible by 50" "\n"))
     else:
          global gap
          gap = abs(userInc)*-1

def more():
     print(("\n"*2)+"""clear() will clear all stored data used to find the average yardage

runMulti() will allow you to run multiple instances of run() with one command

prob() will allow you to change the probability of the runner being tackled

increment() will allow you to change the increment at which the runner
has a chance to get tackled"""+("\n"*2))

          
          

