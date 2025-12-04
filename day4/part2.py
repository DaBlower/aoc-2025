with open("day4/input.txt", 'r') as i:
    inp = i.read().splitlines()

lines = list(inp)
total = 0
removed = -1
while removed != 0:
    removed = 0
    to_remove = []
    for i, line in enumerate(lines):
        for j, character in enumerate(line):
            if character != "@":
                continue

            surrounding = 0
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    if i+k < 0 or i+k > len(lines) - 1:
                        continue
                    if j+l < 0 or j+l > len(line) - 1:
                        continue
                    if lines[i+k][j+l] == "@":
                        surrounding += 1
            
            if surrounding < 4:
                to_remove.append([i, j])
                removed += 1
    for removal in to_remove:
        lines[removal[0]] = lines[removal[0]][:removal[1]] + "." + lines[removal[0]][removal[1]+1:]
    total += removed
    print("done!")

print(total)