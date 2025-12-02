with open("day2\input.txt", 'r') as i:
    inp = i.read().split(",")

ids = []

# list with all ranges
for r in inp:
    start, end = map(int, r.split("-"))
    
    ids.append([start,end])

print(ids)


false_ids = 0

def is_fully_repeated(string, length):
    if length == 1:
        return False
    previous = ""
    for character in list(string):
        previous += character
        if previous * len(string) == string:
            return True

        if len(previous) > length // 2:
            return False
        
        mult = length / len(previous)
        if mult % 1 != 0:
            continue # if a string cannot fully fit, it is not invalid
        mult = int(mult)
        if previous * mult == string:
            return True
    
    return False


for r in ids:
    for id in range(r[0],r[1]+1):
        length = len(str(id))
        if is_fully_repeated(str(id), length):
            print(f"id {id}")
            false_ids += id
    print("done block")


print(false_ids)