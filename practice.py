# Iterator 

# my_list = [1,2,3,4]
# my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))

# Genrator 

# def my_gen(n):
#     for i in range(1,n+1):
#         yield i*i
        
# my_generator = my_gen(4)
# for num in my_generator:
#     print(num)


# Annotations

# def check_anno(name:str) -> str:
#     return f"Hello {name}"

# print(check_anno("Harshal"))

# Decorators

def deco(func):
    def inner():
        print("Excecuting now")
        func()
        print("Exceuted")
    return inner

@deco
def who_is_harsh():
    print("harsh is smart boy")
who_is_harsh()

# l = [4,12,65,7,7,9,10]

# l.sort()
# list(set(l))
# print(l)
# print(l[1])

# list = [4,12,65,7,7,2,9,12,10]

# # high = secondhigh = -112345678
# low = secondlow = list[0]

# for nums in list:
#     if (nums<low):
#         low = nums
    
# for nums in list:
#     if(nums<secondlow and nums!=low):
#         print(nums)


# Reverse a string
# str = "tac si trams"
# str = list(str.split(" "))
# print(str)
# res_word = [word[::-1] for word in str]
# print(res_word)
# res = ''.join(res_word)
# print(res)     
   
#   Custom List to calculate length
   
# class CustomList:
#     def __init__(self):
#         self.__numbers = [1,2]
        

#     def __len__(self):
#         count = 0
#         for i in self.__numbers:
#             count += 1
#         return count
        
# l = CustomList()
# print(l._numbers)

# 1 to 10 using generator 

# def my_gen(n):
#     for num in range(1,11):
#         yield num*num
        
# x=my_gen(6)
# for num in x:
#     print(num)

# split into dictionary
# a = 'a/1/b/2/c/3'

# o/p = {'a':1,'b':2,'c':3}
# d = dict()
# a_a = a.split('/')
# print(a_a)

# for i in range(len(a_a)):
#     if(i%2 == 0):
#         d[a_a[i]] = a_a[i+1]

# print(d)

# def gen(n):
#     for i in range(n):
#         if(i%2 == 0):
#             yield i

# for i in gen(len(a_a)):
#     d[a_a[i]] = a_a[i+1]
    
# print(d)

# l = [1,2,3]
# d= dict()
# for i in l:
#     d[i] = i
# print(d)


# Parenthethis 

stack = []

open_backets = '{(['

str = '{()}'

for char in str:
    if char in open_backets:
        stack.append(char)
        
    else:
        if char == ')' and stack[len(stack)-1] == '(':
            stack.pop()
        
        elif char == '}' and stack[len(stack)-1] == '{':
            stack.pop()
            
        elif char == ']' and stack[len(stack)-1] == '[':
            stack.pop()
        
        else:
            print("Invalid Parenthesis")
            break

        
if(len(stack) == 0):
    print("Valid")

    
# class custom_len:
#     def __init__(self):
#         self.numbers = [1,2]
        
#     def __len__(self):
#         count = 0
#         for i in self.numbers:
#             count = count + 1
#         return count
            
# d = custom_len()
# print(d.numbers)

num = int(input("Enter a num of elements: "))
f = 0
s = 1

print("the series is: ", f,s, end = '')

for i in range(2,num):
    t = f + s
    f = s
    s = t
    print(t, end = '')    


