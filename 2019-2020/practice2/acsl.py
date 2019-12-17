def chunk(items, chunk_size):
    return [items[i:i+chunk_size] for i in range(0, len(items), chunk_size)]

def get_all_combinations(number):
    digits = list(str(number))
    digit_combinations = []
    combinations = []

    for i in range(len(digits)):
        first_chunk = digits[:i]

        if len(first_chunk) == 0:
            first_chunk = ["0"]

        for chunk_size in range(1, len(digits)):
            remaining_chunks = chunk(digits[i:], chunk_size)
            digit_combinations.append([first_chunk, *remaining_chunks])

    for i in range(len(digits)):
        last_chunk = digits[i:]

        if len(last_chunk) == len(digits):
            last_chunk = ["0"]

        for chunk_size in range(1, len(digits)):
            first_chunks = chunk(digits[:i], chunk_size)
            digit_combinations.append([*first_chunks, last_chunk])


    for digit_combination in digit_combinations:
        combination = []

        for digits in digit_combination:
            combination.append(int("".join(digits)))

        combinations.append(combination)

    return combinations 

def get_sums_below_threshold(combinations, threshold):
    sums = []

    for combination in combinations:
       combo_sum = sum(combination)
       
       if combo_sum <= threshold:
           sums.append(combo_sum)

    return sums

for _ in range(5):
    [card_number, threshold] = input().split(", ")
    card_number = int(card_number)
    threshold = int(threshold)

    combos = get_all_combinations(card_number)
    sums = get_sums_below_threshold(combos, threshold)
    max_sum = max(sums)

    print(max_sum)
