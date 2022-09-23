from fastapi import FastAPI
from api.authAPI import AuthAPI
from api.router import Router
from api.employee import Employee
from api.analytics import Analytics


app = FastAPI()

auth_api = AuthAPI()
employee = Employee()
analytics = Analytics()
router = Router(auth_api,employee,analytics)

app.include_router(router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}