from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass

# Concrete Products
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"
    
    def get_type(self) -> str:
        return "Dog"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"
    
    def get_type(self) -> str:
        return "Cat"

class Duck(Animal):
    def speak(self) -> str:
        return "Quack!"
    
    def get_type(self) -> str:
        return "Duck"

# Factory Class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        """Factory method to create animals"""
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "duck":
            return Duck()
        else:
            raise ValueError(f"Animal type {animal_type} not supported")

# Example usage
if __name__ == "__main__":
    factory = AnimalFactory()
    
    # Create different animals using the factory
    animals = [
        factory.create_animal("dog"),
        factory.create_animal("cat"),
        factory.create_animal("duck")
    ]
    
    # Make them speak
    for animal in animals:
        print(f"The {animal.get_type()} says: {animal.speak()}") 