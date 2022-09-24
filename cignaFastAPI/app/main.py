from fastapi import FastAPI
from api.authAPI import AuthAPI
from api.router import Router
from api.employee import Employee
from api.employeeRepository import EmployeeRepository
from api.analytics import Analytics
from api.db import initialize_db


app = FastAPI()
db = initialize_db()

auth_api = AuthAPI()
employeeRepository = EmployeeRepository(db)

employee = Employee(employeeRepository)
analytics = Analytics()
router = Router(auth_api,employee,analytics)

app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}