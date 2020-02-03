import re

def find_all_common_substrings(first, second):
    substrings = []

    for i in range(len(first)):
        for j in range(len(first)):
            if j >= i:
                first_substring = first[i:j+1]
                if first_substring in second:
                    substrings.append(first_substring)

    for i in range(len(second)):
        for j in range(len(second)):
            if j >= i:
                second_substring = second[i:j+1]
                if second_substring in first and second_substring not in substrings:
                    substrings.append(first_substring)

    return substrings

def find_longest_common_substring(first, second):
    longest = ""
    equals = []

    for string in find_all_common_substrings(first, second):
        if len(string) > len(longest):
            longest = string

    for string in find_all_common_substrings(first, second):
        if len(string) == len(longest):
            equals.append(string)

    if len(equals) != 0:
        return sorted(equals)[0]

    return longest

substrings = { 0: [], 1: [], 2: [], 3: [], 4: [] }

def find_adf(first, second, identifier):
    longest_substring = find_longest_common_substring(first, second)
    print(longest_substring)

    if longest_substring == "":
        return 0

    if longest_substring in substrings[identifier]:
        return 0

    substrings[identifier].append(longest_substring)

    longest_substring_length = len(longest_substring)
    first_index_start = first.index(longest_substring)
    first_index_end = first_index_start + len(longest_substring)
    first_left = first[0:first_index_start]
    first_right = first[first_index_end:]
    second_index_start = second.index(longest_substring)
    second_index_end = second_index_start + len(longest_substring)
    second_left = second[0:second_index_start]
    second_right = second[second_index_end:]

    left_adf = find_adf(first_left, second_left, identifier)
    right_adf = find_adf(first_right, second_right, identifier)
    return longest_substring_length + left_adf + right_adf

def normalize_line(line):
    line = line.upper()
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.replace("'", "")
    line = line.replace("\"", "")
    line = line.replace(" ", "")
    return line

for i in range(5):
    first = normalize_line(input())
    second = normalize_line(input())
    adf = find_adf(first, second, i)
    print(adf)
