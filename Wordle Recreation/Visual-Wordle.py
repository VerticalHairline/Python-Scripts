from wordleWords import getWord
from wordleWords import wordList
from Wordle import checkWord

rowPosition = 0
columnPosition = 0
secretWord = getWord()
instance = 1

import tkinter as tk

class GUI():

    instances = 1

    def __init__(self, instance):
        self.main = tk.Tk()
        self.instance = instance

        self.main.title("Wordle Recreation (Aiden Pickett 6/3/34)")
        self.header()
        self.initialize()

        self.main.mainloop()

    def header(self):
        self.label = tk.Label(self.main, text = "Wordle", font=("Arial", 35))
        self.label.pack(padx=10,pady=10)

    def initialize(self):

        self.buttons = []
        self.guesses = []
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        self.main.geometry("500x700")

        self.guessboard = tk.Frame(self.main)
        for i in range(0, 6):
            self.guessboard.columnconfigure(i, weight = 1)

        for i in range(0,5):
            guess = []
            for x in range(0,6):
                guessLetter = tk.Label(self.guessboard, width = 5, height = 2, text = "||", font = ('Arial', 20))
                guessLetter.grid(row = x, column = i)
                guess.append(guessLetter)
            self.guesses.append(guess)

        self.guessboard.pack(padx = 10, pady = 10)

        self.keyboard = tk.Frame(self.main)
        for i in range(0,1):
            self.keyboard.columnconfigure(i, weight = 1)

        for i in range(0,2):
           for x in range(0,13):
                buttonLetter = self.alphabet[x + i*13]
                button = tk.Button(self.keyboard, width=3, text = str(buttonLetter), font = ("Arial", 12), command = lambda buttonLetter = buttonLetter: self.keyboardPress(buttonLetter))
                button.grid(row=i, column=x)
                self.buttons.append(button)

        self.keyboard.pack(padx=10,pady=10)

    def keyboardPress(self, letter):

        global rowPosition
        global columnPosition

        if(not(columnPosition == 6 and rowPosition == 0) and not rowPosition == 5):
            currentPosition = self.guesses[rowPosition][columnPosition]
            currentPosition['text'] = letter
            rowPosition += 1
        
        if rowPosition == 5 and not columnPosition == 6:
            self.isValidWord()

    def buttonColorChange(self, colorInfo):
        lettersToColor = []
        letterColors = []
        for x in colorInfo:
            if x['color'] != 'grey':
                lettersToColor.append(x['letter'])
        for x in colorInfo:
            if x['color'] != 'grey':
                letterColors.append(x['color'])
        
        self.keyboardColorChange(lettersToColor, letterColors)

        lettersToColor = []
        letterColors = []
        for x in colorInfo:
            if x['color'] == 'grey':
                lettersToColor.append(x['letter'])
        for x in colorInfo:
            if x['color'] == 'grey':
                letterColors.append(x['color'])

        self.keyboardColorChange(lettersToColor, letterColors)

    def keyboardColorChange(self, lettersToColor, letterColors):
        for button in self.buttons:
            for index, letter in enumerate(lettersToColor):
                if button.cget('text').lower() == letter:
                    match button.cget('bg'):
                        case 'SystemButtonFace':
                            button.config(bg = letterColors[index])    
                        case 'gray':
                            button.config(bg = letterColors[index])    
                        case 'yellow':
                            if letterColors[index] == 'green':
                                button.config(bg = letterColors[index])
                        case 'green':
                            break

    def isValidWord(self):
        global rowPosition
        global columnPosition

        guess = ''

        for i in self.guesses:
            guess += i[columnPosition].cget('text')

        guess = guess.lower()

        if guess in wordList:
            info = checkWord(guess, secretWord)
            columnPosition += 1
            rowPosition = 0
            self.colorLetters(info)
            
        else:
            for x in range(0, 5):
                currentPosition = self.guesses[x][columnPosition]
                currentPosition['text'] = '||'

            rowPosition = 0

    def colorLetters(self, colorInformation):

        self.buttonColorChange(colorInformation)
        self.buttonColorChange(colorInformation)

        win = 0
        for x in range(0, 5):
            currentPosition = self.guesses[x][columnPosition - 1]
            currentPosition.config(bg = colorInformation[x]['color'])
            if currentPosition.cget('bg') == 'green':
                win += 1

        if win == 5:
            self.end('You win!', f'It took you {columnPosition} guesses')
            win = True

        if columnPosition == 6 and win != True:
            self.end('You Lose!', f'The Word was: {secretWord}')
    
    def end(self, *endScreenText):
        self.keyboard.destroy()
        endScreenTexts = []

        for endScreenText in endScreenText:
            self.winScreen = tk.Label(self.main, text = endScreenText, font=("Arial", 23))
            self.winScreen.pack(padx = 10, pady = 10)
            endScreenTexts.append(self.winScreen)

        self.button = tk.Button(text = 'Play Again?', command = lambda: self.playAgainButtonFunctionality(self.winScreen, self.button, *endScreenTexts))
        self.button.pack(padx = 10, pady = 10)

    def playAgainButtonFunctionality(self, *destructions):
        global instance
        global columnPosition
        global secretWord
        
        columnPosition = 0
        secretWord = getWord()
        self.guessboard.destroy()
        for toDestroy in destructions:
            toDestroy.destroy()

        self.instances += 1
        self.initialize()
        
GUI(instance)