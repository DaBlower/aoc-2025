with open("day3/input.txt", 'r') as i:
    inp = i.read().split("\n")


joltages = 0
for line in inp:
    highest = 0
    highest_index = 0
    current_index = 0
    # first digit
    for battery in list(line):
        if current_index == len(list(line)) - 1:
            break
        elif int(battery) > highest:
            highest = int(battery)
            highest_index = current_index
        current_index += 1
    
    # second digit
    second_highest = 0
    current_index = 0
    for battery in list(line):
        if current_index <= highest_index:
            current_index += 1
            continue
        elif int(battery) > second_highest:
            second_highest = int(battery)
        current_index += 1
        

    joltages += int(str(highest)+str(second_highest))

print(joltages)