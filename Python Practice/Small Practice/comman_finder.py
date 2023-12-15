def commanlist(l1,l2):
    comman = []
    for i in l1:
        if i in l2:
            comman.append(i)
    return comman

list1,list2 = [1,2,3,4],[1,3,6,7]
print(commanlist(list1,list2))