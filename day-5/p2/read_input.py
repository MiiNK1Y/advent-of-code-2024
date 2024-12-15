# get the input into memory, sort the different input types.
def read_input() -> list[list]:
    rules = []
    updates = []
    f = open("stuff/input.txt", "r")

    for line in f:
        line = line.replace("\n", "")
        if "|" in line:
            rule = line.split("|")
            rules.append([int(i) for i in rule])
        elif "," in line:
            page = line.split(",")
            updates.append([int(i) for i in page])
        else:
            continue

    f.close()

    return [rules, updates]
