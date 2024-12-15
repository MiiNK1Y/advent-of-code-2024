import debugger


class Map:
    def __init__(self, map: list[str]) -> None:
        self._map = map

        self._current_char = "" # the char found at the X-Y axis.
        self._curret_x = 0      # horizontal axis, AKA: a singe array.
        self._current_y = 0     # vertical axis, AKA: all arrays.
        self._current_looking_direction = "" # north, south, east, west.
        self._distinct_positions = []
        self._path_complete = False

        self._set_initial_x_y()
        self._set_initial_direction()
        self._start()

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
                self._current_x = x.index("^")
                self._current_y = n
            except ValueError:
                continue

    def _add_distinct_position(self) -> None:
        position = [self._current_y, self._current_x]
        if position not in self._distinct_positions:
            self._distinct_positions.append(position)

    def _obstruction(self) -> bool:
        obstruction = "#"
        try:
            self._current_char = self._map[self._current_y][self._current_x]
        except IndexError:
            self._path_complete = True
            return False
        return self._current_char == obstruction

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

    def _start(self) -> None:
        while (not self._path_complete):
            #debugger.draw_predicted_path(self._map, self._current_y, self._current_x, self._current_looking_direction)
            self._move()

    def get_distinct_position(self) -> int:
        return len(self._distinct_positions) - 1
