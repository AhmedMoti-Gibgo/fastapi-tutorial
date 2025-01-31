from asyncpg import Record

class FindUserPlan_DBModel:
  def from_db(record: Record):
    return {
      "plan": str(record["plan"])
    }
  
class User_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]),
      "clerkId": str(record["clerkId"])
    }