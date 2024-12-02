# PART 1
# CORRECT ANSWER: 423


# get input from AoC by reading input.txt
li = []
with open("input.txt", "r") as f:
    for line in f:
        t = []
        for i in line.split():
            t.append(int(i))  # convert string input to int
        li.append(t)
f.close()


li_s = [sorted(i) for i in li]  # subarrays are sorted increasingly
li_r = [sorted(i, reverse=True) for i in li]  # subarrays are sorted decreasingly


# new list with only increasing or decreasing subarrays
li_m = [i for n, i in enumerate(li) if (li[n] == li_s[n]) or (li[n] == li_r[n])]


# check that every item in the list is within a distance of (n <= 3) of eachother.
def check_list(li):
    t = 0
    for n, j in enumerate(li):
        if n == 0:
            t = j
            continue

        match = max(t, j) - min(t, j)
        if match <= 3 and match > 0:
            t = j
        else:
            return False

    return True


# find amount of lists that match the criteria of the challenge
final = 0
for i in li_m:
    if check_list(i):
        final += 1


print(final)
