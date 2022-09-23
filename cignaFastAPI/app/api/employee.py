from pydantic import BaseModel

class EmployeeModel(BaseModel):
    name: str
    email: str 
    password: str
    age: int | None = None  
    address: str | None = None

class Employee:

    def create_employee(self,employee: EmployeeModel):
        return 'create employee details  '
    def get_employee(self):
        return 'get  employee details '

    # def get_all_employee(self):
    #     return 'get  all employee details '

    def update_employee(self):
        return 'update employee details  '

    def delete_employee(self):
        return 'delete employee'