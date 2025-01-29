from fastapi import HTTPException
from src.modules.user.user_service import UserService
import src.modules.user.user_schema as UserSchema
from fastapi import status
from src.modules.chatbot_domain.domain_service import DomainService
from src.connections.database import db

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
  async def user_controller_update_item(user_id: str, user_date: UserSchema.UpdateUser):
    try: 
      return await UserService.user_service_update_item(user_id, user_date)
    except Exception as error:
      raise HTTPException(status_code=400, detail=str(error))
    
  @staticmethod
  async def user_service_on_login(clerk_id: str):
    try:
      user = await UserService.find_user_by_clerk_id(clerk_id, db)
      if not user:
        return { # TO.DO!!: apply a model to this (e.g. AppResponse(status=400, data=""))
          "status": 400,
          "data": "No user found in the database"
        }
      domains = await DomainService.domain_service_get_all_account_domains(user["id"], db)
      if domains:
        return {
          "status": 200,
          "data": {
            "user":  UserSchema.User.model_validate(user).model_dump(),
            "user_domains": [dict(domainItem) for domainItem in domains]
          }
        }
      return {
        "status": 400,
        "data": dict(UserSchema.User)
      }
    except Exception as error:
      raise HTTPException(
        status_code=500,
        detail=str(error)
      )