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
    previous = ""
    for character in list(string):
        previous += character
        print("")
        print(f"Character: {character}")
        print(f"Previous: {previous}")
        if previous * len(string) == string:
            return True

        print(f"Length: {len(previous)}")
        print(f"Condition: length // 2 = {length // 2}")
        if len(previous) > length // 2:
            print(f"FALSE: length is greater than the condition")
            return False
        
        mult = length / len(previous)
        print(f"Mult: {mult}")
        if mult % 1 != 0:
            print("FALSE: The mult is not a int")
            return False # if a string cannot fully fit, it is not invalid
        mult = int(mult)
        if previous * mult == string:
            return True
    
    return False


# for r in ids:
#     for id in range(r[0],r[1]+1):
#         length = len(str(id))
#         if is_fully_repeated(str(id), length):
#             print(f"id {id}")
#             false_ids += id
#     print("done block")

new = input("What is the ID you want to test? ")
print(is_fully_repeated(new, len(new)))

# print(false_ids)