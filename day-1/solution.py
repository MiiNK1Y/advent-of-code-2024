# NEEDED FOR PART 1 AND 2

l1 = []
l2 = []

# get input from AoC by reading input.txt
with open("input.txt", "r") as f:
    for line in f:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))
f.close()

# sort the input lists
l1s = sorted(l1)
l2s = sorted(l2)


# PART 1
# sum the difference between the pairs
# sum = 0
# for i in range(len(l1s)):
#    nums = sorted([l1s[i], l2s[i]])
#    sum += nums[1] - nums[0]
#
# print(sum)


# PART 2
similarity_score = 0
for i in l1s:
    for j in l2s:
        if i == j:
            similarity_score += j

print(similarity_score)
