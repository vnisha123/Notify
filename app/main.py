from fastapi import FastAPI
from app.core.models import NotificationRequest
from app.db_config.db import engine, Base
from app.db_config.models import NotificationTable

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{"message": "welcome to notify"}

@app.post("/notify")
async def send_notification(payload : NotificationRequest):
    return{"data":payload}