
lower = 50
upper = 100
print("The prime number between",lower, "and",upper,"are")

for num in range(lower,upper+1):
    flag = False
    if(num>1):
        for i in range(2,int(num/2)+1):
            if(num%i == 0):
                flag = True
                break
        if(flag == False):
            print(num)