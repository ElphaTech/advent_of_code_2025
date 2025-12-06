# 1. Find largest number that isn't the last number
# 2. Look in numbers after and get second largest number
# 3. Sum output of each line

final_sum = 0
digits = 12
with open('input.txt') as f:
    for line in f:
        line = [int(i) for i in line.strip()]
        numbers = []
        min_index = 0
        max_index = -digits + 1

        print('line: ', line)
        for i in range(digits):
            print('minmax: ', min_index, max_index)
            numbers.append(max(line[min_index:max_index]))
            print('selarea: ', line[min_index:max_index])
            print('sel: ', numbers[-1])
            min_index = line[min_index:max_index].index(
                numbers[-1]) + min_index + 1
            max_index = len(line) - (digits - (len(numbers)+1))

        # == JOIN & SUM ==
        final_sum += int(''.join([str(i) for i in numbers]))
        print(final_sum)
        print()

print(f"Final Sum: {final_sum}")
