import os  # Import the os module, which provides a way to interact with the operating system

class Config:
    # Set the URI for the SQLAlchemy database
    # It tries to get the 'DATABASE_URL' environment variable, and if not found, it defaults to using a local SQLite database named 'employees.db'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///employees.db')
    
    # Disable SQLAlchemy event system to save resources and improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False
