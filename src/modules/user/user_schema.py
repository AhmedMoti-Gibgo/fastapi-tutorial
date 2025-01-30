from pydantic import BaseModel, Field
from datetime import datetime
import ujson
from enum import Enum

# work on inheritance later

class UserTypeEnum(str, Enum):
  student = "student"
  business = "business"

# create registered user request schema
class CreateRegisteredUser_RequestSchema(BaseModel):
  name: str
  clerkId: str
  type: UserTypeEnum

# create registered user response schema
class CreateRegisteredUser_ResponseSchema(BaseModel):
  name: str
  id: str
  type: UserTypeEnum

  class Config:
    json_dumps = ujson.dumps
    json_loads = ujson.loads