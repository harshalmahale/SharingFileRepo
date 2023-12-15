# print("\U0001F602")
# print("Harshal")
# print(r"this is \n")
# print('\U0001F602')
# x = 2
# y = 3
# z = 5
# avg = ((x+y+z)/3)
# print(f"Average of {x},{y},{z} is {avg}")
# num1,num2,num3 = input("Enter the three numbers comma separated:").split(",")
# print(f"Average of three numbers is:", int(num1+num2+num3)/3)
# n = "Harshal"
# print(n[0:3])
# print("Harshal"[3::-1])
# name = "HaRsHaL MaHaLe"
# print (name.count("a"))
list1 = [10,20,30,40,50]
def squareElement(num):
    return num**2
mapobj = map(squareElement, list1)
print("mapobj", mapobj)
squarelist3 =list(mapobj)
print("Squareelementis :", squarelist3)
