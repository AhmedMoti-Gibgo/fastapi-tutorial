from asyncpg import exceptions
from src.connections.database import Database
from src.modules.chatroom import chatroom_model
from fastapi import HTTPException

class ChatroomService:
  def __init__(self, db: Database):
    self.db = db

  async def chatroom_service_update_chatroom_live(self, update_data):
    query_string = """
      UPDATE "ChatRoom"
      SET ("live" = $2)
      WHERE "ChatRoom"."id" = $1
    """
    try:
      result = self.db.execute(query_string, update_data["id"], update_data["live"])
    except exceptions.UniqueViolationError:
      raise HTTPException(status_code=400, detail="400 is probably incorrect")
    return chatroom_model.ChatroomModel.from_db(result[0])
  
  async def chatroom_service_update_chatroom_live_state(
    self,
    chatroom_id: str,
    live: bool
  ):
    query_string = """
      UPDATE "ChatRoom"
      SET "live" = $1
      WHERE "ChatRoom"."id" = $2
      RETURNING id, live
    """
    try:
      result = await self.db.fetchrow(query_string, live, chatroom_id)
      if not result:
        raise HTTPException(status_code=404, detail="Chatroom not found")
      return chatroom_model.ChatroomModel.from_db(result)
    except Exception as error:
      raise HTTPException(
        status_code=500,
        detail=f"Database error: {error}"
      )
    
  async def chatroom_service_toggle_live_state(
      self,
      chatroom_id: str
  ):
    query_string = """
      UPDATE "ChatRoom"
      SET live = NOT live
      WHERE id = $1
      RETURNING id, live
    """
    try:
      result = await self.db.fetchrow(query_string, chatroom_id)
      if not result:
        raise HTTPException(status_code=404, detail="Chatroom not found")
      return chatroom_model.ToggleChatroomLive_DBModel.from_db(result)
    except Exception as error:
      raise HTTPException(status_code=500, detail=f"Database error: {str(error)}")
    
  async def chatroom_service_get_live_state(
      self,
      chatroom_id: str
  ):
    query_string = """
      SELECT live
      FROM "ChatRoom"
      WHERE id = $1
    """
    try:
      result = await self.db.fetchval(query_string, chatroom_id)
      if result is None:
        raise HTTPException(status_code=404, detail="Chatroom not found")
      return chatroom_model.GetChatroomLive_DBModel.from_db(result)
    except Exception as error:
      raise HTTPException(status_code=500, detail=f"Database error: {error}")