ra, ia = open("day5/input.txt").read().split("\n\n")

ranges = [[int(i) for i in r.split("-")] for r in ra.split("\n")]
ids = [int(i) for i in ia.split("\n")]

total = sum(any(r[0] <= i <= r[1] for r in ranges for i in ids))

print(total)