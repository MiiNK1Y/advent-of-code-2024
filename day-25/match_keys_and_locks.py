class MatchKeysAndLocks:
    def __init__(self, input: list[str]) -> None:
        self._input = input

        self._height_of_item = 7  # the vertical height of a lock or key.

        self._locks = []
        self._keys = []

        self._matching_pairs = []

        self._sort_locks_and_keys()
        self._match_pairs()

    def _chunk_is_lock(self, chunk) -> bool:
        return chunk[0] == "#####"

    def _sort_locks_and_keys(self) -> None:
        chunk = []

        for line in self._input:
            line = line.replace("\n", "")

            if line != "":
                chunk.append(line)

            if len(chunk) != self._height_of_item:
                continue

            if self._chunk_is_lock(chunk):
                self._locks.append(chunk)
            else:
                self._keys.append(chunk)

            # clear out the appended chunk.
            chunk = []

    # create a list with coordinates where "#" (the object in the grid) occurs.
    def _pattern(self, chunk: list[list[str]]) -> list[list[int]]:
        pattern = []

        for i in range(len(chunk)):
            for j in range(len(chunk[i])):
                if chunk[i][j] == "#":
                    pattern.append([i, j])

        return pattern

    def _pair_is_matching(self, lock: list[list[str]], key: list[list[str]]) -> bool:
        key_pattern = self._pattern(key)
        for i in key_pattern:
            y = i[0]
            x = i[1]
            key_coords = key[y][x]
            lock_coords = lock[y][x]
            if (key_coords == "#") and (lock_coords == "#"):
                return False

        return True

    def _match_pairs(self) -> None:
        for key in self._keys:
            for lock in self._locks:
                if self._pair_is_matching(lock, key) and [lock, key] not in self._matching_pairs:
                    self._matching_pairs.append([lock, key])

    def get_locks(self) -> list[list[str]]:
        return self._locks

    def get_keys(self) -> list[list[str]]:
        return self._keys

    def get_matching_pairs(self) -> list[list[int]]:
        return self._matching_pairs
