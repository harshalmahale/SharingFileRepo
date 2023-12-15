# A word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or radar run

# Using For loop
m = '12345'
n = ''
for i in m:
    n = i + n 
# print(n)
if(m==n):
    print('palindrome')
else:
    print('not palindrome')

# Using Flag

st = 'malayalam'
j = -1
flag = 0
for i in st:
    if i != st[j]:
        flag = 1
        break
    j = j - 1
if flag == 1:
    print("NO")
else:
    print("Yes")
    
# Function which return reverse of string

def ispalindrome(s):
    return s == s[::-1]

s = 'malayalam'
ans = ispalindrome(s)

if ans:
    print('yes')
else:
    print("No")    