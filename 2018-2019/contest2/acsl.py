from typing import List


def get_common_string(first: str, second: str, common: str = "") -> str:
    if not first or not second:
        return common

    try:
        first_letter = first[0]
        letter_index = second.index(first_letter)
        rest_of_first = first[1:]
        second_after_letter_occurance = second[(letter_index + 1):]
        common_with_letter = common + first_letter

        return get_common_string(rest_of_first, second_after_letter_occurance, common_with_letter)

    except ValueError:
        rest_of_first = first[1:]
        return get_common_string(rest_of_first, second, common)


def get_four_common_strings(first: str, second: str) -> List[str]:
    reversed_first = first[::-1]
    reversed_second = second[::-1]

    return [
        get_common_string(first, second),
        get_common_string(second, first),
        get_common_string(reversed_first, reversed_second),
        get_common_string(reversed_second, reversed_first)
    ]


def get_always_occuring_letters(common_strings: List[str]) -> List[str]:
    always_occuring_letters = set()

    for index, common in enumerate(common_strings):
        for letter in common:
            in_all_strings = True

            for other_common in (s for i, s in enumerate(common_strings) if i != index):
                if letter not in other_common:
                    in_all_strings = False

            if in_all_strings:
                always_occuring_letters.add(letter)

    return sorted(always_occuring_letters)


for _ in range(5):
    letters = input().split(" ")
    first_letters = letters[0]
    second_letters = letters[1]

    four_common_strings = get_four_common_strings(
        first_letters, second_letters)
    always_occuring_letters = get_always_occuring_letters(four_common_strings)

    if not always_occuring_letters:
        print('NONE')

    else:
        print("".join(always_occuring_letters))
