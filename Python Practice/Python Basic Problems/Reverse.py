num = int(input("Enter the number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num//10
print(f"The given number is {temp} and reverse is {reverse}")