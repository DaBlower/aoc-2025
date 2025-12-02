with open("day2\input.txt", 'r') as i:
    input = i.read().split(",")

ids = []

# big list with all ids
for r in input:
    start, end = map(int, r.split("-"))
    
    ids.append([start,end])

print(ids)


false_ids = 0

def is_fully_repeated(string):
    n = len(string)
    if n % 2 != 0:
        return False
    
    half = n // 2
    if string[:half] * 2 == string:
        return True
    
    return False


for r in ids:
    for id in range(r[0],r[1]+1):
        if is_fully_repeated(str(id)):
            print(f"id {id}")
            false_ids += id
    print("done block")



print(false_ids)