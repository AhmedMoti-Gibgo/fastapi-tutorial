from asyncpg import exceptions
from src.connections.database import Database
from src.modules.user import user_model, user_schema
from fastapi import HTTPException

class UserService:
  def __init__(self, db: Database):
    self.db = db

  async def user_service_create_registered_user(
    self, 
    name: str,
    clerkId: str,
    type: str
  ):
    query_string = """
      INSERT INTO "User"
      (name, "clerkId", type)
      VALUES ($1, $2, $3)
      RETURNING id, name, type
    """
    try:
      result = await self.db.fetchrow(query_string, name, clerkId, type)
      if not result:
        raise HTTPException(status_code=404, detail="Failed to insert")
      return user_model.CreateRegisteredUser_DBModel.from_db(result)
    except exceptions.UniqueViolationError:
      raise HTTPException(status_code=400, detail="400 is probably incorrect")