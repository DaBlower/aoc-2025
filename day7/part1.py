inp = open("day7/input.txt").read().splitlines()

total = 0

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == "S":
            s = inp[i+1]
            inp[i+1] = s[:j] + "|" + s[j+1:]
            print(inp[i])
            break

for i, line in enumerate(inp):
    for j, char in enumerate(line):
        if char == "^":
            # check above to see if there is a tachyon
            if inp[i-1][j] != "|":
                continue
            else:
                print("yes")
                total += 1
                s = inp[i+1]
                inp[i+1] = s[:j-1] + "|" + s[j:] # left side
                s = inp[i+1]
                inp[i+1] = s[:j+1] + "|" + s[j+2:] # right side
        elif char == ".":
            # check above again
            if inp[i-1][j] == "|":
                s = inp[i]
                inp[i] = s[:j] + "|" + s[j+1:] # set this one to a tachyon as well

print(total)