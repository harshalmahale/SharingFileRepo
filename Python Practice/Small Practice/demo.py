#s1 = {1,2,3,3,3,3}
#s1.add(22)
#print(s1)
#s4 = {3,3,3,4,4,5,6,6,5}
#print(s4)
#newset = s1 & s4
#print("Intersection is :",newset)
emp = {'1a':25000,'2a':45000,'1a': 33000}
print("emp", emp ,"type", type(emp), "id", id(emp))
while True:
    line1 = input("Enter EmpId:salary")
    if line1 == "": break
    list1 = line1.split(":")
    emp[list1[0]]=list1[1]
    print("emp", emp ,"type", type(emp), "id", id(emp))
totalitems=emp.items()
print("total items is :", totalitems)

