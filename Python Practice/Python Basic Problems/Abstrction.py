# We can achieve abstraction using abstract base classes (ABC) from the abc module
# The abc module is used to create an abstract base class Shape with the @abstractmethod
# decorator to define an abstract method area. 

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    

obj_circle = Circle(3)
obj_square = Square(4)

print(obj_circle.area())
print(obj_square.area())
