class UpdateManager:
    def __init__(self, rules: list[list], updates: list[list]) -> None:
        self._rules = rules
        self._updates = updates

        self._first_rules = list(set([rule for [rule, _] in rules]))
        self._second_rules = list(set([rule for [_, rule] in rules]))

        self._good_updates = []
        self._bad_updates = []
        self._current_update = []

        self._set_good_bad_updates()

    def _page_position_legal(self, page: int):
        page_index = self._current_update.index(page)
        scan_len = len(self._current_update) - (page_index + 1)

        for i in range(scan_len):
            second_page = self._current_update[page_index + i + 1]
            pair = [page, second_page]

            if pair not in self._rules:
                return False

        return True

    def _update_is_good(self) -> bool:
        for page in self._current_update[:-1]:
            if not self._page_position_legal(page) or (page not in self._first_rules):
                return False

        return True

    def _set_good_bad_updates(self) -> None:
        for update in self._updates:

            self._current_update = update

            if self._update_is_good():
                self._good_updates.append(update)
            else:
                self._bad_updates.append(update)

    def get_good_updates(self) -> list[list]:
        return self._good_updates

    def get_bad_updates(self) -> list[list]:
        return self._bad_updates


class SortPageUpdates:
    def __init__(self, rules: list[list[int]], update: list[int]) -> None:
        self._rules = rules
        self._updates = update

        self._rule_numbers = []
        self._sorted_pages = []
        
        self._sort_update_pages()

    def _set_rule_numbers(self) -> None:
        for rule in self._rules:
            self._rule_numbers.extend(rule)
        self._rule_numbers = list(set(self._rule_numbers))

    def _sort_update_pages(self) -> None:
        ...

    def get_sorted_pages(self) -> list[int]:
        return self._sorted_pages



class UpdateFixer:
    def __init__(self, rules: list[list[int]], updates: list[list[int]]) -> None:
        self._rules = rules
        self._updates = updates

        self._fixed_bad_updates = []

        self._current_rule_set = []
        self._current_rule_set_numbers_sorted = []

        self._current_update = []

    def _sort_current_rule_set_numbers(self) -> None:
        current_rule_set_numbers_sorted = SortPageUpdates(self._current_rule_set, self._current_update)
        self._current_rule_set_numbers_sorted = current_rule_set_numbers_sorted.get_sorted_pages()

    def _set_current_rule_set(self) -> None:
        for n, page in enumerate(self._current_update[:-1]):
            second_page = self._current_update[n + 1]
            pair = [page, second_page]
            pair_reverse = [second_page, page]
            if pair in self._rules:
                self._current_rule_set.append(pair)
            if pair_reverse in self._rules:
                self._current_rule_set.append(pair_reverse)

    def _set_fixed_bad_updates(self) -> None:
        for update in self._updates:
            self._current_update = update
            self._set_current_rule_set()
            self._sort_current_rule_set_numbers()

    def get_fixed_updates(self) -> list[list[int]]:
        return self._fixed_bad_updates
