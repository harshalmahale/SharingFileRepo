# #List comprehension summary
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)

square = [i**2 for i in range(1,11)]
print(square)

even_num = [i for i in range(1,11) if i%2==0]
print(even_num)

l1 = [[1,2,3],[1,2,3],[1,2,3]]
comb = [[i for i in range(1,4)] for j in range(3)]
print(comb)    