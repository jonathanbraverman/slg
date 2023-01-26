import time
import keyboard
gamepiece = "|"
gameboard = [" "," ", " ", " "," "]
pieceposition = 3
print(gameboard)

gameinprogress = True

while gameinprogress:
    time.sleep(0.5)
    if keyboard.is_pressed("left arrow"):
        if pieceposition > 0:
            gameboard[pieceposition] = " "
            pieceposition = pieceposition - 1
        gameboard[pieceposition] = gamepiece
        
    