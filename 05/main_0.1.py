def check_within_inclusive(num, inc_range) -> bool:
    if min(inc_range) <= num <= max(inc_range):
        return True
    else:
        return False


before_break = True
safe_ranges = []
fresh = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            before_break = False
        elif before_break:
            safe_ranges.append(
                [int(i) for i in line.split('-')]
            )
        else:
            for safe_range in safe_ranges:
                if check_within_inclusive(int(line), safe_range):
                    fresh += 1
                    break

print(fresh)
