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
        for prefix in prefixes:
            if prefix not in self._sorted_rule_array:
                return False
        return True

    def _all_nums_accounted_for(self) -> bool:
        for i in self._array_of_all_numbers:
            if (i in self._sorted_rule_array) or (i in self._no_prefix_still_suffix):
                continue
            else:
                return False
        return True

    def _sort_all_collected_numbers(self) -> None:
        while True:
            if self._all_nums_accounted_for():
                break

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


ordering_rules = []
updates = []

with open("test.txt", "r") as f:
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

# ordered_pages = Ordering(ordering_rules, updates)
sorted_rules = SortRules(ordering_rules)

print(sorted_rules.get_array_of_all_numbers())
print(sorted_rules.get_sorted_rule_array())

# part 2
# print(ordered_pages.get_wrong_ordered_pages())
# print(len(ordered_pages.get_wrong_ordered_pages()))
