
class Person:
    def role(self):
        return "I am a person"
    
class Father(Person):
    def role (self):
        return "I am a father"
    
class Husband(Person):
    def role(self):
        return "I am a Husband"
    
class Employee(Person):
    def role(Self):
        return "I am a Employee"
    
p = Person()
f = Father()
h = Husband()
e = Employee()

print(p.role())
print(f.role())
print(h.role())
print(e.role())