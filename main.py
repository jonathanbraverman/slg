import time
import event as event

gamepiece = "|"
bg = " "
boardwidth = 30
gameboard_past = [bg for x in range(0,boardwidth)]
gameboard_future = [list() for preview in range(0,4)]
for preview in range(0,4):
    gameboard_future[preview] = [bg for x in range(0, boardwidth)]
pieceposition = 3
max_position = len(gameboard_past)

gameinprogress = True

while gameinprogress:
    time.sleep(0.10)
    events = event.get_events()

    if "left arrow" in events:
        if pieceposition > 0:
            gameboard_past[pieceposition] = bg
            pieceposition = pieceposition - 1
        gameboard_past[pieceposition] = gamepiece
        
    if "right arrow" in events:
        if pieceposition < max_position:
            gameboard_past[pieceposition] = bg
            pieceposition = pieceposition + 1
        gameboard_past[pieceposition] = gamepiece
    
    if "q" in events:
        gameinprogress = False

    print(*gameboard_past, sep='')
