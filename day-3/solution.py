# import time


# findout if a string has a repeating character.
def repeat_char(string, char):
    if string.count(char) > 1:
        return False
    else:
        return True


# check if the passed instructions are valid with the memory spec.
def instruction_is_valid(instruction):
    mul_range = instruction[:4]  # > mul( < xx,xxx)
    mul = "mul(" == mul_range

    comma_range = instruction[5:8]  # mul(x > xx, < xxx)
    comma = "," in comma_range

    closing_range = instruction[-1]  # mul(xxx, > xxx) <
    closing = ")" in closing_range

    if (
        not repeat_char(instruction, "(")
        or not repeat_char(instruction, ",")
        or not repeat_char(instruction, ")")
        or not mul
        or not comma
        or not closing
    ):
        return False

    open_paranthesis_index = instruction.index("(")
    comma_index = instruction.index(",")
    closing_paranthesis_index = instruction.index(")")

    try:
        int(instruction[open_paranthesis_index + 1 : comma_index])
        int(instruction[comma_index + 1 : closing_paranthesis_index])
    except ValueError:
        return False
    else:
        return True


instructions = []


# "sliding window" technique to skim all possible iterations of the instructions.
def sliding_window(input):
    min_window = 8  # mul(x,x)
    max_window = 13  # mul(xxx,xxx)

    current_conditional = "do"  # starting conditional should be "do"

    for i in range(len(input)):
        for j in range(max_window - min_window):
            # extend the window for each possible instruction.
            window = input[i : i + min_window + j]

            if "do()" in window and current_conditional != "do":
                current_conditional = "do"
                # debug
                # print("[O] Conditional: DO <- is set")
                # time.sleep(0.2)

            elif "don't()" in window and current_conditional != "don't":
                current_conditional = "don't"
                # debug
                # print("[X] Conditional: DON'T <- is set")
                # time.sleep(0.2)

            # if the instuction is valid and the conditional allows it to run
            if instruction_is_valid(window) and current_conditional == "do":
                instructions.append(window)
                # debug
                # print(
                #     f"[+] Conditional: DO <- is set, adding {window} to instruction set"
                # )
                # time.sleep(0.2)


# the instructions are eval'ed with this function.
def mul(n1, n2):
    return n1 * n2


def main():
    # get the whole file into memory.
    input = ""
    with open("input.txt", "r") as f:
        input = f.read()
    f.close()

    # skim the string with "sliding window" technique.
    sliding_window(input)

    # get the final sum for each instruction added together.
    sum = 0
    for i in instructions:
        sum += eval(i)

    print(sum)


main()

# PART 1:
# ---------------
# CORRECT ANSWER:
# 164730528
#
# TRIES:
# 1. 3568098
# ---------------
#
# PART 2:
# ---------------
# CORRECT ANSWER:
# 70478672
# 0. First try babyyyy
