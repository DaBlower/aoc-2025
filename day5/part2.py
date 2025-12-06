ra, ia = open("day5/input.txt").read().split("\n\n")

ranges = [[int(i) for i in r.split("-")] for r in ra.split("\n")]

def mergeRanges(arr):
    arr.sort() # sort based on start values

    result = []
    result.append(arr[0])

    for i in range(1, len(arr)):
        last = result[-1]
        current = arr[i]

        # if current overlaps with last, then merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)

    return result

result = mergeRanges(ranges)
print(result)
total = 0
for r in result:
    total += len(range(r[0], r[1]))+1

print(total)