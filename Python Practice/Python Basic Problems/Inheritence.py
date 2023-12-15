class A:
    def method1(self):
        return "Method 1 from Class A"
    
class B(A):
    def method2(self):
        return "Method 2 from class B"
    
class C(A):
    def method3(self):
        return "Method 3 from class C"
    
obj_b = B()
obj_c = C()

print(obj_b.method1())
print(obj_b.method2())
print(obj_c.method1())
print(obj_c.method3())
