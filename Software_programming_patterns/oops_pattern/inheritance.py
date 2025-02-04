class Animal:
    """Base class demonstrating inheritance"""
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "Some sound"
    
    def get_name(self) -> str:
        return self.name

# Single Inheritance
class Dog(Animal):
    """Demonstrates single inheritance from Animal"""
    def speak(self) -> str:
        return "Woof!"
    
    def fetch(self) -> str:
        return f"{self.name} is fetching the ball"

# Multiple Inheritance
class FlyingMixin:
    """Mixin class to add flying capability"""
    def fly(self) -> str:
        return f"{self.name} is flying"

class SwimmingMixin:
    """Mixin class to add swimming capability"""
    def swim(self) -> str:
        return f"{self.name} is swimming"

class Duck(Animal, FlyingMixin, SwimmingMixin):
    """Demonstrates multiple inheritance"""
    def speak(self) -> str:
        return "Quack!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
print(dog.fetch())  # Output: Buddy is fetching the ball

duck = Duck("Donald")
print(duck.speak())  # Output: Quack!
print(duck.fly())   # Output: Donald is flying
print(duck.swim())  # Output: Donald is swimming 