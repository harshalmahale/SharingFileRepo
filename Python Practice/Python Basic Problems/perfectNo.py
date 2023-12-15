# Sum of all factors or divisor excluding itself = Perfect Number

num = int(input("Enter any number"))
sump = 0
for i in range(1, num):
    if(num%i == 0):
        sump = sump + i
        print(i)

if(num == sump):
    print("The number is a perfect number")
else:
    print("The number is not perfect number")


