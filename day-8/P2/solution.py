from read_file import read_file
from find_antinodes import FindAntinodes


def main():
    input = read_file()
    antinodes = FindAntinodes(input)
    print(len(antinodes.get_antinodes()))
    # print(antinodes.get_antinodes())


if __name__ == "__main__":
    main()
