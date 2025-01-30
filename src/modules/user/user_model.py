from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime
import uuid

Base = declarative_base()

class UserModel(Base):
  __tablename = "User"

  id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
  name = Column(String, nullable=False)
  clerkId = Column(String, unique=True, nullable=False)
  type = Column(String, nullable=False)
  createdAt = Column(DateTime, default=datetime.datetime.utcnow)
  updatedAt = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)