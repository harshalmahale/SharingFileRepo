num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))

if (num1>num2):
    small = num2
else:
    small = num1

def findgcd(num1,num2):
    
    for i in range(1,small+1):
        if (num1%i==0) and (num2%i==0):
            gcd = i
    print("Gcd is :",gcd)

findgcd(num1,num2)


