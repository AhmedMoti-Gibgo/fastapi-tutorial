from fastapi import HTTPException
from src.modules.user.user_service import UserService
import src.modules.user.user_schema as UserSchema
from fastapi import status
# from src.modules.chatbot_domain.domain_service import DomainService
from src.connections.database import db
from src.modules.user import user_schema

class UserController:
  
  @staticmethod
  async def user_controller_get_many_items():
    try:
      return await UserService.user_service_get_many_items(db)
    except Exception as error:
      raise HTTPException(status_code=500,  detail=str(error))
    
  @staticmethod
  async def user_controller_get_item(user_id: str):
    item = await UserService.user_service_get_item(user_id, db)

    if not item:
      raise HTTPException(status_code=404, detail="item not found")
    
    return item
  
  @staticmethod
  async def user_controller_create_item(item_data: user_schema.user_schema_CreateUser):
    try:
      item_data_dict = item_data.model_dump()
      item = await UserService.user_service_create_item(item_data_dict, db)
      if not item:
        raise HTTPException(status_code=500, detail="User could not be created")
      return {
        "status": 201,
        "data": item
      }
    except Exception as error:
      raise HTTPException(status_code=500, detail=str(error))
  
  @staticmethod
  async def user_controller_update_item(user_id: str, user_date: UserSchema.user_schema_UpdateUser):
    try: 
      return await UserService.user_service_update_item(user_id, user_date)
    except Exception as error:
      raise HTTPException(status_code=400, detail=str(error))
    
  @staticmethod
  async def user_controller_get_item_clerk_id(clerk_id: str):
    item = await UserService.find_user_by_clerk_id(clerk_id, db)
    if not item:
      raise HTTPException(status_code=404, detail="Item not found")
    return item