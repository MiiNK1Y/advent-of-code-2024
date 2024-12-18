class FindEquatingOperators:
    def __init__(self, input: list[list[int]]) -> None:
        self._input = input

        self._operators = ["+", "*", "|"]
        self._valid_calibrations = []

        self._current_calibration = []
        self._current_operator_sets = []
        self._amount_of_needed_operators = 0

        self._validate_calibrations()


    def _make_operator_sets(self, prefix, n):
        if (n == 0):
            self._current_operator_sets.append(prefix)
            return
        
        for i in range(len(self._operators)):
            new_prefix = prefix + self._operators[i]
            self._make_operator_sets(new_prefix, n - 1)


    def _check_operator_sets(self) -> None:
        operators_not_same = (len(self._operators) ** self._amount_of_needed_operators) != len(self._current_operator_sets)
        if operators_not_same:
            self._current_operator_sets.clear()
            self._make_operator_sets("", self._amount_of_needed_operators)


    def _found_equation(self) -> bool:
        self._check_operator_sets()

        for operators in self._current_operator_sets:
            equate = str(self._current_calibration[1])

            for n, operator in enumerate(operators):
                current_num = str(self._current_calibration[2 + n])

                if (operator == "|"):
                    equate = str(eval(equate + current_num))
                else:
                    equate = str(eval(equate + operator + current_num))

            evaulated = eval(equate)

            if evaulated == self._current_calibration[0]:
                print(f"FOUND: {evaulated}")

                return True
        
        return False


    def _validate_calibrations(self) -> None:
        for n, calibration in enumerate(self._input):
            goal = calibration[0]
            self._current_calibration = calibration
            self._amount_of_needed_operators = len(self._current_calibration) - 2

            progress = f"{n + 1}/{len(self._input)}"
            print(f"\tIndex [{progress}]: {calibration}")

            if self._found_equation():
                self._valid_calibrations.append(goal)


    def get_valid_calibrations(self) -> list[int]:
        return self._valid_calibrations
