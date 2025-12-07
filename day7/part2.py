inp = open("day7/input.txt").read().splitlines()
rows = len(inp)
cols = len(inp[0])

total = 0

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == "S":
            start_row, start_column = i, j
            break

# recursion is yummy
cache = {}
def timelines(r, c): # row, column
    if (r, c) in cache:
        return cache[(r, c)]
    
    # outside bounds or bottom
    if r >= rows or c < 0 or c >= cols:
        return 1
    
    cell = inp[r][c]
    if cell in (".", "S"):
        ans = timelines(r+1, c)
    elif cell == "^":
        # left and right
        ans = timelines(r+1, c-1) + timelines(r+1, c+1)
    else:
        ans = 0 # just incase my code is ahh

    cache[(r, c)] = ans
    return ans

total_timelines = timelines(start_row+1, start_column)

print(total_timelines)