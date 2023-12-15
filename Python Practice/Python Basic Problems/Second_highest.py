list = [1,45,2,45,63,67,22,87,52]
high = secondhigh = -123457890

for num in list:
    if(num>high):
        high = num
        
for num in list:
    if(num>secondhigh and num!=high):
        secondhigh=num
    
print(secondhigh)
