from fastapi import APIRouter, Depends, HTTPException, Path
from src.modules.subscription.subscription_controller import SubscriptionController
from src.modules.subscription import subscription_schema
from fastapi.responses import UJSONResponse

router = APIRouter(
    prefix="/api/v1/subscription",
    tags=["subscription"],
    default_response_class=UJSONResponse
)

@router.get("/{clerk_id}/subscription")
async def subscription_route_get_subscription_plan_clerk_id(
    clerk_id: str = Path(..., description="Clerk ID used to find the user, and therefore the subscription plan"), 
    controller: SubscriptionController = Depends()
):
  return await controller.subscription_controller_get_subscription_plan_clerk_id(clerk_id)