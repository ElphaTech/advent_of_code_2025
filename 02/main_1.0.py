from pprint import pprint


def chunk_str(string: str, chunk_size: int) -> list:
    '''Returns list of strings or blank list if impossible'''
    if (len(string) % chunk_size) != 0:
        return []

    return [
        string[i:i+chunk_size] for i in range(
            0,
            len(string),
            chunk_size
        )
    ]


def test_validity(i: int) -> bool:
    '''Returns true if valid'''
    istr = str(i)
    digits = len(str(i))
    for digit in range(1, digits):
        chunk_list = chunk_str(istr, digit)
        chunk_count = len(set(chunk_list))
        if chunk_count == 1 and len(chunk_list) >= 2:
            return False
    return True


with open('input.txt') as f:
    ranges = [[int(j) for j in i.split('-')]
              for i in f.read().strip().split(',')]

invalid_ids = []
for pair in ranges:
    for i in range(pair[0], pair[1]+1):
        if not test_validity(i):
            invalid_ids.append(i)

pprint(invalid_ids)
print(sum(invalid_ids))
