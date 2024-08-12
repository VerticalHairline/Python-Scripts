#App to send out generic copies of a thank you card or other type in mass


import tkinter as tk
import tkinter.ttk as ttk
from DocsPrinter import main as API
from tkinter.constants import *


letterDictionary = {}
completedLetters = {}

#control what phrases the program replaces with the ones inputted by the user
namePrompt = '*NAME*'
giftPrompt = '*GIFT*'

genericLetterText = ''


#Large class that creates objects that contain the name and gift for a letter, as well as methods to mutate these
class Letters:

    instances = []

    def __init__(self, Name, Gift):
        self.name = Name
        self.gift = Gift

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name} object, {self.gift} gift"

    def editLetter(self, newName, newGift):
        self.gift = newGift
        self.name = newName

#Function to instantiate Letters class
def addLetter(Name, Gift):
    obj = Letters(Name, Gift)
    obj.instances.append(obj)

    GUIDestroy()
    buildMainWindow()

#Adds the rows displayed on the left side of the GUI
def addInfoRows():

    wrapper1 = tk.LabelFrame(mainWindow)

    canvas = tk.Canvas(wrapper1, width=450, height=1500)
    canvas.pack(side=LEFT)

    scrollbar = tk.Scrollbar(wrapper1, orient=VERTICAL, command = canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox(ALL)))
    
    rowFrame = tk.Frame(canvas)

    for count, Name in enumerate(letterDictionary):

        nameLabel = tk.Label(rowFrame, text=letterDictionary[Name].name, font= 10, background= 'gray', width=15)
        giftLabel = tk.Label(rowFrame, text=letterDictionary[Name].gift, font = 10, background= 'dark gray', width=15)
        editButton = tk.Button(rowFrame, text='Edit', font = 8, command = lambda Name = Name: editInital(Name))
        deleteButton = tk.Button(rowFrame, text='Delete', font = 8, command = lambda Name = Name: deleteName(Name))
    

        for i in range(0,4):
            rowFrame.columnconfigure(i, weight=4)
        nameLabel.grid(row=count, column=0)
        giftLabel.grid(row=count, column=1)
        editButton.grid(row=count, column=2)
        deleteButton.grid(row=count, column=3)

    canvas.create_window(0, 0, window = rowFrame, anchor=NW)

    wrapper1.pack(padx = 10, pady = 10, side=LEFT)

#Deletes unwanted instance of Letters class, called by deleteButton made in addInfoRows
def deleteName(name):
    GUIDestroy()
    Letters.instances.remove(letterDictionary[name])
    del letterDictionary[name]
    buildMainWindow()

#Button side function to change the states of a letter object, calls edit letter
def editInital(name):
    GUIDestroy()
    nameTitle = tk.Label(mainWindow, text="Name?")
    nameTitle.pack(pady=10)
    nameBox = tk.Text(mainWindow, width=30, height=1, wrap=NONE)
    nameBox.pack(pady=10)
    giftTitle = tk.Label(mainWindow, text="Gift?")
    giftTitle.pack(pady = 10)
    giftBox = tk.Text(mainWindow, width=30, height=1, wrap=NONE)
    giftBox.pack(pady = 10)
    editLetterButton = tk.Button(mainWindow, text='confirm', command=lambda: editLetter(name, nameBox.get(1.0, 1.29), giftBox.get(1.0, 1.29)))
    editLetterButton.pack(pady = 10)

#calls edit method in given Letters object to change its state
def editLetter(name, nameEdit, giftEdit):
    letterDictionary[name].editLetter(nameEdit, giftEdit)
    GUIDestroy()
    buildMainWindow()

#prints titles to screen
def titles():
    title = tk.Label(mainWindow, text="Automatic Thank-You Card Generator", font= 35)
    title.pack(side=TOP)

    subtitle = tk.Label(mainWindow, text='Created by Aiden Pickett', font = 10)
    subtitle.pack(side=TOP)

    Instructions = tk.Label(mainWindow, text=f'''Enter your generic letter format below, with {namePrompt} and {giftPrompt} for where you want the \n program to place the name and gift in the letter, respectively.''')
    Instructions.pack(side=TOP)

#removes all GUI elements
def GUIDestroy():

    for widget in mainWindow.winfo_children():
        widget.destroy()

#Button side function for adding new rows to left hand GUI list, calls addLetter
def addLetterInital():
    GUIDestroy()
    nameTitle = tk.Label(mainWindow, text="Name?")
    nameTitle.pack(pady = 10)
    nameBox = tk.Text(mainWindow, width=30, height=1, wrap=NONE)
    nameBox.pack(pady = 10)
    giftTitle = tk.Label(mainWindow, text="Gift?")
    giftTitle.pack(pady = 10)
    giftBox = tk.Text(mainWindow, width=30, height=1, wrap=NONE)
    giftBox.pack(pady = 10)
    addLetterButton = tk.Button(mainWindow, text='Add letter', command=lambda: addLetter(nameBox.get(1.0, 1.29), giftBox.get(1.0, 1.29)))
    addLetterButton.pack(pady = 10)

#Adds text box where user enters generic version of the letters they will send
def textBox():
    addLetterButton = tk.Button(mainWindow, text = "Add another Letter", command = addLetterInital)
    addLetterButton.pack(side=TOP, pady = 10)

    genericLetter = tk.Text(mainWindow, width=130)
    genericLetter.insert(1.0, genericLetterText)
    genericLetter.pack(side=TOP)

    #replaces the namePrompt and giftPrompt strings in letter with user supplied data. Also calls API
    def writeLetter():
        global completedLetters
        completedLetters = {}

        for name in letterDictionary.values():
            letter = genericLetter.get(1.0, 'end-1c')
            if namePrompt in letter:
                letter = letter.replace(namePrompt, name.name)
            if giftPrompt in letter:
                letter = letter.replace(giftPrompt, name.gift)
            
            completedLetters.__setitem__(name.name, letter)
        
        API(completedLetters.values())

    writeButton = tk.Button(mainWindow, text="Write Letters", command=writeLetter, width = 15, height =3)
    writeButton.pack(side=TOP, pady = 10)

    saveButton = tk.Button(mainWindow, text='Save Letter', command=lambda: saveLetter(genericLetter.get(1.0, 'end-1c')), width=10, height=2)
    saveButton.pack(side=TOP)

#Saves generic version of letter so on GUIdestroy call it remains saved
def saveLetter(letterToSave):
    global genericLetterText
    print(letterToSave)
    genericLetterText = letterToSave

#Builds the home window as well as resets the letterDictonary as to make sure the left side bar is correct for the new instance
def buildMainWindow():
    global letterDictionary
    letterDictionary = {}
    for object in Letters.instances:
        letterDictionary.__setitem__(object.__str__(), object)
    addInfoRows()
    titles()
    textBox()

mainWindow = tk.Tk()
mainWindow.geometry('1600x700')
mainWindow.resizable(height = TRUE, width = FALSE)
mainWindow.title('Auto Thank-You Card Generator')
buildMainWindow()

mainWindow.mainloop()