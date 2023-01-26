import keyboard

def get_events():
    return_value = []

    if keyboard.is_pressed("left arrow"):
        return_value.append("left arrow")

    if keyboard.is_pressed("right arrow"):
        return_value.append("right arrow")

    if keyboard.is_pressed("up arrow"):
        return_value.append("up arrow")

    return return_value