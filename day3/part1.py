with open("day3/input.txt", 'r') as i:
    inp = i.read().split("\n")


joltages = 0
for line in inp:
    highest = 0
    highest_index = 0
    second_highest = 0

    current_index = 0
    for battery in list(line):
        if int(battery) > highest:
            highest = int(battery)
            highest_index = current_index
        current_index += 1
    
    current_index = 0
    for battery in list(line):
        if int(battery) > second_highest and current_index > highest_index:
            second_highest = int(battery)
        current_index += 1
    
    print(int(str(highest)+str(second_highest)))
    joltages += int(str(highest)+str(second_highest))

print(joltages)