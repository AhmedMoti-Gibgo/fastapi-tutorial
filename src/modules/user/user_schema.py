from pydantic import BaseModel
from datetime import datetime
import ujson

class UserBase(BaseModel):
  name: str
  clerkId: str
  type: str

class CreateUser(UserBase):
  pass

class UpdateUser(UserBase):
  pass

class User(UserBase):
  id: str
  createdAt: datetime
  updatedAt: datetime
  stripeId: str | None = None
  chatbotDomains: list[dict] | None = None

  class Config:
    orm_mode = True
    json_loads = ujson.loads
    json_dumps = ujson.dumps

class FindUserByIdResponseSchema(BaseModel):
  name: str
  id: str
  type: str

class ResponseSchema(BaseModel):
  status: int
  data: str | dict