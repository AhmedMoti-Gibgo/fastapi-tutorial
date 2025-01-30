from src.connections.database import Database

class ChatbotDomainService:
  
  @staticmethod
  async def domain_service_get_domains(user_id: str, db: Database):
    query_string = ""
    return ""
  
  @staticmethod
  async def domain_service_get_domains_clerk_id(clerk_id: str, db: Database):
    query_string = """
      SELECT
    """
    item = await db.fetch(query_string)
    return item