from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource

class EmployeeRepository:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all_employee(self):
        table = self.__db.Table('employee')
        response = table.scan()
        return response.get('Items', [])

    def get_employee(self, id: str):
        try:
            table = self.__db.Table('employee')
            response = table.get_item(Key={'id': id})
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def create_employee(self, employee: dict):
        table = self.__db.Table('employee')
        response = table.put_item(Item=employee)
        return response

    def update_employee(self, employee: dict):
        table = self.__db.Table('employee')
        response = table.update_item(
            Key={'uid': employee.get('uid')},
            UpdateExpression="""
                set
                    name=:name,
                    email=:email,
                    password=:password,
                    age=:age,
                    address=:address
            """,
            ExpressionAttributeValues={
                ':name': employee.get('name'),
                ':email': employee.get('email'),
                ':password': employee.get('password'),
                ':age': employee.get('age'),
                ':address': employee.get('address')
            },
            ReturnValues="UPDATED_NEW"
        )
        return response

    def delete_employee(self, uid: str):
        table = self.__db.Table('employee')
        response = table.delete_item(
            Key={'uid': uid}
        )
        return response