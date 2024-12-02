# PART 2
# CORRECT ANSWER: 488
#
# FAILED ATTEMPTS:
# 1. 724
# 2. 569
# 3. 457
# 4. 747

# check that every item in the list is within a distance of (n <= 3) of eachother.
def check_list(my_list):
    tmp = 0
    for n, i in enumerate(my_list):
        if n == 0:
            tmp = i
            continue

        math = tmp - i
        if math <= 3 and math > 0:
            tmp = i
            continue
        else:
            return False
    return True


# try to get a list that matches the criteria by removing one item at a time
def try_remove_one(my_list):
    for i in range(len(my_list)):
        new_list = my_list.copy()
        del new_list[i]
        # check the list reversed aswell, to cover decreasing lists
        if check_list(new_list) or check_list(new_list[::-1]):
            return True
        else:
            continue
    return False


# get input from AoC by reading input.txt
input_list = []
with open("input.txt", "r") as f:
    for line in f:
        tmp = []
        for i in line.split():
            tmp.append(int(i))
        input_list.append(tmp)
f.close()


# check every subarray, then finalize
input_list_filtered = []
for i in input_list:
    if try_remove_one(i):
        input_list_filtered.append(i)


# show the final length of the filtered list
print(len(input_list_filtered))
