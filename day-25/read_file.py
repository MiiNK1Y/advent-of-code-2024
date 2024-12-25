def read_input() -> list[str]:
    input = []

    f = open("input.txt", "r")
    input = f.readlines()
    f.close()

    return input
