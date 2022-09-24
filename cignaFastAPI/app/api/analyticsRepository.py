from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource

class AnalyticsRepository:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all_analyitcs(self):
        table = self.__db.Table('analytics')
        response = table.scan()
        return response.get('Items', [])

    def get_analytics(self, id: str):
        try:
            table = self.__db.Table('analytics')
            response = table.get_item(Key={'id': id})
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def get_employee_analytics(self, userid: str):
       try:
            table = self.__db.Table('analytics')
            response = table.get_item(Key={'userid': userid})
            return response['Item']
       except ClientError as e:
            raise ValueError(e.response['Error']['Message'])
     
    def create_employee_analytics(self, analytics: dict):
        table = self.__db.Table('analytics')
        response = table.put_item(Item=analytics)
        return response
    

    def update_analyitcs(self, analytics: dict):
        table = self.__db.Table('analytics')
        response = table.update_item(
            Key={'id': analytics.get('id')},
            UpdateExpression="""
                set
                    lastVisitTime=:lastVisitTime
                   
                    
            """,
            ExpressionAttributeValues={
                ':lastVisitTime': analytics.get('lastVisitTime')
                   
            },
            
            ReturnValues="UPDATED_NEW"
        )
        return response

    def delete_employee(self, id: str):
        table = self.__db.Table('analytics')
        response = table.delete_item(
            Key={'id': id}
        )
        return response