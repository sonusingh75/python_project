from extensions import db  # Import the db instance from the extensions module, which is an instance of SQLAlchemy

class Employee(db.Model):  # Define the Employee class, which inherits from db.Model, making it a SQLAlchemy model
    # Define the columns of the Employee table
    id = db.Column(db.Integer, primary_key=True)  # Integer column named 'id' that serves as the primary key
    name = db.Column(db.String(100), nullable=False)  # String column named 'name' with a maximum length of 100 characters, cannot be null
    position = db.Column(db.String(100), nullable=False)  # String column named 'position' with a maximum length of 100 characters, cannot be null
    department = db.Column(db.String(100), nullable=False)  # String column named 'department' with a maximum length of 100 characters, cannot be null

    def __repr__(self):  # Define the __repr__ method, which provides a string representation of an Employee instance
        return f'<Employee {self.name}>'  # Return a formatted string showing the name of the employee
