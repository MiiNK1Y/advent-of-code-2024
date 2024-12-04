class seeker:
    def __init__(self, input: str, words: list[str]) -> None:
        self._input = input
        self._words = words

        self._input_lines = input.splitlines()
        self._height = len(self._input_lines)
        self._width = max(len(i) for i in self._input_lines)

        self._count = 0

        self._count_horizontal()
        self._count_vertical()
        self._count_diagonal()

    def get_count(self) -> int:
        return self._count

    def _count_horizontal(self) -> None:
        for word in self._words:
            for j in self._input_lines:
                self._count += j.count(word)

    def _count_vertical(self) -> None:
        for word in self._words:
            for j in range(self._width):
                vertical = ""
                for k in range(self._height):
                    vertical += self._input_lines[k][j]
                self._count += vertical.count(word)

    def _get_word_from_diagonal(self, word: str, lines: list[str]):
        count = 0

        # the vertical word built from the crimped 2D array
        diagonal_word = ""  # \

        for i in range(self._width):
            # make the window diagonal, deviate +1 every new line
            diagonal_deviation = 0

            for j in range(len(lines)):
                try:
                    char = lines[j][i + diagonal_deviation]
                except IndexError:
                    return count

                diagonal_word += char
                diagonal_deviation += 1

                if len(diagonal_word) == len(word):
                    if diagonal_word == word:
                        count += 1
                    diagonal_word = ""
                    diagonal_deviation = 0
        return count

    def _get_word_from_diagonal_r(self, word: str, lines: list[str]):
        count = 0

        # the vertical word built from the crimped 2D array
        diagonal_word = ""  # /

        for i in range(self._width):
            # make the window diagonal, deviate -1 every new line
            diagonal_deviation = len(word) - 1

            for j in range(len(lines)):
                try:
                    char = lines[j][i + diagonal_deviation]
                except IndexError:
                    return count

                diagonal_word += char
                diagonal_deviation -= 1

                if len(diagonal_word) == len(word):
                    if diagonal_word == word:
                        count += 1
                    diagonal_word = ""
                    diagonal_deviation = len(word) - 1
        return count

    def _count_diagonal(self) -> None:
        for i in self._words:
            window = len(i)
            for j in range((self._height - window) * self._width):
                # break down the 2D array to fit the sliding window
                lines = self._input_lines[j : j + window]

                # if the 2D array is smalled than the window,
                # it means we are nearing the end and there is no more room for the word.
                if len(lines) < window:
                    break
                self._count += self._get_word_from_diagonal(i, lines)
                self._count += self._get_word_from_diagonal_r(i, lines)


input = ""
with open("input.txt") as f:
    input = f.read()
f.close()

find = seeker(input, ["XMAS", "SAMX"])

print(find.get_count())

# PART 1:
#
# CORRECT ANSWER:
# 2406
