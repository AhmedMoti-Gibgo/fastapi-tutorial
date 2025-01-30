from src.connections.database import Database

class ChatbotDomainService:
  @staticmethod
  async def domain_service_get_all_account_domains(
    user_id: str,
    db: Database
  ):
    query_string = """
      SELECT id, nickname, "userId"
      FROM "ChatbotDomain"
      WHERE "userId" = $1
    """
    user_domains = await db.fetch(query_string, user_id)
    return user_domains