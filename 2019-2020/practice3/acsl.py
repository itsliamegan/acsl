def get_next_largest_number(number, digits):
    for i in range(1, len(digits) + 1):
        potential_number = int("".join([str(d) for d in digits[0:i]]))
        digits_without_number = digits[i::]
        if (potential_number > number):
            return (potential_number, digits_without_number)

    return (None, None)

def get_largest_number_sequence(digits):
    sequence = []
    largest = digits[0]
    digits_without_number = digits[1::]

    while (
        (largest is not None) and
        (digits_without_number is not None)
    ):
        sequence.append(largest)
        largest, digits_without_number = get_next_largest_number(
            largest,
            digits_without_number[::-1]
        )

    return sequence

for _ in range(5):
    digits = [int(c) for c in list(input())]
    sequence = get_largest_number_sequence(digits)

    print(" ".join([str(d) for d in sequence]))
