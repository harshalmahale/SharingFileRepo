numbers = [1,2,3,4]

# With list comprehension

square_list = [i**2 for i in numbers]
print("1-->",square_list)

# With function

def square_list(no):
    for i in numbers:
        return no**2
    
print("2-->", square_list(3))

#        OR  

def sq_list(nos):
    return nos**2

new_list = []
for nos in numbers:
    new_list.append(sq_list(nos))
    
print("3-->" , new_list)

# With Map & Lambda Function

sq_list4 = list(map(lambda nos:nos**2 , numbers))
print("4-->", sq_list4)

# -----------

# names 