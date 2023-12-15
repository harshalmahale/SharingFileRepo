
def reverse_list(l):
    r_list = []
    for i in l:
        r_list.append(i[::-1])
    return r_list

words = ['abc','xyz','pqr']
print(reverse_list(words))  
