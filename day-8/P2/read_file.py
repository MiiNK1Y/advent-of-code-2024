def read_file():
    input = []

    with open("input.txt", "r") as f:
        for line in f:
            input.append(line.replace("\n", ""))

    return input


def read_example():
    input = []

    with open("test_filled.txt", "r") as f:
        for line in f:
            input.append(line.replace("\n", ""))

    return input
