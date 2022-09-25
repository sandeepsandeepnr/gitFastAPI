
from pydantic import BaseModel
from uuid import uuid4
import datetime
from api.analyticsRepository import AnalyticsRepository
from api.employee import Employee


from fastapi import HTTPException
class AnalyticsModel(BaseModel):
    pageName: str
    PageUrl: str 
    PageId: str
    userid: str


class Analytics:

    
    def __init__(self, analyticsRepository: AnalyticsRepository,employee: Employee) -> None:
        self.__analyticsRepository = analyticsRepository
        self.__employee = employee
        

    def create_analytics(self,createAnalytics: AnalyticsModel ):
       
        try:
         
         id = str(createAnalytics.userid)
         empyoeedata =   self.__employee.get_employee(id)
    
         createAnalyticsDict = createAnalytics.dict()
         createAnalyticsDict['id'] =  str(uuid4())
         createAnalyticsDict['createdTime'] =  str(datetime.datetime.now())
         createAnalyticsDict['lastVisitTime'] = None
         return self.__analyticsRepository.create_employee_analytics(createAnalyticsDict)
        except KeyError:
            
            raise HTTPException(status_code=400, detail='No user found')


    def get_all_analytics(self):
        return self.__analyticsRepository.get_all_analyitcs()

    def get_analytics(self,id:str):
        try:
            return   self.__analyticsRepository.get_analytics(id)   
        except KeyError:
            raise HTTPException(status_code=400, detail='No AnalyticsDataFound found')

    def update_analytics(self,id:str):
        try:
            analyticsData = self.__analyticsRepository.get_analytics(id)
            analyticsData['lastVisitTime'] =  str(datetime.datetime.now())

            return  self.__analyticsRepository.update_analyitcs(analyticsData)
            
        except KeyError:
            raise HTTPException(status_code=400, detail='No AnalyticsDataFound found')

    def get_user_analytics(self,userid:str):
        try:
            userdata =    self.__employee.get_employee(userid) 
            return   self.__analyticsRepository.get_employee_analytics(userid)
        except KeyError:
            raise HTTPException(status_code=400, detail= 'no data found')        
        
