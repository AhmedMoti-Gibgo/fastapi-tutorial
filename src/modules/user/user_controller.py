from fastapi import Depends
from src.modules.user import user_schema
from src.modules.user.user_service import UserService
from src.connections.database import Database, get_db

class UserController:
  def __init__(self, db: Database = Depends(get_db)):
    self.user_service = UserService(db)

  async def user_controller_create_registered_user(
    self, 
    create_data: user_schema.CreateRegisteredUser_RequestSchema
  ):
    return await self.user_service.user_service_create_registered_user(create_data.name, create_data.clerkId, create_data.type)