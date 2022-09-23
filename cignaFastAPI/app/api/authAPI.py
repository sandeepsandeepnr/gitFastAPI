

from pydantic import BaseModel



class Login(BaseModel):
    email:str
    password:str

class AuthAPI:
    
    def post_login_user(self,login:Login):
	    return login
