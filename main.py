import time
import event as event

gamepiece = "|"
bg = " "
boardwidth = 30
previewsize = 4
gameboard_past = [bg for x in range(0,boardwidth)]
gameboard_future = [[bg for x in range(0, boardwidth)] for preview in range(0,previewsize)]
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
        
    if "right arrow" in events:
        if pieceposition < max_position - 1:
            gameboard_past[pieceposition] = bg
            pieceposition = pieceposition + 1
        gameboard_past[pieceposition] = gamepiece
    
    if "q" in events:
        gameinprogress = False

    print(*gameboard_past, sep='')
    #for line_preview in gameboard_future:
    #    print(*line_preview, sep='')
