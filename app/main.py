from fastapi import FastAPI
from app.core.models import NotificationRequest

app = FastAPI()

@app.get("/")
def home():
    return{"message": "welcome to notify"}

@app.post("/notify")
async def send_notification(payload : NotificationRequest):
    return{"data":payload}