from pydantic import BaseModel
from typing import Optional
import ujson

# get user domains request schema
class GetUserDomainsClerkID_RequestSchema(BaseModel):
  pass

# get user domains request schema
class GetUserDomainsClerkID_ResponseSchema(BaseModel):
  userId: str
  nickname: str
  icon: str
  domainId: str
  roomId: str
  live: bool

  class Config:
    json_dumps = ujson.dumps
    json_loads = ujson.loads
    allow_population_by_field_name = True