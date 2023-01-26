import time
import event_test as event

gamepiece = "|"
gameboard = [" "," ", " ", " "," "]
pieceposition = 3
max_position = len(gameboard)
print(gameboard)

gameinprogress = True

while gameinprogress:
    time.sleep(0.5)
    events = event.get_events()

    if "left arrow" in events:
        if pieceposition > 0:
            gameboard[pieceposition] = " "
            pieceposition = pieceposition - 1
        gameboard[pieceposition] = gamepiece
        
    if "right arrow" in events:
        if pieceposition < max_position:
            gameboard[pieceposition] = " "
            pieceposition = pieceposition - 1
        gameboard[pieceposition] = gamepiece
    
    if "up arrow" in events:
        gameinprogress = False