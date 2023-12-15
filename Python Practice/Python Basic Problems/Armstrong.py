# Armstrong number is a number that is equal to the sum of cubes of its digits.
# num = 371
# number = num
# sum,digit = 0,0
# length = len(str(num))
# for i in range(length):
#     digit = num%10
#     num = num//10
#     sum = sum + pow(digit,length)
# if (sum==number):
#     print("Armstrong Number")
# else:
#     print("not armstrong")
    
    
# Alternate solutions

num = 372
number = num
length = len(str(num))
digit,sum = 0,0
for i in range(length):
    digit = num%10
    num = num//10
    sum += digit**length 
# pow(digit,length)
if(sum == number):
    print("It is amstrong no.")
else:
    print("not amstrong")
    