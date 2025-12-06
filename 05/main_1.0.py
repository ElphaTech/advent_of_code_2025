# Similar to 0.1 but tries to be more efficient by
# removing of overlapping ranges.

def check_within_inclusive(num, inc_range) -> bool:
    if min(inc_range) <= num <= max(inc_range):
        return True
    else:
        return False


def optimize_range_list(range_list: list) -> list:
    range_list.sort(key=lambda x: x[0])
    for index in range(len(range_list)-1):
        i = range_list[index]
        j = range_list[index+1]

        if i[1] < j[0] or j[1] < i[0]:
            # do not touch
            pass
        else:
            # do touch
            range_list[index] = []
            range_list[index+1] = [min(i[0], j[0]), max(i[1], j[1])]

    return [i for i in range_list if i != []]


safe_ranges = []
fresh = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            changed = True
            prev_len = len(safe_ranges)
            while changed:
                safe_ranges = optimize_range_list(safe_ranges)
                new_len = len(safe_ranges)
                changed = prev_len == new_len
                prev_len = new_len

            print(sum([
                len(range(i[0], i[1]+1)) for i in safe_ranges
            ]))
            exit()

        else:
            safe_ranges.append(
                [int(i) for i in line.split('-')]
            )
