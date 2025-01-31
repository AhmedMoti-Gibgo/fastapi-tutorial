from asyncpg import exceptions
from src.connections.database import Database
from src.modules.subscription import subscription_model
from fastapi import HTTPException
from src.modules.user.user_model import User_DBModel

class SubscriptionService:
  def __init__(self, db: Database):
    self.db = db
    
  async def subscription_service_find_user_plan(
      self,
      clerk_id: str
  ):
    user_query_string = """
      SELECT *
      FROM "User"
      WHERE "clerkId" = $1
    """
    query_string = """
      SELECT plan
      FROM "Subscription"
      WHERE "userId" = $1
    """
    try:
      user = await self.db.fetchrow(user_query_string, clerk_id)
      if not user:
        raise HTTPException(status_code=404, detail="User not found")
      user = User_DBModel.from_db(user)
      result = await self.db.fetchrow(query_string, user["id"])
      if not result:
        raise HTTPException(status_code=404, detail="Chatroom not found")
      subsription = subscription_model.FindUserPlan_DBModel.from_db(result)
      return subscription_model.FindUserPlan_DBModel.from_db(result)
    except Exception as error:
      raise HTTPException(status_code=500, detail=f"Database error: {error}")