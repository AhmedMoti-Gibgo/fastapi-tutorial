from fastapi import HTTPException
from src.modules.chatbot_domain.domain_service import ChatbotDomainService
from src.connections.database import Database, get_db
from fastapi import Depends

class ChatbotDomainController:
  def __init__(self, db: Database = Depends(get_db)):
    self.chatbot_domain_service = ChatbotDomainService(db)

  async def domain_controller_get_user_domains_clerk_id(
    self,
    clerk_id: str
  ):
    data = await self.chatbot_domain_service.domain_service_get_user_domains_clerk_id(clerk_id)
    return data