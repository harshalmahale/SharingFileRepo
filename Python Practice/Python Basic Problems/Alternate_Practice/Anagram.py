# using if statement
# a = 'cat'
# b = 'act'
# if (len(a)!=len(b)):
#     print('not anagram')
# else:
#     print('anagram')
    
# Giving input
a = input("Enter the string:-")
b = input("Enter the string:-") 
if (len(a)!=len(b)):
    print('not anagram')
elif True:
    a = sorted(a)
    b = sorted(b)
if (a==b):
    print('anagram')
else:
    print('notanagram')
    