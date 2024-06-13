# I will be attempting to draw thing

from graphics import *
import time

def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.setCoords(0,0,500,500)
    for coords in range(0,50):
        win.plot(coords, coords)
    for balls in range(0,100):
        c.move(6,5)
        time.sleep(0.05)
    
main()