def read_input():
    input = []

    f = open("test.txt", "r")
    for line in f:
        l = line.replace("\n", "").replace(":", "").split()
        input.append([int(i) for i in l])
    f.close()

    return input