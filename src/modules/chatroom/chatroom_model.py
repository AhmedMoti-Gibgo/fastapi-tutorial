from asyncpg import Record

class ChatroomModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]), # UUID
      "live" : bool(record["live"]), # boolean
      "mailed": record.get("mailed", None), # boolean
      "createdAt": record.get("createdAt", None), # DateTime
      "updatedAt": record.get("updatedAt", None), # DateTime
      "customerId": str(record.get("customerId", "")) # UUID
    }
  
class ToggleChatroomLive_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]),
      "live": bool(record["live"])
    }
  
class GetChatroomLive_DBModel:
  @staticmethod
  def from_db(live_state: bool):
    return {
      "live": live_state
    }