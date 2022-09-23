
from pydantic import BaseModel

class AnalyticsModel(BaseModel):
    pageName: str
    PageUrl: str 
    PageId: str
    created: str
    lastVisitTime: str | None = None
    userid: str

class UpdateAnalytics(BaseModel):

     analyitcs_id: str
     lastVisitTime: str    


class Analytics:

    def create_analytics(self,createAnalytics :AnalyticsModel ):
        return createAnalytics

    def update_analytics(self,updateAnalytics: UpdateAnalytics):
        return updateAnalytics
