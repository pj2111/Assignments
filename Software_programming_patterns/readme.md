I'll explain the SOLID principles, which are five design principles in object-oriented programming that help create more maintainable and scalable software.

Let's break down each principle with examples:

1. **S - Single Responsibility Principle (SRP)**
Each class should have only one reason to change, meaning it should have only one job or responsibility.

```python:srp.py
# Bad Example - Multiple responsibilities
class User:
    def __init__(self, name: str):
        self.name = name
    
    def get_user_data(self):
        # Gets user data
        pass
    
    def save_to_database(self):
        # Saves to database
        pass
    
    def generate_report(self):
        # Generates report
        pass

# Good Example - Single responsibility
class User:
    def __init__(self, name: str):
        self.name = name
    
    def get_user_data(self):
        # Gets user data
        pass

class UserRepository:
    def save_to_database(self, user):
        # Saves to database
        pass

class UserReportGenerator:
    def generate_report(self, user):
        # Generates report
        pass
```

2. **O - Open/Closed Principle (OCP)**
Software entities should be open for extension but closed for modification.

```python:ocp.py
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
```

3. **L - Liskov Substitution Principle (LSP)**
Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

```python:lsp.py
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
```

4. **I - Interface Segregation Principle (ISP)**
Clients should not be forced to depend on interfaces they don't use.

```python:isp.py
from abc import ABC, abstractmethod

# Bad Example
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

# Good Example
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        return "Working"
    
    def eat(self):
        return "Eating"
    
    def sleep(self):
        return "Sleeping"

class Robot(Workable):
    def work(self):
        return "Working"
```

5. **D - Dependency Inversion Principle (DIP)**
High-level modules should not depend on low-level modules. Both should depend on abstractions.

```python:dip.py
from abc import ABC, abstractmethod

# Bad Example
class EmailNotifier:
    def send_email(self, message):
        print(f"Sending email: {message}")

class UserManager:
    def __init__(self):
        self.notifier = EmailNotifier()  # Direct dependency
    
    def change_password(self):
        # Change password logic
        self.notifier.send_email("Password changed")

# Good Example
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass

class EmailNotifier(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending email: {message}")

class SMSNotifier(NotificationService):
    def send_notification(self, message: str):
        print(f"Sending SMS: {message}")

class UserManager:
    def __init__(self, notifier: NotificationService):
        self.notifier = notifier  # Dependency injection
    
    def change_password(self):
        # Change password logic
        self.notifier.send_notification("Password changed")

# Usage
email_notifier = EmailNotifier()
user_manager = UserManager(email_notifier)
user_manager.change_password()

# Can easily switch to SMS notification
sms_notifier = SMSNotifier()
user_manager = UserManager(sms_notifier)
user_manager.change_password()
```

These SOLID principles help create code that is:
- Easier to maintain
- Easier to understand
- Easier to extend
- More reusable
- More testable

Following these principles helps avoid common pitfalls in software design and leads to more robust and maintainable applications. However, it's important to note that these principles should be applied with pragmatism - sometimes strictly following them might lead to over-engineering for simple problems.
