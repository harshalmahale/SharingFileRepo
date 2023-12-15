demosplit="gsdhgd3767647ghsggd"
num=[]
alpha=[]

for i in demosplit:
    if i.isalpha() == True:
        alpha.append(i)
    elif i.isdigit() == True:
        num.append(i)
        
print(f'Letters is {set(alpha)}')
print(f'Numbers is {set(num)}')
