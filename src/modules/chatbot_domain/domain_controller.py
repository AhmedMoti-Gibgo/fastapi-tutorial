from fastapi import HTTPException
from src.modules.chatbot_domain.domain_service import ChatbotDomainService
from src.modules.user.user_service import UserService
from src.connections.database import db

class ChatbotDomainController:
  
  @staticmethod
  async def domain_controller_get_domains(user_id: str):
    return ""
  
  @staticmethod
  async def domain_controller_get_domains_clerk_id(clerk_id: str):
    # first return the associated 'userId' for the given 'clerkId'
    user = await UserService.user_controller_user_clerk_id(clerk_id, db)
    user_id = user["id"]
    items = await ChatbotDomainService.domain_service_get_all_account_domains(user_id, db)
    if not items:
      raise HTTPException(status_code=404, detail="No associated domains found")
    return items