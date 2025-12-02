def get_movement_int(inp: str) -> int:
    direction = inp[0]
    number = inp[1:]
    if direction == 'R':
        return int(number)
    else:
        return -1 * int(number)


cur_pos = 50
zero_count = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        move = get_movement_int(line)
        cur_pos = (cur_pos + move) % 100

        if cur_pos == 0:
            zero_count += 1

print(f'Password is :"{zero_count}"')
