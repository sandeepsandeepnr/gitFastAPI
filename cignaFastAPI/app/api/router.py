import imp
from fastapi import APIRouter
from fastapi import HTTPException

from api.authAPI import AuthAPI,Login
from api.employee import Employee,EmployeeModel
from api.analytics import Analytics,AnalyticsModel,UpdateAnalytics


class Router:
    def __init__(self, auth_api: AuthAPI,employee:Employee,analytics:Analytics ) -> None:
        self.__auth_api = auth_api
        self.__employee = employee
        self.__analytics = analytics

    @property
    def router(self):
        api_router = APIRouter(prefix='/api', tags=['api'])
        
        @api_router.get('/login')
        def create_login(login: Login):
            return self.__auth_api.post_login_user(login)

        @api_router.post('/employee')
        def create_employee(employeemodel: EmployeeModel):
            return self.__employee.create_employee(employeemodel)

        @api_router.get('/AllEmployees') 
        def get_all_employee():
            return self.__employee.get_all_employees()  

        @api_router.get('/employee/id/{user_id}')     
        def get_employee(user_id:str):
            return self.__employee.get_employee(user_id)  

        @api_router.post('/analytics')
        def create_analytics(analytics:AnalyticsModel):
            return self.__analytics.create_analytics(analytics)    

        @api_router.put('/analytics')
        def update_analytics(updateAnalytics:UpdateAnalytics):
            return self.__analytics.update_analytics()



        return api_router