class seeker:
    def __init__(self, input: str, match: list[str]) -> None:
        self._match = match
        self._width_of_match = max(len(i) for i in self._match)
        self._input_lines = input.splitlines()
        self._height = len(self._input_lines)
        self._width = max(len(i) for i in self._input_lines)

        self._count = 0

        self._make_derivative()

    def get_count(self) -> int:
        return self._count

    def _modify_derivative(self, derivative: str) -> str:
        modified_string = ""
        for i in range(len(derivative)):
            if i % 2 == 0:
                modified_string += derivative[i] + "."

        return modified_string[:-1]

    def _make_derivative(self) -> None:
        for word in self._match:
            window = 3  # x=3 y=3

            for i in range(self._height):
                derivative = self._input_lines[i : i + window]

                to_match = ""
                for j in range(self._width):
                    for k in range(len(derivative)):
                        to_match += derivative[k][j : j + 3]

                        if (
                            len(to_match) == self._width_of_match
                            and self._modify_derivative(to_match) == word
                        ):
                            self._count += 1

                    to_match = ""


input = ""
with open("input.txt") as f:
    input = f.read()
f.close()

# M.S or S.M or S.S or M.M
# .A.    .A.    .A.    .A.
# M.S    S.M    M.M    S.S

find = seeker(input, ["M.S.A.M.S", "S.M.A.S.M", "S.S.A.M.M", "M.M.A.S.S"])

print(find.get_count())

# PART 2:
#
# CORRECT ANSWER:
# 1807
