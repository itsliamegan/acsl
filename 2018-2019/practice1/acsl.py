from typing import List, Set
from collections import Counter


def get_check_digit(pin: int) -> int:
    product_pairs = [
        int(val) * (i + 2) for i, val in enumerate(list(str(pin))[::-1])
    ]
    sum_of_products = sum(product_pairs)

    if sum_of_products == 17:
        return -1

    check_digit = sum_of_products % 123

    if check_digit < 10:
        return check_digit
    else:
        return get_check_digit(sum_of_products)


def get_check_digits_in_range(pin: int, pin_range: int) -> List[int]:
    check_digits_in_range = [
        get_check_digit(pin + n) for n in range(pin_range + 1)
    ]
    check_digits_in_range_without_discards = [
        n for n in check_digits_in_range if n != -1
    ]

    return check_digits_in_range_without_discards


def get_most_common_check_digits_in_range(pin: int, pin_range: int) -> Set[int]:
    check_digits = get_check_digits_in_range(pin, pin_range)
    check_digit_occurance_pairs = Counter(check_digits).most_common()

    largest_occurance = 0
    most_common_digits = set()

    for check_digit, occurance in check_digit_occurance_pairs:
        if occurance >= largest_occurance:
            largest_occurance = occurance
            most_common_digits.add(check_digit)

    return most_common_digits


for _ in range(5):
    input_line = input()
    pin = int(input_line.split(', ')[0])
    pin_range = int(input_line.split(', ')[1])
    most_common_check_digits = get_most_common_check_digits_in_range(
        pin, pin_range)
    most_common_check_digit_strings = [
        str(n) for n in most_common_check_digits
    ]
    print(', '.join(most_common_check_digit_strings))
