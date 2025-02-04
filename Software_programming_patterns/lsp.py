from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

# Bad Example - Violates LSP
class Penguin(Bird):
    def fly(self):
        raise Exception("I can't fly")  # Breaks substitution

# Good Example
class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmingBird(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(FlyingBird, SwimmingBird):
    def fly(self):
        return "Flying"
    
    def swim(self):
        return "Swimming"

class Penguin(SwimmingBird):
    def swim(self):
        return "Swimming"
