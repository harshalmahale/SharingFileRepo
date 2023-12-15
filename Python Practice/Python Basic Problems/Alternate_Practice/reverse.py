# Using For Loop
a = 'Harshal'
rev = ''
for i in a:
    rev = i + rev
print(rev)

# Alternate

x = '456789'
y = []
for i in range(len(x),0,-1):
    y.append(x[i-1])
print(y)

# Without using For loop
m = '123456'
n = m[::-1]
print(n)

# Without using Foor loop

num = 123
rev = 0
last_digit = 0 
while(num>0):
    last_digit =  num%10
    rev = (rev * 10) + last_digit
    num = num//10
print('reverse is',rev)

    
    
