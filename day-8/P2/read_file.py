def read_file():
    input = []

    with open("input.txt", "r") as f:
        for line in f:
            input.append(line.replace("\n", ""))

    return input
