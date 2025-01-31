from pydantic import BaseModel, Field
from typing import Optional
import ujson
import datetime
import ujson

# inheritance of classes will be done later (i.e. class CreateUser(BaseUser))

# request schema for getting live state (there is none since it is a path parameter)
class GetSubscriptionPlanClerkId_RequestSchema(BaseModel):
  clerkId: str

# response schema for getting live state
class GetSubscriptionPlanClerkId_ResponseSchema(BaseModel):
  plan: bool

  class Config:
    json_dumps = ujson.dumps
    json_loads = ujson.loads
    allow_population_by_field_name = True