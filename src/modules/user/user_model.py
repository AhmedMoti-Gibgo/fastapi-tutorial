from asyncpg import Record
  
class CreateRegisteredUser_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]),
      "name": str(record["name"]),
      "type": str(record["type"])
    }
  
class User_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]),
      "name": str(record["name"]),
      "clerkId": str(record["clerkId"]),
      "type": str(record["type"]),
      "createdAt": record["createdAt"],
      "updatedAt": record["updatedAt"],
      "stripeId": str(record["stripeId"])
    }