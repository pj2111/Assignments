from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

# Concrete Observers
class TemperatureDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Temperature Display: {temperature}°C")

class HumidityDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Humidity Display: {humidity}%")

class PressureDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"Pressure Display: {pressure} hPa")

# Example usage
if __name__ == "__main__":
    # Create the weather station
    weather_station = WeatherStation()
    
    # Create displays
    temp_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()
    pressure_display = PressureDisplay()
    
    # Register displays with the weather station
    weather_station.attach(temp_display)
    weather_station.attach(humidity_display)
    weather_station.attach(pressure_display)
    
    # Simulate weather changes
    print("Weather update 1:")
    weather_station.set_measurements(24.5, 65, 1013)
    
    print("\nWeather update 2:")
    weather_station.set_measurements(27.8, 70, 1014) 