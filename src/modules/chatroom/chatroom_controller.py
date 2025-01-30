from fastapi import Depends
from src.modules.chatroom import chatroom_schema
from src.modules.chatroom.chatroom_service import ChatroomService
from src.connections.database import Database, get_db

class ChatroomController:
  def __init__(self, db: Database = Depends(get_db)):
    self.chatroom_service = ChatroomService(db)

  async def chatroom_service_update_chatroom_live(self, update_data: dict):
    return await self.chatroom_service.chatroom_service_update_chatroom_live(update_data)
  
  async def chatroom_controller_get_all_users(self):
    return await self.chatroom_service.poes_klap()
  
  async def chatroom_controller_update_chatroom_live_state(
    self,
    update_data: chatroom_schema.UpdateChatroomLive_RequestSchema
  ):
    updated_chatroom = await self.chatroom_service.chatroom_service_update_chatroom_live_state(
      chatroom_id=update_data.id,
      live=update_data.live
    )
    return chatroom_schema.UpdateChatroomLive_ResponseSchema(**updated_chatroom)
  
  async def chatroom_controller_toggle_live_state(
    self,
    update_data: chatroom_schema.ToggleChatroomLive_RequestSchema
  ):
    updated_chatroom = await self.chatroom_service.chatroom_service_toggle_live_state(update_data.id)
    return chatroom_schema.ToggleChatRoomLive_ResponseSchema(**updated_chatroom)
  
  async def chatroom_controller_get_live_state(
    self,
    chatroom_id: str
  ):
    live_state = await self.chatroom_service.chatroom_service_get_live_state(chatroom_id)
    return live_state