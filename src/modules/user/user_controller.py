from fastapi import HTTPException
from src.modules.user.user_service import UserService
from src.modules.user.user_schema import User, CreateUser, UpdateUser
from fastapi import status

class UserController:
  
  @staticmethod
  async def user_controller_get_many_items():
    try:
      return await UserService.user_service_get_many_items()
    except Exception as error:
      raise HTTPException(status_code=500,  detail=str(error))
    
  @staticmethod
  async def user_controller_get_item(item_id: str):
    item = await UserService.user_service_get_item(item_id)

    if not item:
      raise HTTPException(status_code=404, detail="item not found")
    
    return item
  
  @staticmethod
  async def user_controller_create_item(item_data: dict):
    item = await UserService.user_service_create_item(item_data)

    if not item:
      raise HTTPException(status_code=500, detail="TODO!!:")
  
  @staticmethod
  async def user_controller_update_item(user_id: str, user_date: UpdateUser):
    try: 
      return await UserService.user_service_update_item(user_id, user_date)
    except Exception as error:
      raise HTTPException(status_code=400, detail=str(error))