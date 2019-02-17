from typing import List


def get_chunks(string: str, chunk_length: int, chunks: List = []) -> List:
    if len(string) == 0 or len(string) < chunk_length:
        return chunks

    new_chunk = string[0:chunk_length]
    new_chunks = chunks + [new_chunk]
    remaining_string = string[1::]

    return get_chunks(remaining_string, chunk_length, new_chunks)


for i in range(5):
    input_line = input('Input Line ' + str(i + 1) + ': ')

    string = input_line.split(' ')[0]
    chunk_length = int(input_line.split(' ')[1])

    string_chunks = get_chunks(string, chunk_length)
    int_chunks = map(lambda x: int(x), string_chunks)
    int_chunks_sum = sum(int_chunks)

    print(int_chunks_sum)
