from asyncpg import Record

class GetUserDomainClerkID_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "userId": str(record["userId"]),
      "nickname": str(record["nickname"]),
      "icon": str(record["icon"]),
      "domainId": str(record["domainId"]),
      "roomId": str(record["roomId"]),
      "live": bool(record["live"])
    }