num = int(input("Enter any number:"))
sum = 0
for i in range(1,num):
    if(num%i==0):
        sum = sum + i

if (num==sum):
    print("It is perfect number")
else:
    print("It is not perfect number") 