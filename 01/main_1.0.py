def get_movement_int(inp: str) -> (int, int):
    '''Returns direction (1 or -1) and magnitude.'''
    direction = inp[0]
    number = inp[1:]
    if direction == 'R':
        return (1, int(number))
    else:
        return (-1, int(number))


cur_pos = 50
zero_count = 0
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        direction, magnitude = get_movement_int(line)
        for i in range(magnitude):
            cur_pos = (cur_pos + (direction)) % 100

            if cur_pos == 0:
                zero_count += 1

print(f'Password is :"{zero_count}"')
