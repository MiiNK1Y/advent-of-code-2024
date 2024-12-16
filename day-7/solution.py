from read_input import read_input
from find_operator import FindEquatingOperators


def main():
    input = read_input()

    find_operators = FindEquatingOperators(input)
    valid_calibrations = find_operators.get_valid_calibrations()

    print(sum(valid_calibrations))


if __name__ == '__main__':
    main()
