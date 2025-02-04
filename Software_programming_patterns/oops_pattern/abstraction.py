from abc import ABC, abstractmethod

# Abstract base class demonstrating abstraction
class Vehicle(ABC):
    """
    Abstract base class that defines the interface for vehicles
    Demonstrates abstraction by hiding implementation details
    """
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self) -> str:
        """Abstract method that must be implemented by concrete classes"""
        pass
    
    @abstractmethod
    def stop_engine(self) -> str:
        """Abstract method that must be implemented by concrete classes"""
        pass
    
    def get_info(self) -> str:
        """Concrete method available to all subclasses"""
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """Concrete implementation of Vehicle for cars"""
    def start_engine(self) -> str:
        return "Car engine starting with key turn"
    
    def stop_engine(self) -> str:
        return "Car engine stopped"
    
    def drive(self) -> str:
        return "Car is being driven"

class ElectricCar(Vehicle):
    """Another concrete implementation showing different behavior"""
    def start_engine(self) -> str:
        return "Electric car powering up silently"
    
    def stop_engine(self) -> str:
        return "Electric car powered down"
    
    def charge(self) -> str:
        return "Electric car is charging"

# Example usage
car = Car("Toyota", "Camry")
print(car.get_info())      # Uses inherited method
print(car.start_engine())  # Uses overridden method
print(car.drive())         # Uses class-specific method

electric_car = ElectricCar("Tesla", "Model 3")
print(electric_car.get_info())      # Uses inherited method
print(electric_car.start_engine())  # Different implementation
print(electric_car.charge())        # Class-specific method 