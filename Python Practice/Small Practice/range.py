#rangeobj = range(5)
#print("Range is :", rangeobj)
#list1 = list(rangeobj)
#print("list ia :",list1)
#def display():
 #   print("In display function")
#Fin = open("data.txt", "r")
#print(Fin)
#data = Fin.readlines()
#print("data =", data)
# fout = open("target.txt","w")
# fout.write("Persistent!!\n")
# fout.write("ABC!!")
# fout.close()
class SayHello:
    def __init__(self, msg="Hello World!!"):
        print("Inside Constructor ,self =" , self)
        self.greeting = msg
    def display(self):
        print("Greeting message =",self.greeting)