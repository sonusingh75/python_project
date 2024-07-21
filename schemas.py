from extensions import ma  # Import the ma instance from the extensions module, which is an instance of Marshmallow
from models import Employee  # Import the Employee model from the models module

class EmployeeSchema(ma.SQLAlchemyAutoSchema):  # Define the EmployeeSchema class, inheriting from Marshmallow's SQLAlchemyAutoSchema
    class Meta:  # Meta class to hold schema configuration
        model = Employee  # Specify the model to base the schema on
        load_instance = True  # Indicates that deserialization should return a model instance

# Create an instance of the EmployeeSchema for single employee serialization/deserialization
employee_schema = EmployeeSchema()  

# Create an instance of the EmployeeSchema for multiple employees serialization/deserialization
employees_schema = EmployeeSchema(many=True)  
