import sys

sys.path.append("C:/Users/aiden/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/site-packages")
                
import pyautogui
import time
import urllib
import urllib.request
copy = False
splitList = []
lineReturn = []
    
def getText():
    global copy
    global splitList
    global lineReturn
    
    request = urllib.request.urlopen("https://ai.eecs.umich.edu/people/dreeves/Fox-In-Socks.txt")
    text = request.readlines()
    
    for line in text:
        
        readableText = ((str(line.strip()).replace("b","",1)).replace("'","")).replace('"',"")
        
        if readableText == "":
            splitList.append(lineReturn)
            lineReturn = []
        else:
            lineReturn.append(readableText)

def showMousePos():
    time.sleep(2)
    print(pyautogui.position())

def makeSlide():
    for l in range(0, len(splitList)):
        pyautogui.moveTo(125, 259)
        pyautogui.click(button = 'right')
        time.sleep(0.05)
        pyautogui.click(206, 481)

def fillSlide():
    pyautogui.click(125, 259)
    pyautogui.click(424, 598)
    time.sleep(0.05)
    for slide in splitList:
        for line in slide:
            pyautogui.typewrite(line)
            pyautogui.press('enter')
        pyautogui.click(424, 400)
        pyautogui.press('right')
        pyautogui.click(424, 598)
        
        
getText()
makeSlide()
fillSlide()

