#import keyboard

def get_events():
    return_value = []
    left = False
    right = False
    up = False

    if left:
        return_value.append("left arrow")

    if right:
        return_value.append("right arrow")

    if up:
        return_value.append("up arrow")

    return return_value