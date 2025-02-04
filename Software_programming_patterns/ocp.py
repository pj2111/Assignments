from abc import ABC, abstractmethod

# Good Example
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2

# Adding new shapes doesn't require modifying existing code
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    
    def area(self) -> float:
        return 0.5 * self.base * self.height
