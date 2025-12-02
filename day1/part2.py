with open("day1\input.txt", 'r') as i:
    input = i.read().splitlines()

dial = 50
zeros = 0

for instruction in input:
    #direction, amount = instruction.split("", 1)
    direction = instruction[:1]
    value = int(instruction[1:])
    
    if direction == "L":
        for click in range(value):
            dial = (dial - 1) % 100
            if dial == 0:
                zeros += 1

    elif direction == "R":
        for click in range(value):
            dial = (dial + 1) % 100
            if dial == 0:
                zeros += 1

    else:
        print(f'{direction} is not a valid direction! ["L", "R"]')
        exit()

print(zeros)