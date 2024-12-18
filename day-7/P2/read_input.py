def read_input():
    input = []

    f = open("./input.txt", "r")
    for line in f:
        l = line.replace("\n", "").replace(":", "").split()
        input.append([int(i) for i in l])
    f.close()

    input.sort(key=len)

    return input
