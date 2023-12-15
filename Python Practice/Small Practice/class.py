class SayHello:
    count =0                #class level variable
    def __init__(self, msg="Hello World!!"):                 #constructor method
        print("Inside constructor , self = ", self)#<__main__.SayHello object at 0x103016da0>
        self.greeting = msg
        SayHello.count += 1
    def display(self):                      #instance method
        print("Greeting message = ",self.greeting)
ob1 =  SayHello()#this transfers the cotrol to the default constructior method __init__
#it passes the loaded memory as the implicit parameter
print("Ob1  = ", ob1)#Ob1  =  <__main__.SayHello object at 0x103016da0>
print("ob1.greeting = ", ob1.greeting)
ob1.display()  #method call over an object, ob1 itself passed as parameter to the display method
print("----------------------------------------")
ob2 =  SayHello("Hello Everyone!!!")#2 memeory, 'Hello everyone'
print("Ob2  = ", ob2)#
print("ob1.greeting = ", ob2.greeting)
ob2.display()#ob2 itself is passed as a parametr to the disp