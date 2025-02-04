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
