from uuid import uuid4
from pydantic import BaseModel
from fastapi import HTTPException

import boto3
import os
import requests
import tqdm
from typing import List, Optional
from api.employeeRepository import EmployeeRepository

class EmployeeModel(BaseModel):
    #id: Optional[str] = None
    name: str
    email: str 
    password: str
    age: int | None = None  
    address: str | None = None

class Employee:

    def __init__(self, employeeRepository: EmployeeRepository) -> None:
        self.__employeeRepository = employeeRepository

    def create_employee(self,employee: EmployeeModel):

        #employee.id = str(uuid4())
        employeeDict = employee.dict()
        employeeDict['id'] =  str(uuid4())

        return self.__employeeRepository.create_employee(employeeDict)
        # dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1',
        #       aws_access_key_id = 'AKIAZBTEZ2WJYB472WN5',
        #       aws_secret_access_key = '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')
        # employee_table = dynamo_client.Table('employee') 

        # employee_table.put_item(Item = employee.dict())

        return  employee.dict()

    def get_all_employees(self):
        return self.__employeeRepository.get_all_employee()

    def get_employee(self,id: str):
        try:
            return self.__employeeRepository.get_employee(id)
        except KeyError:
            raise HTTPException(status_code=400, detail='No user found')
       

    def update_employee(self,employee: EmployeeModel):
       
        return self.__employeeRepository.update_employee(employee.dict())

    def delete_employee(self,id:str):
        return self.__employeeRepository.delete_employee(id)