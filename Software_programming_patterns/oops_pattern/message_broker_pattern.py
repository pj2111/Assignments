from typing import Dict, List, Any, Callable
from queue import Queue
from threading import Thread
import time
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Message:
    topic: str
    payload: Any
    timestamp: datetime = datetime.now()

class MessageBroker:
    """
    Message Broker implementation with topic-based queues and async delivery
    """
    def __init__(self):
        self._queues: Dict[str, Queue] = {}
        self._subscribers: Dict[str, List[Callable]] = {}
        self._running = True
        
        # Start message delivery thread
        self._delivery_thread = Thread(target=self._deliver_messages)
        self._delivery_thread.daemon = True
        self._delivery_thread.start()
    
    def create_topic(self, topic: str) -> None:
        """Create a new topic with its message queue"""
        if topic not in self._queues:
            self._queues[topic] = Queue()
            self._subscribers[topic] = []
            print(f"Created topic: {topic}")
    
    def subscribe(self, topic: str, subscriber: Callable) -> None:
        """Subscribe to a topic"""
        if topic not in self._subscribers:
            self.create_topic(topic)
        if subscriber not in self._subscribers[topic]:
            self._subscribers[topic].append(subscriber)
            print(f"Subscribed to topic: {topic}")
    
    def publish(self, message: Message) -> None:
        """Publish message to a topic"""
        if message.topic not in self._queues:
            self.create_topic(message.topic)
        self._queues[message.topic].put(message)
        print(f"Published message to topic: {message.topic}")
    
    def _deliver_messages(self) -> None:
        """Background thread for message delivery"""
        while self._running:
            for topic, queue in self._queues.items():
                if not queue.empty():
                    message = queue.get()
                    for subscriber in self._subscribers[topic]:
                        try:
                            subscriber(message)
                        except Exception as e:
                            print(f"Error delivering message: {e}")
            time.sleep(0.1)  # Prevent CPU overuse
    
    def stop(self) -> None:
        """Stop the message broker"""
        self._running = False
        self._delivery_thread.join()

# Example subscribers
class EmailNotifier:
    def __init__(self, email: str):
        self.email = email
    
    def notify(self, message: Message) -> None:
        print(f"Sending email to {self.email}: {message.payload} "
              f"(Topic: {message.topic}, Time: {message.timestamp})")

class SMSNotifier:
    def __init__(self, phone: str):
        self.phone = phone
    
    def notify(self, message: Message) -> None:
        print(f"Sending SMS to {self.phone}: {message.payload} "
              f"(Topic: {message.topic}, Time: {message.timestamp})")

class LoggingService:
    def log_message(self, message: Message) -> None:
        print(f"Logging: {message.payload} "
              f"(Topic: {message.topic}, Time: {message.timestamp})")

# Example usage
if __name__ == "__main__":
    # Create message broker
    broker = MessageBroker()
    
    # Create subscribers
    email_notifier = EmailNotifier("user@example.com")
    sms_notifier = SMSNotifier("+1234567890")
    logger = LoggingService()
    
    # Subscribe to topics
    broker.subscribe("alerts", email_notifier.notify)
    broker.subscribe("alerts", sms_notifier.notify)
    broker.subscribe("alerts", logger.log_message)
    broker.subscribe("logs", logger.log_message)
    
    # Publish messages
    print("\nPublishing messages:")
    broker.publish(Message("alerts", "System alert: High CPU usage"))
    broker.publish(Message("logs", "User login successful"))
    
    # Wait for messages to be delivered
    time.sleep(1)
    
    # Stop the broker
    broker.stop() 