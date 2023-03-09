import time
import event as event
from turtle import *  # use the turtle library
space = Screen()      # create a Screen object named space
slg = Turtle()       # create a Turtle object named slg

gamepiece = "|"
bg = " "
boardwidth = 30
previewsize = 4
gameboard_past = [bg for x in range(0,boardwidth)]
pieceposition = 3
max_position = len(gameboard_past)

gameinprogress = True

while gameinprogress:
    time.sleep(0.05)
    events = event.get_events()

    if "left arrow" in events:
        if pieceposition > 0:
            gameboard_past[pieceposition] = bg
            pieceposition = pieceposition - 1
        gameboard_past[pieceposition] = gamepiece
        slg.left(15)   

    if "right arrow" in events:
        if pieceposition < max_position - 1:
            gameboard_past[pieceposition] = bg
            pieceposition = pieceposition + 1
        gameboard_past[pieceposition] = gamepiece
        slg.right(15)   

    if "up arrow" in events:
        slg.forward(50)     
    
    if "q" in events:
        gameinprogress = False

    #print(*gameboard_past, sep='')
