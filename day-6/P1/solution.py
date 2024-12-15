from read_file import read_file
from map import Map


def main():
    input = read_file()
    map = Map(input)
    print(map.get_distinct_position())


if __name__ == '__main__':
    main()
