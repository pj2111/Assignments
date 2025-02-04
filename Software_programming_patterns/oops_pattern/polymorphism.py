from abc import ABC, abstractmethod
from typing import List

# Abstract base class demonstrating polymorphism
class Shape(ABC):
    """Abstract base class for shapes"""
    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate perimeter of the shape"""
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14 * self.radius

# Function demonstrating polymorphic behavior
def print_shape_info(shapes: List[Shape]) -> None:
    """
    This function works with any shape that inherits from Shape class
    Demonstrates polymorphism through method overriding
    """
    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")

# Example usage
shapes = [Rectangle(5, 3), Circle(4)]
print_shape_info(shapes) 