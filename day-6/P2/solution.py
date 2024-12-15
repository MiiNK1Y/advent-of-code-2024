from read_file import read_file
from map import Map


def main():
    input = read_file()
    map = Map(input)
    print("distinct positions:", map.get_distinct_position())
    print("obstruction positions creates loops:", map.get_looping_obstrucions())


if __name__ == '__main__':
    main()
