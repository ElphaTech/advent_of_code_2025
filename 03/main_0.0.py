# 1. Find largest number that isn't the last number
# 2. Look in numbers after and get second largest number
# 3. Sum output of each line

final_sum = 0
with open('input.txt') as f:
    for line in f:
        line = [int(i) for i in line.strip()]

        # == NUM 1 ==
        num1_value = max(line[:-1])
        num1_index = line.index(num1_value)

        # == NUM 2 ==
        num2_value = max(line[(num1_index+1):])

        # == JOIN & SUM ==
        final_sum += int(f"{num1_value}{num2_value}")

print(f"Final Sum: {final_sum}")
