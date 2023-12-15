num = int(input("Enter the number:-"))
binary = num
base = 1
decimal = 0
while(num>0):
    rem = num%10
    decimal = decimal + rem * base
    num = num//10
    base = base*2

print(f"Binary no is {binary} and decimal no is {decimal}")