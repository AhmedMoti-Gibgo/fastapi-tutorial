from src.connections.database import Database

class DomainService:
  @staticmethod
  async def domain_service_get_all_account_domains(
    user_id: str,
    db: Database
  ):
    query_string = """
      SELECT id, nickname, "userId"
      FROM "ChatbotDomain"
      WHERE "userId" = 'c94f1ad8-3bd4-4f6a-a1ad-0ad0264d3283'
    """
    user_domains = await db.fetch(query_string)
    return user_domains