from pydantic import BaseModel, Field
from datetime import datetime
import ujson
from enum import Enum

class UserTypeEnum(str, Enum):
  student = "student"
  business = "business"

class user_schema_UserBase(BaseModel):
  name: str = Field(..., description="Full name of the user")
  clerkId: str = Field(..., description="Unique Clerk ID of the user")
  type: UserTypeEnum = Field(..., description="Type of user (i.e. 'student' or 'business')")

class user_schema_CreateUser(user_schema_UserBase):
  pass
  
class user_schema_UpdateUser(user_schema_UserBase):
  name: str | None = None
  type: UserTypeEnum | None = None

class User(user_schema_UserBase):
  id: str
  createdAt: datetime
  updatedAt: datetime
  stripeId: str | None = None

  class Config:
    orm_mode = True
    json_loads = ujson.loads
    json_dumps = ujson.dumps

class user_schema_FindUserByIdResponseSchema(BaseModel):
  name: str
  id: str
  type: str

class user_schema_ResponseSchema(BaseModel):
  status: int
  data: str | dict