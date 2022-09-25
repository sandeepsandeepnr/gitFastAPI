from fastapi import FastAPI
from api.authAPI import AuthAPI
from api.router import Router
from api.employee import Employee
from api.employeeRepository import EmployeeRepository
from api.analytics import Analytics
from api.db import initialize_db
from api.analyticsRepository import AnalyticsRepository
from api.employeeSerch import EmployeeSearch


app = FastAPI()
db = initialize_db()

auth_api = AuthAPI()
employeeRepository = EmployeeRepository(db)
analyticsRepository = AnalyticsRepository(db)
employeeSerch = EmployeeSearch()

employee = Employee(employeeRepository)
analytics = Analytics(analyticsRepository,employee)
router = Router(auth_api,employee,analytics,employeeSerch)

app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}