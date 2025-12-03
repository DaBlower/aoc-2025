with open("day3/input.txt", 'r') as i:
    inp = i.read().split("\n")


joltages = 0
for line in inp:      
    locked_index = -1 # same as highest_index but for everything
    nums = ""
    repeats = 12
    for i in range(12):
        print(f"new range")
        current_index = 0
        highest = 0
        for battery in list(line):
            if current_index > len(list(line)) - repeats:
                current_index += 1
                continue
            if current_index <= locked_index:
                current_index += 1
                continue
            elif int(battery) > highest:
                highest = int(battery)
                locked_index = current_index
            current_index += 1
        print(f"Highest: {highest}")
        nums += str(highest)
        repeats -= 1

    print(nums)
    joltages += int(nums)

print(joltages)