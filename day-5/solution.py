class Ordering:
    def __init__(self, rules: list[list], updates: list[list]) -> None:
        self._rules = rules
        self._updates = updates
        self._ordered_pages = []
        self._rules_length = len(rules)
        self._middle_page_numbers = []
        self._middle_page_number_sum = 0

        self._count_ordered_pages()
        self._collect_middle_page_number()
        self._sum_middle_page_numbers()

    def get_ordered_pages(self) -> list[list]:
        return self._ordered_pages

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
f.close()

ordered_pages = Ordering(ordering_rules, updates)
print(ordered_pages.get_middle_page_number_sum())

# PART 1
#
# CORRECT ANSWER:
# 5651
