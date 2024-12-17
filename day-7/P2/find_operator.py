from random import random
from debugger import debug


class FindEquatingOperators:
    def __init__(self, input: list[list[int]]) -> None:
        self._input = input

        self._operators = ["+", "*"]
        self._valid_calibrations = []
        self._current_calibration = []
        self._current_calibration_tried_equation_sets = []
        self._amount_of_needed_operators = 0
        self._amount_of_unique_operator_sets = 0

        self._validate_calibrations()

    def _make_operator_set(self) -> list[str]:
        """
        Returns a list of a possible operator-combination for the current calibration. 
        """
        operator_combination = []

        operator_combination_is_not_unique = True
        while (operator_combination_is_not_unique):

            for _ in range(self._amount_of_needed_operators):
                operator_combination.append(self._operators[int(random() * len(self._operators))])

            if operator_combination in self._current_calibration_tried_equation_sets:
                operator_combination.clear()
                continue
            else:
                self._current_calibration_tried_equation_sets.append(operator_combination)
                operator_combination_is_not_unique = False

        return operator_combination

    def _make_equation_set(self) -> int:
        """
        Make a possible equation from a unique set of operators,
        then evaluate the equation.
        If the equation matches the calibration, stop the equation-generation loop.
        """
        equation_set = str(self._current_calibration[1])
        operator_set = self._make_operator_set()

        for i in range(self._amount_of_needed_operators):
            equation_set = str(eval(str(equation_set) + str(operator_set[i]) + str(self._current_calibration[2 + i])))

        return eval(equation_set)

    def _validate_calibrations(self) -> None:
        """
        Checks all the given calibrations and appends all valid calibration measurements to _valid_calibrations.
        """
        for calibration in self._input:
            self._current_calibration_tried_equation_sets.clear()
            self._current_calibration = calibration

            # -result gual num, -first calibration num
            self._amount_of_needed_operators = len(self._current_calibration) - 2
            self._amount_of_unique_operator_sets = len(self._operators) ** self._amount_of_needed_operators

            for _ in range(self._amount_of_unique_operator_sets):
                if (self._make_equation_set() == calibration[0]):
                    self._valid_calibrations.append(calibration[0])
                    break

    def get_valid_calibrations(self) -> list[int]:
        return self._valid_calibrations
