from read_file import read_input
from match_keys_and_locks import MatchKeysAndLocks


def main() -> None:
    input = read_input()

    keys_and_locks = MatchKeysAndLocks(input)
    print(len(keys_and_locks.get_matching_pairs()))


if __name__ == "__main__":
    main()
