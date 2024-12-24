class FindAntinodes:
    def __init__(self, map: list[str]) -> None:
        self._map = map
        self._count_antinodes = 0
        self._antinodes = []
        self._antennas = {}

        self._current_key = ""

        self._set_all_possible_frequencies()
        print(self._antennas)
        self._set_count_antinodes()

    # frequencies are represented by a char, collect all the possible ones in a set,
    # bundeling the coordinates in a list within a list.
    def _set_all_possible_frequencies(self) -> None:
        length_of_map_y = range(len(self._map))

        for y in length_of_map_y:
            length_of_map_x = range(len(self._map[y]))

            for x in length_of_map_x:
                keys = self._antennas.keys()
                map_item = self._map[y][x]

                if map_item == ".":
                    continue

                item_coordinates = [y, x]

                # setting all the antennas on tha map:
                if map_item not in keys:
                    self._antennas[map_item] = [item_coordinates]

                else:
                    self._antennas[map_item].append(item_coordinates)

    # check if an antinode is out-of-bouds of the map, making it not count.
    def _is_antinode_inside_bounds(self, antinode: list[int]) -> bool:
        antinode_y = antinode[0]
        antinode_x = antinode[1]

        height_of_map = len(self._map)
        width_of_map = len(self._map[0])

        antinode_y_within_bounds = antinode_y < height_of_map and antinode_y >= 0
        antinode_x_within_bounds = antinode_x < width_of_map and antinode_x >= 0

        if antinode_y_within_bounds and antinode_x_within_bounds:
            return True

        print("antinode:", antinode, "is outside of bounds!")
        return False

    def _append_new_antinode_pair(self, antinodes: list[list[int]]) -> None:
        for antinode in antinodes:
            if self._is_antinode_inside_bounds(antinode) and antinode not in self._antinodes:
                self._antinodes.append(antinode)

    def _deviation(self, xy1, xy2) -> int:
        return max(xy1, xy2) - min(xy1, xy2)

    # return the position of the two antinodes.
    def _antinode_coordinates(self, ant1: list[int], ant2: list[int]) -> list[list[int]]:
        # find the deviation of a possible antinode
        deviation_y = self._deviation(ant1[0], ant2[0])
        deviation_x = self._deviation(ant1[1], ant2[1])

        top_antenna = ant1 if (ant1[0] <= ant2[0]) else ant2
        bottom_antenna = ant2 if top_antenna == ant1 else ant1

        antinode_1_y = (top_antenna[0] - deviation_y)
        antinode_1_x = (top_antenna[1] - deviation_x) if top_antenna[1] <= bottom_antenna[1] else (top_antenna[1] + deviation_x)

        antinode_2_y = (bottom_antenna[0] + deviation_y)
        antinode_2_x = (bottom_antenna[1] + deviation_x) if bottom_antenna[1] >= top_antenna[1] else (bottom_antenna[1] - deviation_x)

        return [[antinode_1_y, antinode_1_x], [antinode_2_y, antinode_2_x]]


    # the legal position of a node is the mirrored location of an adjacent node, making two antinodes.
    def _find_antinodes(self, key: str) -> None:
        for antenna in self._antennas[key]:
            print()

            for adjacent_antenna in self._antennas[key]:
                print("working with antenna:", antenna)
                print("working with adjacent antenna:", adjacent_antenna)

                if antenna == adjacent_antenna:
                    print("cheking own antenna, skipping")
                    continue

                antinode_pair = self._antinode_coordinates(antenna, adjacent_antenna)
                print("current antinode pair: ", antinode_pair)
                self._append_new_antinode_pair(antinode_pair)

    # count all the antinodes and store them in a class-set with coordinates.
    def _set_count_antinodes(self) -> None:
        for key in self._antennas:
            print("working with freqency:", key)
            if len(self._antennas[key]) == 1:
                continue

            self._find_antinodes(key)

        self._count_antinodes = len(self._antinodes)

    def get_antinodes(self) -> list[list[int]]:
        return self._antinodes