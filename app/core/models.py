from pydantic import BaseModel,Field,ConfigDict
from enum import Enum
from typing import Optional

class Channel(str, Enum):
    EMAIL = "email"
    SMS = "sms"

class NotificationRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    channel: Channel
    recipient: str = Field(..., description="Email, Phone number")
    content : str = Field(..., description="The actual message to be sent")
    subject: Optional[str] = Field(description="Subject for email")
    idempotency_key: str = Field(..., description="Unique Key to prevent duplicates")