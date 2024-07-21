from extensions import ma
from models import Employee

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
