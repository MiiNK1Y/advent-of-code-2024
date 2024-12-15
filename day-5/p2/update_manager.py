import debugger

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
        debugger.debug("log", "page_position_legal()")

        page_index = self._current_update.index(page)
        scan_len = len(self._current_update) - (page_index + 1)

        for i in range(scan_len):
            second_page = self._current_update[page_index + i + 1]
            pair = [page, second_page]

            if pair not in self._rules:
                return False

        return True

    def _update_is_good(self) -> bool:
        debugger.debug("log", "_update_is_good()")

        for page in self._current_update[:-1]:
            if not self._page_position_legal(page) or (page not in self._first_rules):
                return False

        return True

    def _set_good_bad_updates(self) -> None:
        debugger.debug("log", "_set_good_bad_updates()")

        for update in self._updates:

            self._current_update = update

            if self._update_is_good():
                self._good_updates.append(update)
            else:
                self._bad_updates.append(update)

    def get_good_updates(self) -> list[list]:
        debugger.debug("log", "_get_good_updates()")

        return self._good_updates

    def get_bad_updates(self) -> list[list]:
        debugger.debug("log", "_get_bad_updates()")

        return self._bad_updates


class SortPageRules:
    def __init__(self, rules: list[list[int]], update: list[int]) -> None:
        self._rules = rules
        self._updates = update

        self._first_rules = list(set([rule for [rule, _] in rules]))
        self._second_rules = list(set([rule for [_, rule] in rules]))
        self._rule_numbers = []
        self._sorted_rule_numbers = []

        self._set_rule_numbers()
        self._set_sorted_rule_numbers()

    def _set_rule_numbers(self) -> None:
        debugger.debug("log", "_set_rule_numbers()")

        for page in self._rules:
            self._rule_numbers.extend(page)
        self._rule_numbers = list(set(self._rule_numbers))

    def _has_multiple_prefix_rules(self, rule: int) -> list:
        debugger.debug("log", "_has_multiple_prefix_rules()")

        prefix_rules = []
        for pair in self._rules:
            if pair[1] == rule:
                prefix_rules.append(pair[0])
                debugger.debug("data", f"{rule} has this prefix:", pair[0])
        return prefix_rules

    def _prefixes_in_sorted_rule_numbers(self, prefixes: list[int]) -> bool:
        debugger.debug("log", "_prefixes_in_sorted_rule_numbers()")

        for prefix in prefixes:
            if prefix not in self._sorted_rule_numbers:
                return False
        return True

    def _set_sorted_rule_numbers(self) -> None:
        debugger.debug("log", "_set_sorted_rule_numbers()")

        only_suffix = []

        debugger.debug("data", "unmanaged rules:", self._rules)
        debugger.debug("data", "unsorted rules:", self._rule_numbers)
        debugger.debug("data", "current FIRST rule-set:", self._first_rules)
        debugger.debug("data", "current SECOND rule-set:", self._second_rules)

        while (len(self._sorted_rule_numbers) + len(only_suffix) != len(self._rule_numbers)):

            for page in self._rule_numbers:
                debugger.debug("data", "currently working on this rule:", page)
                if page in self._sorted_rule_numbers or page in only_suffix:
                    debugger.debug("data", f"{page} is accounted for, skipping...")
                    continue

                elif page not in self._first_rules and page in self._second_rules:
                    debugger.debug("data", f"{page} only has a suffix, adding to 'only_suffix'")
                    only_suffix.append(page)

                else:
                    prefix_rules = self._has_multiple_prefix_rules(page)
                    if self._prefixes_in_sorted_rule_numbers(prefix_rules):
                        debugger.debug("data", f"{page} has these prefixes: {prefix_rules} and they are already sorted! Adding...")
                        self._sorted_rule_numbers.append(page)

        if len(only_suffix) > 0:
            self._sorted_rule_numbers.extend(only_suffix)

    def get_sorted_rules(self) -> list[int]:
        debugger.debug("log", "_get_sorted_rules()")

        return self._sorted_rule_numbers


class UpdateFixer:
    def __init__(self, rules: list[list[int]], updates: list[list[int]]) -> None:
        self._rules = rules
        self._updates = updates

        self._fixed_bad_updates = []

        self._current_rule_set = []
        self._current_rule_set_numbers_sorted = []

        self._current_update = []
        self._current_update_sorted = []

        self._set_fixed_bad_updates()

    def _flush_temp_values(self) -> None:
        debugger.debug("log", "_flush_temp_values()")

        self._current_rule_set = []
        self._current_rule_set_numbers_sorted = []
        self._current_update = []
        self._current_update_sorted = []

    def _set_current_update_sorted(self) -> None:
        debugger.debug("log", "_set_current_update_sorted()")
        debugger.debug("data","matching update against these rules:", self._current_rule_set_numbers_sorted)

        self._current_update_sorted = [page for page in self._current_rule_set_numbers_sorted if page in self._current_update]
        self._current_update_sorted.extend([page for page in self._current_update if page not in self._current_update_sorted])

        debugger.debug("data","sorted update pages:", self._current_update_sorted)

    def _set_current_rule_set_numbers_sorted(self) -> None:
        debugger.debug("log", "_set_current_rule_set_numbers_sorted()")

        current_rule_set_numbers_sorted = SortPageRules(self._current_rule_set, self._current_update)
        self._current_rule_set_numbers_sorted = current_rule_set_numbers_sorted.get_sorted_rules()

    def _set_current_rule_set(self) -> None:
        debugger.debug("log", "_set_current_rule_set()")

        # DOES NOT ACCOUNT FOR ALL POSSIBLE OCCURENCES OF A RULE, REWRITE!!
        # for n, page in enumerate(self._current_update[:-1]):
        #     second_page = self._current_update[n + 1]
        #     pair = [page, second_page]
        #     pair_reverse = [second_page, page]
        #     debugger.debug("data", f"looking for rules for {pair} and {pair_reverse}")

        #     if pair in self._rules:
        #         debugger.debug("data", f"found {pair} in: ", self._rules)
        #         self._current_rule_set.append(pair)

        #     if pair_reverse in self._rules:
        #         debugger.debug("data", f"found {pair_reverse} in: ", self._rules)
        #         self._current_rule_set.append(pair_reverse)


        for page1 in self._current_update:
            for page2 in self._current_update:
                pair = [page1, page2]
                pair_reverse = [page2, page1]

                if page1 == page2:
                    continue

                debugger.debug("data", f"looking for rules for {pair} and {pair_reverse}")

                if pair in self._rules:
                    debugger.debug("data", f"found {pair}")
                    self._current_rule_set.append(pair)

                if pair_reverse in self._rules:
                    debugger.debug("data", f"found {pair_reverse}")
                    self._current_rule_set.append(pair_reverse)


    def _set_fixed_bad_updates(self) -> None:
        debugger.debug("log", "_set_fixed_bad_updates()")

        for update in self._updates:
            self._current_update = update

            self._set_current_rule_set()
            self._set_current_rule_set_numbers_sorted()
            self._set_current_update_sorted()

            self._fixed_bad_updates.append(self._current_update_sorted)

            self._flush_temp_values()

    def get_fixed_updates(self) -> list[list[int]]:
        debugger.debug("log", "_get_fixed_updates()")

        return self._fixed_bad_updates
