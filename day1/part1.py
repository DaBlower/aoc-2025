with open("day1\input.txt", 'r') as i:
    input = i.read().splitlines()

dial = 50
zeros = 0

for instruction in input:
    #direction, amount = instruction.split("", 1)
    direction = instruction[:1]
    value = int(instruction[1:])
    
    if direction == "L":
        dial = (dial - value) % 100
    elif direction == "R":
        dial = (dial + value) % 100
    else:
        print(f'{direction} is not a valid direction! ["L", "R"]')
        exit()
    
    if dial == 0:
        zeros += 1

print(zeros)
    
