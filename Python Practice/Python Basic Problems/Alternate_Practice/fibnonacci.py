# With taking input
num = int(input("Enter any number:-"))
a1,a2 = 0,1
print("The fibonacci series is ",a1,a2 , end =" ")
for i in range(2,num):
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print(a3, end= " ")
    
# Sum of fibnonacci recurssion

def fibo(n):
    if n<0:
        print("Incorrect output")
    
    elif n==0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(6))


# With using Recurssion

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else: 
        return fibo(n-1)+fibo(n-2)
    
n = int(input("Enter the number:-"))
for i in range(1,n+1):
    print(fibo(i))
 
    