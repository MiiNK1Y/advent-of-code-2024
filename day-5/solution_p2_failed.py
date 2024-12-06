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
        self._sort_wrong_ordered_pages()

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

    # part 2 FAILED
    def _in_front_of_this(self, page, update, used):
        for rule in self._rules:
            if (rule[1] == page) and ((rule[0] in update) and (rule[0] not in used)):
                print(f"\t[+] {rule[0]} - in front of - {page}")
                return rule[0]
            else:
                continue
        return None

    # part 2 FAILED
    def _sort_wrong_ordered_pages(self):
        for update in self._wrong_ordered_pages:
            print(update)
            reconstrunction = []
            for page in update:
                print(f"[>] seeking {page}")
                next_page = self._in_front_of_this(page, update, reconstrunction)
                if next_page is not None:
                    reconstrunction.append(next_page)
                else:
                    continue
            print(reconstrunction)
            self._fixed_ordered_pages.append(reconstrunction)

    def _count_ordered_pages(self) -> None:
        for update in self._updates:
            if self._check_rule_with_page(update):
                self._ordered_pages.append(update)
            else:
                # part 2
                self._wrong_ordered_pages.append(update)


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
f.close()

ordered_pages = Ordering(ordering_rules, updates)

# part 2
# print(ordered_pages.get_wrong_ordered_pages())
# print(len(ordered_pages.get_wrong_ordered_pages()))
