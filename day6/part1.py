from math import prod

inp = open("day6/input.txt").read().splitlines()

rows = [line.split() for line in inp if line.strip()]

columns = [list(col) for col in zip(*rows)]


total = 0
for column in columns:
    col_sum = 0
    if column[-1] == "+":
        col_sum += sum(int(column[r]) for r in range(len(column)-1))
    elif column[-1] == "*":
        col_sum += prod(int(column[r]) for r in range(len(column)-1))
    total += col_sum
print(total)