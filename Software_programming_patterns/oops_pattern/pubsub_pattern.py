from typing import Dict, List, Callable
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
    topic: str
    data: str
    timestamp: datetime = datetime.now()

class PubSub:
    """
    Publisher-Subscriber implementation with topic-based messaging
    """
    def __init__(self):
        # Dictionary to store topics and their subscribers
        self._subscribers: Dict[str, List[Callable]] = {}
    
    def subscribe(self, topic: str, subscriber: Callable) -> None:
        """Subscribe to a topic"""
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(subscriber)
        print(f"Subscribed to topic: {topic}")
    
    def unsubscribe(self, topic: str, subscriber: Callable) -> None:
        """Unsubscribe from a topic"""
        if topic in self._subscribers and subscriber in self._subscribers[topic]:
            self._subscribers[topic].remove(subscriber)
            print(f"Unsubscribed from topic: {topic}")
    
    def publish(self, message: Message) -> None:
        """Publish a message to a topic"""
        if message.topic in self._subscribers:
            for subscriber in self._subscribers[message.topic]:
                subscriber(message)

# Example subscribers
class NewsAgency:
    def __init__(self, name: str):
        self.name = name
    
    def receive_news(self, message: Message) -> None:
        print(f"{self.name} received news: {message.data} "
              f"(Topic: {message.topic}, Time: {message.timestamp})")

class WeatherStation:
    def __init__(self, location: str):
        self.location = location
    
    def receive_weather_update(self, message: Message) -> None:
        print(f"Weather station at {self.location} received update: {message.data} "
              f"(Topic: {message.topic}, Time: {message.timestamp})")

# Example usage
if __name__ == "__main__":
    # Create PubSub system
    pubsub = PubSub()
    
    # Create subscribers
    reuters = NewsAgency("Reuters")
    ap = NewsAgency("Associated Press")
    ny_weather = WeatherStation("New York")
    la_weather = WeatherStation("Los Angeles")
    
    # Subscribe to topics
    pubsub.subscribe("news", reuters.receive_news)
    pubsub.subscribe("news", ap.receive_news)
    pubsub.subscribe("weather", ny_weather.receive_weather_update)
    pubsub.subscribe("weather", la_weather.receive_weather_update)
    
    # Publish messages
    print("\nPublishing news:")
    pubsub.publish(Message("news", "Breaking: Important event occurred!"))
    
    print("\nPublishing weather update:")
    pubsub.publish(Message("weather", "Severe weather warning issued"))
    
    # Unsubscribe and publish again
    print("\nUnsubscribing AP from news:")
    pubsub.unsubscribe("news", ap.receive_news)
    
    print("\nPublishing news after unsubscribe:")
    pubsub.publish(Message("news", "Another important event!")) 