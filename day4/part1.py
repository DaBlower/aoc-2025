with open("day4\input.txt", 'r') as i:
    inp = i.read().splitlines()

lines = list(inp)
rolls = 0
for i, line in enumerate(lines):
    for j, character in enumerate(line):
        if character != "@":
            continue

        surrounding = 0
        for k in [-1, 0, 1]:
            for l in [-1, 0, 1]:
                if k == 0 and l == 0:
                    continue
                if i+k < 0 or i+k > len(line) - 1:
                    continue
                if j+l < 0 or j+l > len(line) - 1:
                    continue
                if lines[i+k][j+l] == "@":
                    surrounding += 1
        
        if surrounding < 4:
            rolls += 1

print(rolls)