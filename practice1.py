# # Iterator

# my_list = [1,2,3,4]
# my_iter = iter(my_list)
# print(next((my_iter)))
# print(next((my_iter)))

# Generator

# def my_gen(n):
#     for nums in range(1,n+1):
#         yield nums*nums
    
# my_generator = my_gen(5)
# for nums in my_generator:
#     print(nums)

# Annotations

# def check_ano(name:str,age:int)->str:
#     return f"Hello {name} my age is {age}" 

# # print(check_ano.__annotations__)
# xy = check_ano("Harshal" , 21)
# print(xy)

# Decorators


# cached_values = {}
# def deco(func):
#     def inner(n,m=None):
#             value = cached_values.get((n,m), None)
#             if value is not None:
#                 print('cached value is now returning value')
#                 func(cached_values[(n,m)])
#             else:
#                 print('computing the new value')
#                 func(n+m)
#                 cached_values[(n,m)] = n+m
#     return inner

# @deco
# def who_is_harshal(n):
#     print("Harshal is smart", n)
# # who_is_harshal = deco(who_is_harshal)

# who_is_harshal(2,4)
# who_is_harshal(2,4)

    
# cached_values = {'a':1, 'b':2}


# print(cached_values.get('c', None))


# Second highest

# list = [13,3,5,8,4,9,9,12,12]

# a=sorted(list)
# print(a)
# a = list(set(a))

# print(a)
# print(a[-2])

# high = secondhigh = -123457890

# for num in list:
#     if(num>high):
#         high = num
        
# for num in list:
#     if(num>secondhigh and num!=high):
#         secondhigh=num
    
# print(secondhigh)


# a = 'a/1/b/2/c/3'

# d = dict()

# ab = a.split('/')
# print(ab)
# for i in range(len(ab)):
#     print(i)
#     if(i%2==0):
#         d[ab[i]]=ab[i+1]
    
# print(d)

str = '[(])'
stack = [] 

open_brackets = '[({'

for char in str:
    if char in open_brackets:
        stack.append(char)
    
    else:
        if (char == '(' and len(stack-1) ==')'):
            stack.pop()
        
        elif(char == '[' and len(stack-1) == ']'):
            stack.pop()
        
        elif(char == '{' and len(stack-1) == '}'):
            stack.pop()
            
        else:
            print("Invalid Parentheis ")
            
if(len(stack) == None):
    print("Valid parenthetis")

# def gen():
#     for num in range(1,11):
#         yield num
        

# my_gen = gen()
# for num in my_gen:
#     print(num)


# Inheritence

# class A:
#     def method1(self):
#         return "Method 1 from Class A"
    
# class B(A):
#     def method2(self):
#         return "Method 2 from class B"
    
# class C(A):
#     def method3(self):
#         return "Method 3 from class C"
    
# obj_b = B()
# obj_c = C()

# print(obj_b.method1())
# print(obj_b.method2())
# print(obj_c.method1())
# print(obj_c.method3())


# Abstraction


#  We can achieve abstraction using abstract base classes (ABC) from the abc module
# The abc module is used to create an abstract base class Shape with the @abstractmethod
# decorator to define an abstract method area. 

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
        
#     def area(self):
#         return self.side * self.side
    

# obj_circle = Circle(3)
# obj_square = Square(4)

# print(obj_circle.area())
# print(obj_square.area())

# Encapsulation Ex

# class BankAccount:
#     def __init__(self,acc_no,balance):
#         self._acc_no = acc_no
#         self.__balance = balance
        
#     def deposit(self, amount):
#         self.__balance = self.__balance + amount
    
#     def withdraw(self,amount):
#         if (self.__balance>=amount):
#             self.__balance = self.__balance - amount
        
#         else:
#             print("Insufficient Balance")
        
#     def display_Acc_info(self):
#         print(f"Balance is :{self.__balance}")
#         print(f"Account No. is : {self._acc_no}")
        
        
# bnk_amt = BankAccount("123456789", 190000)

# bnk_amt.deposit(500)
# bnk_amt.withdraw(200)
# bnk_amt.display_Acc_info()


# Polymorphism Example

# class Person:
#     def role(self):
#         return "I am a person"
    
# class Father(Person):
#     def role (self):
#         return "I am a father"
    
# class Husband(Person):
#     def role(self):
#         return "I am a Husband"
    
# class Employee(Person):
#     def role(Self):
#         return "I am a Employee"
    
# p = Person()
# f = Father()
# h = Husband()
# e = Employee()

# print(p.role())
# print(f.role())
# print(h.role())
# print(e.role())

# nth Highest Salary From SQL emp table has ID, SALARY

# SELECT MAX (Salary) from Emp: .......get max salary

# SELECT MAX (Salary) from Emp Where Salary Not in (SELECT MAX (Salary) from Emp ) ...2nd max salary

# SELECT ID, SALARY from Emp e1 where N-1 = (SELECT count (Distinct salary) from 
                                        #    emp2 where e2.salary > e1.salary) ...nth salary

# Check Anagram Act/Cat

# str1 = input("Enter the string")
# str2 = input("Enter second string")

# if (len(str1)!=len(str2)):
#     print("length is not equal")
    
# else:
#     s1 = sorted(str1)
#     s2 = sorted(str2)
    
# if(s1 == s2):
#     print("it is anagram")

# Check It is amstrong no. or not
# num = 372
# number = num
# length = len(str(num))
# digit,sum = 0,0
# for i in range(length):
#     digit = num%10
#     num = num//10
#     sum += digit**length 
# # pow(digit,length)
# if(sum == number):
#     print("It is amstrong no.")
# else:
#     print("not amstrong")
    
# Factorial of number
# def fact(n):
#     if n==0:
#         return 1
    
#     else:
#         return n*fact(n-1)

# print("The fact is",fact(5))

# Fibonacci series

# def fibo(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
    
#     else:
#         return fibo(n-1) + fibo(n-2)
    
# n = int(input("Enter any number"))
# for i in range(1,n+1):
#     print("fibo series is",fibo(6))

# num = int(input("enter any number"))
# f,s=0,1
# print("The series is",f, s, end = " ")
# for i in range(2,num):
#     t = f + s
#     f = s
#     s = t
#     print(t, end = " ")

# Non Repetative Character
# str = "harshal"

# for i in str:
#     count = 0
#     for j in str:
#         if(i==j):
#             count = count + 1
#         if count>1:
#             break
#     if count == 1:
#         print (i, end = "")
    
    
# str = 'madan'
# b = str

# a =str[::-1]
# if(a==b):
#     print("palindrome")
# else:
#     print("not palindrome")
# a = ''
# for i in str:
#     a = i + a

# if(a==str):
#     print("palindrome")
# else:
#     print("not palindrome")    
    
# Remove space

# str = " hey how is going "
# a = ''
# a = ''.join(str.split(' '))
# print(a)

# Remove special character check right or not?

# str = "Hello@nice&work?"
# str1 = '!@#$%^&*()_+|<>?-=[]{}'
# print(str)
# for i in str:
#     count = 0
#     for j in str1:
#         if(i==j ):
#             count = count+1
        
#     if (count>1):
#         break
# if(count==0):
#     print(str)
 
# 2nd Apporach

# str1 = input("Enter the string")
# str2 = ''

# for i in  str1:
#     if (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 ):
#         str2 = str2 + i
    
# print("the string is:",str2)

# Replace Substring

# str = input("Enter the string")
# str1 = input("enter the string to replace")
# str2 = input("enter the string to be replace")
# str = str.replace(str1,str2)
# print("Replace string is:",str)

# Reverse a number

# num = 1234
# rem = 0
# res = 0

# while(num!=0):
#     rem = num%10
#     res = (res*10) + rem
#     num = num//10
# print(res)

# Highest number 

# list = [15,3,2,8,9,6,10,19]

# high=secondhigh = -9876545432

# for num in list:
#     if(num>high):
#         high = num
        
# print(num)

# for num in list:
#     if(num>secondhigh and num!=high):
#         secondhigh = num
    
# print(secondhigh)



# to demonstrate access specifiers
# class InterviewbitEmployee:
   
#     # protected members
#     _emp_name = None
#     _age = None

#     # private members
#     __branch = None
    
#     # constructor
#     def __init__(self, emp_name, age, branch): 
#          self._emp_name = emp_name
#          self._age = age
#          self.__branch = branch
    
#     #public member
#     def display():
#         print(self._emp_name +" "+self._age+" "+self.__branch)


#  Empty class
# class EmptyClassDemo:
#    pass
# obj=EmptyClassDemo()
# obj.name="Interviewbit"
# print("Name created= ",obj.name)

