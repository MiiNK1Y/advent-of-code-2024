import time


class SortRules:
    def __init__(self, rules: list[list]) -> None:
        self._rules = rules
        self._array_of_all_numbers = []
        self._sorted_rule_array = []
        self._no_prefix_still_suffix = []

        self._collect_all_numbers()
        self._sort_all_collected_numbers()

    def get_sorted_rule_array(self) -> list[int]:
        return self._sorted_rule_array

    def get_array_of_all_numbers(self) -> list[int]:
        return self._array_of_all_numbers

    def _collect_all_numbers(self) -> None:
        temp = []
        for subarray in self._rules:
            temp.extend(subarray)
        self._array_of_all_numbers = list(set(temp))

    def _has_prefix_rule(self, rule: int) -> bool:
        for first in self._rules:
            if rule == first[0]:
                return True
        return False

    def _has_suffix_rule(self, rule: int) -> bool:
        for second in self._rules:
            if rule == second[1]:
                return True
        return False

    def _has_multiple_prefix_rules(self, rule: int) -> list:
        prefix_rules = []
        for pair in self._rules:
            if pair[1] == rule:
                prefix_rules.append(pair[0])
        return prefix_rules

    def _prefixes_in_array(self, prefixes: list[int]) -> bool:
        print(prefixes)
        for prefix in prefixes:
            if prefix not in self._sorted_rule_array:
                return False
        return True

    # def _all_nums_accounted_for(self) -> bool:
    #    for i in self._array_of_all_numbers:
    #        if i in self._sorted_rule_array:
    #            continue
    #        elif i in self._no_prefix_still_suffix:
    #            continue
    #        else:
    #            return False
    #    return True

    def _sort_all_collected_numbers(self) -> None:
        while len(self._array_of_all_numbers) != len(self._sorted_rule_array) + len(
            self._no_prefix_still_suffix
        ):
            print(f"current sorted list:{self._sorted_rule_array}", end=" \r")
            # if self._all_nums_accounted_for():
            #    break

            for i in self._array_of_all_numbers:
                if i in self._sorted_rule_array or i in self._no_prefix_still_suffix:
                    continue

                elif not self._has_prefix_rule(i) and self._has_suffix_rule(i):
                    self._no_prefix_still_suffix.append(i)

                else:
                    prefix_rules = self._has_multiple_prefix_rules(i)
                    if self._prefixes_in_array(prefix_rules):
                        self._sorted_rule_array.append(i)

        if len(self._no_prefix_still_suffix) > 0:
            self._sorted_rule_array.extend(self._no_prefix_still_suffix)


class Ordering:
    def __init__(self, rules: list[list], updates: list[list]) -> None:
        self._rules = rules
        self._updates = updates
        self._ordered_pages = []
        self._rules_length = len(rules)
        self._middle_page_numbers = []
        self._middle_page_number_sum = 0

        # part 2
        self._wrong_ordered_pages = []
        self._fixed_ordered_pages = []

        self._count_ordered_pages()
        self._collect_middle_page_number()
        self._sum_middle_page_numbers()
        # self._sort_wrong_ordered_pages()

    def get_ordered_pages(self) -> list[list]:
        return self._ordered_pages

    def get_wrong_ordered_pages(self) -> list:
        return self._wrong_ordered_pages

    def get_middle_page_numbers(self) -> list:
        return self._middle_page_numbers

    def get_middle_page_number_sum(self) -> int:
        return self._middle_page_number_sum

    def _sum_middle_page_numbers(self) -> None:
        self._middle_page_number_sum = sum(self._middle_page_numbers)

    def _collect_middle_page_number(self) -> None:
        for page in self._ordered_pages:
            self._middle_page_numbers.append(page[len(page) // 2])

    # check if the current page has rules for what should be in front of (p1|p2).
    def _check_page_has_first_rule(self, page) -> bool:
        for rule in self._rules:
            if page == rule[0]:
                return True
        return False

    def _check_if_pair_is_in_rules(self, pair) -> bool:
        for rule in self._rules:
            if pair == str(rule[0]) + str(rule[1]):
                return True
        return False

    def _is_page_position_legal(self, update, page_index) -> bool:
        legal = False
        for i in range(len(update) - (page_index + 1)):
            pair = str(update[page_index]) + str(update[page_index + i + 1])
            if self._check_if_pair_is_in_rules(pair):
                legal = True
            else:
                return False
        return legal

    def _check_rule_with_page(self, update) -> bool:
        legal = False
        for n, page in enumerate(update[:-1]):
            if self._check_page_has_first_rule(page) and self._is_page_position_legal(
                update, n
            ):
                legal = True
            else:
                return False
        return legal

    def _count_ordered_pages(self) -> None:
        for update in self._updates:
            if self._check_rule_with_page(update):
                self._ordered_pages.append(update)
            else:
                self._wrong_ordered_pages.append(update)


class SortUpdatesByRules:
    def __init__(self, updates: list[list], rules: list[int]) -> None:
        self._updates = updates
        self._rules = rules
        self._fixed_updates = []

        self._fix_updates()

    def get_fixed_update(self) -> list[list]:
        return self._fixed_updates

    def _fix_updates(self) -> None:
        for updates in self._updates:
            tmp = []
            for rule in self._rules:
                if rule in updates:
                    tmp.append(rule)

            self._fixed_updates.append(tmp)


def get_middle_page_numbers(updates: list[list]) -> list[int]:
    middle_page_numbers = []
    for page in updates:
        middle_page_numbers.append(page[len(page) // 2])
    return middle_page_numbers


ordering_rules = []
updates = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        if "|" in line:
            split = line.split("|")
            ordering_rules.append([int(i) for i in split])
        elif "," in line:
            split = line.split(",")
            updates.append([int(i) for i in split])
        else:
            continue

ordered_pages = Ordering(ordering_rules, updates)
ordered_wrong = ordered_pages.get_wrong_ordered_pages()

sort_rules = SortRules(ordering_rules)
print(sort_rules.get_array_of_all_numbers())

# sorted_rules = sort_rules.get_sorted_rule_array()
#
# fix_updates = SortUpdatesByRules(ordered_wrong, sorted_rules)
# fixed_updates = fix_updates.get_fixed_update()
#
# middle_page_numbers_from_fixed = get_middle_page_numbers(fixed_updates)
#
# print()
# print(sum(middle_page_numbers_from_fixed))
