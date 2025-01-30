from asyncpg import Record
  
class CreateRegisteredUser_DBModel:
  @staticmethod
  def from_db(record: Record):
    return {
      "id": str(record["id"]),
      "name": str(record["name"]),
      "type": str(record["type"])
    }