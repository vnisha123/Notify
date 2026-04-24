from sqlalchemy import Column, String, DateTime, Enum as SQLEnum, Text
from sqlalchemy.sql import func
from app.db_config.db import Base
from app.core.models import Channel
import uuid

class NotificationTable(Base):
    __tablename__ = "notifications"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    idempotency_key = Column(String, unique=True, index=True, nullable=False)
    channel = Column(SQLEnum(Channel), nullable=False)
    recipient = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    status = Column(String, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())