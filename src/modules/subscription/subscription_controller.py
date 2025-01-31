from fastapi import Depends
from src.modules.chatroom import chatroom_schema
from src.modules.subscription.subscription_service import SubscriptionService
from src.connections.database import Database, get_db

class SubscriptionController:
  def __init__(self, db: Database = Depends(get_db)):
    self.subsciption_service = SubscriptionService(db)

  async def subscription_controller_get_subscription_plan_clerk_id(
    self,
    clerk_id: str
  ):
    subscription_data = await self.subsciption_service.subscription_service_find_user_plan(clerk_id)
    return subscription_data