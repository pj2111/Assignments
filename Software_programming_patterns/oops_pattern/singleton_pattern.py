class Singleton:
    """
    A thread-safe implementation of Singleton pattern
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class DatabaseConnection(Singleton):
    def __init__(self):
        # Initialize only if it hasn't been initialized
        if not hasattr(self, 'initialized'):
            self.connected = False
            self.db_name = None
            self.initialized = True
    
    def connect(self, db_name: str) -> None:
        if not self.connected:
            self.db_name = db_name
            self.connected = True
            print(f"Connected to database: {db_name}")
        else:
            print(f"Already connected to: {self.db_name}")
    
    def disconnect(self) -> None:
        if self.connected:
            print(f"Disconnected from: {self.db_name}")
            self.connected = False
            self.db_name = None
        else:
            print("Not connected to any database")

# Example usage
if __name__ == "__main__":
    # Create multiple instances - they will all be the same object
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    # Verify it's the same instance
    print(f"Are db1 and db2 the same instance? {db1 is db2}")
    
    # Use the connection
    db1.connect("MainDB")
    db2.connect("TestDB")  # This won't create a new connection
    
    # Both variables reference the same connection
    print(f"db1 database: {db1.db_name}")
    print(f"db2 database: {db2.db_name}") 