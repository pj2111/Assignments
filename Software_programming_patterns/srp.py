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


# Function perspective
# Incorrect way
def process_user_registration(user_data):
    # This function does too many things!
    
    # Validates user data
    if len(user_data['password']) < 8:
        raise ValueError("Password too short")
    if '@' not in user_data['email']:
        raise ValueError("Invalid email")
    
    # Saves user to database
    db = Database.connect()
    db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
               user_data['name'], user_data['email'], user_data['password'])
    
    # Sends welcome email
    smtp = SMTPClient()
    smtp.connect()
    smtp.send_email(
        to=user_data['email'],
        subject="Welcome!",
        body=f"Welcome {user_data['name']} to our platform!"
    )


# Better version
class UserValidator:
    def validate(self, user_data):
        self._validate_password(user_data['password'])
        self._validate_email(user_data['email'])
    
    def _validate_password(self, password):
        if len(password) < 8:
            raise ValueError("Password too short")
    
    def _validate_email(self, email):
        if '@' not in email:
            raise ValueError("Invalid email")

class UserRepository:
    def save(self, user_data):
        db = Database.connect()
        db.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            user_data['name'], user_data['email'], user_data['password']
        )

class EmailService:
    def send_welcome_email(self, user_data):
        smtp = SMTPClient()
        smtp.connect()
        smtp.send_email(
            to=user_data['email'],
            subject="Welcome!",
            body=f"Welcome {user_data['name']} to our platform!"
        )

def process_user_registration(user_data):
    # Each step is now handled by a specialized class
    validator = UserValidator()
    repository = UserRepository()
    email_service = EmailService()
    
    validator.validate(user_data)
    repository.save(user_data)
    email_service.send_welcome_email(user_data)