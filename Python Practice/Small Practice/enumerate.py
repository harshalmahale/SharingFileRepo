names = ['abc','abcdef','harshal']

# pos = 0
# print(len(names))
# for name in names:
#     print(f"{pos}.....>{name}")
#     pos += 1
 
#With Enumerate function

# for pos, name in enumerate(names):
#     print(f"{pos}---->{name}")

def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1

print(find_pos(names,'pune'))         
    