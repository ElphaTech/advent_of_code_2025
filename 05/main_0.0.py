# CRASHES BECAUSE OUT OF RAM
# DO NOT RUN!!!

before_break = True
fresh_ids = {}
check_ids = {}
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line == '':
            before_break = False
            print('break')
        elif before_break:
            line = [int(i) for i in line.split('-')]
            fresh_ids.update([i for i in range(line[0], line[1]+1)])
        else:
            check_ids.add(int(line))

print('done')

print(len(
    fresh_ids.intersection(check_ids)
))
