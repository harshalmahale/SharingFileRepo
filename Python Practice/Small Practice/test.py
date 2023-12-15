# from enum import Flag
# a = int(input("Enter any number to determine prime or not:"))
# flag = 0
# for i in range(2,a):
#     if(a%i==0):
#         print("It is non prime")
#         flag=1
#     break
# if(flag==0):
#     print("It is prime")
# list1 = [10,20,30,40,50,60]
# def lessthan(num):
#     return num<40
# newlist = list(filter(lessthan, list1))
# print("newlist is : ",newlist)
import sqlite3 
conn = sqlite3.connect('test')
cursor = conn.cursor()
print ("cursor = ",cursor)
#cursor.execute("create table studentdata1(name text, count integer)")
cursor.execute("insert into studentdata1 (name, count) values (?, ?)",("Jill", 15))
result = cursor.execute("select * from  studentdata1")
print(result.fetchall())
conn.commit()
conn.close()









    




