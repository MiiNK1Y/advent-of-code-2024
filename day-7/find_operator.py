from random import random


class FindEquatingOperators:
    def __init__(self, input: list[list[int]]) -> None:
        self._input = input

        self._operators = ["+", "*"]
        self._valid_calibrations = []

        self._current_calibration = []
        self._current_calibration_tried_equation_sets = []

        self._validate_calibrations()

    # TODO:
    # - make combination of equations to evaluate.
    #   - if said evaluation does not equate the calibration, try another combination.

    def _make_equation_set(self) -> list[list[str]]:
        """
        Make a possible equation from a unique set of operators,
        then evaluate the equation.
        If the equation matches the calibration, stop the equation-generation loop.
        """
        ...

    def _make_operator_set(self) -> list[str]:
        """
        Returns a list of a possible operator-combination for the current calibration. 
        """

        operator_combination = []

        # return a random operator from list of operators
        rand = lambda: int(random() * len(self._operators))

        # -result gual num, -first calibration num
        amount_of_needed_operators = len(self._current_calibration) - 2

        operator_combination_is_not_unique = True
        while (operator_combination_is_not_unique):

            for _ in range(amount_of_needed_operators):
                operator_combination.append(rand)

            if operator_combination in self._current_calibration_tried_equation_sets:
                operator_combination.clear()
                continue
            else:
                operator_combination_is_not_unique = False

        return operator_combination


    def _evaluate_operator_set(self) -> int:
        """
        Returns the evaluated set of operators.
        """
        ...

    def _validate_calibrations(self) -> None:
        """
        Checks all the given calibrations and appends all valid calibration measurements to _valid_calibrations.
        """
        for calibration in self._input:
            self._current_calibration = calibration
            ...

    def get_valid_calibrations(self) -> list[int]:
        return self._valid_calibrations
