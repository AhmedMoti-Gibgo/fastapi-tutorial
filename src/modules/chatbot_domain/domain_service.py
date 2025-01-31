from src.connections.database import Database
from fastapi import HTTPException
from src.modules.chatbot_domain import domain_model
class ChatbotDomainService:
  def __init__(self, db: Database):
    self.db = db

  async def domain_service_get_user_domains_clerk_id(
    self,
    clerk_id: str
  ):
    query_string = """
      SELECT "ChatbotDomain"."userId", "ChatbotDomain"."nickname", "ChatbotDomain"."icon", "ChatbotDomain"."id" as "domainId", "ChatRoom"."id" as "roomId", "ChatRoom"."live"
      FROM "ChatbotDomain"
      LEFT JOIN "User" ON "User"."id" = "ChatbotDomain"."userId"
      LEFT JOIN "Customer" ON "ChatbotDomain"."id" = "Customer"."domainId"
      LEFT JOIN "ChatRoom" ON "Customer"."id" = "ChatRoom"."customerId"
      WHERE "User"."clerkId" = $1
    """
    try:
      result = await self.db.fetch(query_string, clerk_id)
      if not result:
        raise HTTPException(status_code=404, detail="User not found")
      # return domain_model.GetUserDomainClerkID_DBModel.from_db(result[0])
      return [domain_model.GetUserDomainClerkID_DBModel.from_db(resultItem) for resultItem in result]
    except Exception as error:
      raise HTTPException(status_code=500, detail=f"Database error: {error}")