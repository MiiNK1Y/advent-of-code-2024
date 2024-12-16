import time
import os


def draw_predicted_path(map, y, x, direction) -> None:
    match direction:
        case "north":
            symbol = "^"
        case "east":
            symbol = ">"
        case "south":
            symbol = "v"
        case "west":
            symbol = "<"
        case _:
            symbol = "%"

    predicted_path = map.copy()
    print(predicted_path)
    print(y, x)

    guard_at_x = predicted_path[y]
    guard_symbol_at_x = guard_at_x[:x] + symbol + guard_at_x[x + 1:]
    predicted_path[y] = guard_symbol_at_x

    for i in predicted_path:
        print(i)
    time.sleep(0.1)
    os.system("clear")
