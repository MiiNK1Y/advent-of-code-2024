from read_input import read_input
from update_manager import UpdateManager, UpdateFixer


def sum_middle_page_numbers(updates: list[list[int]]) -> int:
    middle_page_numbers = [update[len(update) // 2] for update in updates]
    return sum(middle_page_numbers)


def main() -> None:
    # get the input values and rules
    input = read_input()
    rules = input[0]
    updates = input[1]

    manage_updates = UpdateManager(rules, updates)
    bad_updates = manage_updates.get_bad_updates()

    corrected_updates = UpdateFixer(rules, bad_updates)
    fixed_bad_updates = corrected_updates.get_fixed_updates()

    print(bad_updates)
    print(fixed_bad_updates)
    print(sum_middle_page_numbers(fixed_bad_updates))


if __name__ == "__main__":
    main()

# 4743
