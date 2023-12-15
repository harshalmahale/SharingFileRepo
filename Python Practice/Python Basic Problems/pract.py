l = [56,23,2,44,32,8,17]

high=secondhigh=0
for num in l:
    if(num>high):
        high=num
print(high)

for num in l:
    if(num>secondhigh and num!=high):
        secondhigh=num
        
print(secondhigh)
