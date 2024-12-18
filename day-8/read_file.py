def read_file():
    input = []

    with open("stuff/test.txt", "r") as f:
        for line in f:
            input.append(line.replace("\n", ""))

    return input
