from read_file import read_file
from find_antinodes import FindAntinodes


def main():
    input = read_file()
    antinodes = FindAntinodes(input)
    # print(antinodes.get_antinodes())
    # print(antinodes.get_all_frequencies())
    print(antinodes.get_antinodes_count())


if __name__ == "__main__":
    main()

# NOTE:
# 1257 is too low!
# 1317 is too high!
# 1272 is too low!
