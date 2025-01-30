from pydantic import BaseModel
import datetime
import ujson

# inheritance of classes will be done later (i.e. class CreateUser(BaseUser))

# request schema for getting live state (there is none since it is a path parameter)
class GetChatroomLive_Request(BaseModel):
  pass

# response schema for getting live state
class GetChatroomLive_Response(BaseModel):
  live: bool

  class Config:
    json_dumps = ujson.dumps
    json_loads = ujson.loads

# request schema for toggling chatroom live state
class ToggleChatroomLive_RequestSchema(BaseModel):
  id: str

class ToggleChatRoomLive_ResponseSchema(BaseModel):
  id: str
  live: bool

  class Config:
    json_dumps = ujson.dumps
    json_loads = ujson.loads

# request schema for updating chatroom live state
class UpdateChatroomLive_RequestSchema(BaseModel):
  id: str
  live: bool

# response schema for updating chatroom live state
class UpdateChatroomLive_ResponseSchema(BaseModel):
  id: str
  live: bool
  
  class Config: 
    json_dumps = ujson.dumps
    json_loads = ujson.loads