import debugger


class Map:
    def __init__(self, map: list[str]) -> None:
        self._map_original = map
        self._map = map

        self._current_char = "" # the char found at the X-Y axis.
        self._curret_x = 0      # horizontal axis, AKA: a singe array.
        self._current_y = 0     # vertical axis, AKA: all arrays.
        self._current_looking_direction = "" # north, south, east, west.
        self._distinct_positions = []
        self._path_complete = False
        self._steps = 0

        # part 2
        self._looping_obstructions = 0
        self._current_obstruction = []
        self._initial_x = 0
        self._initial_y = 0

        self._set_initial_x_y()
        self._set_initial_direction()
        self._start_path_finding()

        # part 2
        self._check_obstructions_creates_loops()

    def _set_initial_direction(self) -> None:
        self._current_char = self._map[self._current_y][self._current_x]
        match self._current_char:
            case "^": self._current_looking_direction = "north"
            case ">": self._current_looking_direction = "east"
            case "v": self._current_looking_direction = "south"
            case "<": self._current_looking_direction = "west"

    def _set_initial_x_y(self) -> None:
        for n, x in enumerate(self._map):
            try:
                self._current_x = self._initial_x = x.index("^")
                self._current_y = self._initial_y = n
            except ValueError:
                continue

    def _add_distinct_position(self) -> None:
        self._steps += 1
        position = [self._current_y, self._current_x]
        if position not in self._distinct_positions:
            self._distinct_positions.append(position)

    def _obstruction(self) -> bool:
        obstruction = "#"
        placed_obstruction = "O"
        try:
            self._current_char = self._map[self._current_y][self._current_x]
        except IndexError:
            self._path_complete = True
            return False
        return self._current_char == obstruction or self._current_char == placed_obstruction

    def _change_direction(self) -> None:
        match self._current_looking_direction:
            case "north": self._current_looking_direction = "east"
            case "east": self._current_looking_direction = "south"
            case "south": self._current_looking_direction = "west"
            case "west": self._current_looking_direction = "north"

    def _move(self) -> None:
        match self._current_looking_direction:
            case "north":
                self._current_y -= 1
                if self._obstruction():
                    self._current_y += 1
                    self._change_direction()
                else:
                    self._add_distinct_position()
            case "east":
                self._current_x += 1
                if self._obstruction():
                    self._current_x -= 1
                    self._change_direction()
                else:
                    self._add_distinct_position()
            case "south":
                self._current_y += 1
                if self._obstruction():
                    self._current_y -= 1
                    self._change_direction()
                else:
                    self._add_distinct_position()
            case "west":
                self._current_x -= 1
                if self._obstruction():
                    self._current_x += 1
                    self._change_direction()
                else:
                    self._add_distinct_position()

    def _start_path_finding(self) -> None:
        while (not self._path_complete):
            debugger.draw_predicted_path(self._map, self._current_y, self._current_x, self._current_looking_direction)
            self._move()

    def get_distinct_position(self) -> int:
        return len(self._distinct_positions) - 1

    # part 2
    def _placed_obstruction(self) -> bool:
        obstruction = "#"
        placed_obstruction = "O"
        try:
            self._current_char = self._map[self._current_y][self._current_x]
        except IndexError:
            self._path_complete = True
            return False
        return self._current_char == obstruction or self._current_char == placed_obstruction

    def _location_out_of_bounds(self) -> bool:
        x_len = len(self._map[0]) - 1
        y_len = len(self._map) - 1
        if (
            self._current_y > y_len or
            self._current_y < 0 or
            self._current_x > x_len or
            self._current_x < 0
        ):
            return True
        else:
            return False

    def _move_with_obstructions(self) -> None:
        match self._current_looking_direction:
            case "north":
                self._current_y -= 1
                if self._location_out_of_bounds():
                    raise IndexError
                if self._placed_obstruction():
                    self._current_y += 1
                    self._change_direction()
            case "east":
                self._current_x += 1
                if self._location_out_of_bounds():
                    raise IndexError
                if self._placed_obstruction():
                    self._current_x -= 1
                    self._change_direction()
            case "south":
                self._current_y += 1
                if self._location_out_of_bounds():
                    raise IndexError
                if self._placed_obstruction():
                    self._current_y -= 1
                    self._change_direction()
            case "west":
                self._current_x -= 1
                if self._location_out_of_bounds():
                    raise IndexError
                if self._placed_obstruction():
                    self._current_x += 1
                    self._change_direction()

    def _modify_map_with_obstruction(self) -> None:
        y = self._current_obstruction[0]
        x = self._current_obstruction[1]
        new_map = self._map_original.copy()
        obsticle_at_x = new_map[y]
        obsticle_symbol_at_x = obsticle_at_x[:x] + "O" + obsticle_at_x[x + 1:]
        new_map[y] = obsticle_symbol_at_x
        self._map = new_map

    def _check_obstructions_creates_loops(self) -> None:
        for obstructed_path in self._distinct_positions[:-1]:
            self._current_x = self._initial_x
            self._current_y = self._initial_y

            self._set_initial_direction()

            self._current_obstruction = obstructed_path

            if self._current_obstruction == [self._initial_y, self._initial_x]:
                continue

            self._modify_map_with_obstruction()

            for i in range(self._steps * 2):
                try:
                    self._move_with_obstructions()
                    if i == ((self._steps * 2) - 1):
                        self._looping_obstructions += 1
                except IndexError:
                    break

                debugger.draw_predicted_path(self._map, self._current_y, self._current_x, self._current_looking_direction)

    def get_looping_obstrucions(self) -> int:
        return self._looping_obstructions
