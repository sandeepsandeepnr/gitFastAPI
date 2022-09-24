
import boto3
import pathlib
from dotenv import load_dotenv
from boto3.resources.base import ServiceResource

base_dir = pathlib.Path(__file__).parent.parent.parent

load_dotenv(base_dir.joinpath('.env'))

class Config:
    DB_REGION_NAME = 'us-east-1'
    DB_ACCESS_KEY_ID = 'AKIAZBTEZ2WJYB472WN5'
    DB_SECRET_ACCESS_KEY = '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'
    

def initialize_db() -> ServiceResource:

    ddb = boto3.resource('dynamodb',
                         region_name=Config.DB_REGION_NAME,
                         aws_access_key_id=Config.DB_ACCESS_KEY_ID,
                         aws_secret_access_key=Config.DB_SECRET_ACCESS_KEY)

    return ddb