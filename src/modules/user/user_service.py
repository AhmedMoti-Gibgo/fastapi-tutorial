from src.connections.database import Database
# from src.modules.chatbot_domain.domain_service import DomainService

class UserService:
  
  @staticmethod
  async def user_service_get_many_items(db: Database):
    query_string = """
      SELECT *
      FROM "User"
    """
    return await db.fetch(query_string)
  
  @staticmethod
  async def user_service_get_item(user_id: str, db: Database):
    query_string = """
      SELECT "clerkId"
      FROM "User"
      WHERE "id" = $1
    """ # TODO!!: Remove dynamic values from string to avoid XSS attacks
    return await db.fetchrow(query_string, user_id)
  
  @staticmethod
  async def user_controller_user_clerk_id(clerk_id: str, db: Database):
    query_string = """
      SELECT id
      FROM "User"
      WHERE "clerkId" = $1
    """
    return await db.fetchrow(query_string, clerk_id)
  
  @staticmethod
  async def user_service_create_item(item_data: dict, db: Database):
    query_string = """
      INSERT INTO "User" (name, "clerkId", type)
      VALUES ($1, $2, $3)
      RETURNING id
    """ # TODO!!: Remove dynamic values from string to avoid XSS attacks
    # return await db.database_fetchrow(query_string, item_data["name"], item_data["clerkId"], item_data["type"])
    return await db.execute(query_string, item_data["name"], item_data["clerkId"], item_data["type"])
  
  @staticmethod
  async def user_service_update_item(item_id: str, item_data: dict, db: Database):
    query_string = f"""
      UPDATE "User"
      SET ({item_data.value})
      WHERE "User"."id" = {item_id}
    """
    return await db.database_execute(query_string)
  
  @staticmethod
  async def find_user_by_clerk_id(
    clerk_id: str, db: Database
  ):
    query_string = """
      SELECT name, id, type
      FROM "User"
      WHERE "clerkId" = $1
    """
    user = await db.fetchrow(query_string, clerk_id)
    return user