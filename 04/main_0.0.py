grid = []
with open('input.txt') as f:
    for line in f:
        grid.append([i for i in line.strip()])


adjacent_pos = [(x, y) for y in range(-1, 2) for x in range(-1, 2)]
adjacent_pos.remove((0, 0))


def update_state(x, y, grid):
    if grid[y][x] not in '@x':
        return '.'

    adj_roll_count = 0
    for pos in adjacent_pos:
        tx = x + pos[0]
        ty = y + pos[1]
        if 0 <= tx < width and 0 <= ty < height:
            if grid[ty][tx] in '@x':
                adj_roll_count += 1
        else:
            pass

    if adj_roll_count < 4:
        return 'x'
    else:
        return '@'


width = len(grid[0])
height = len(grid)
for x, y in [(x, y) for y in range(height) for x in range(width)]:
    grid[y][x] = update_state(x, y, grid)

output_str = '\n'.join([''.join(i) for i in grid])
print(output_str)
print(output_str.count('x'))
