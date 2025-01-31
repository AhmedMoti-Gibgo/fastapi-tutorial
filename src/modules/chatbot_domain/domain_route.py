from fastapi import APIRouter, Depends, Path
from fastapi.responses import UJSONResponse
from src.modules.chatbot_domain.domain_controller import ChatbotDomainController
from fastapi.responses import ORJSONResponse
from src.modules.chatbot_domain import domain_schema

router = APIRouter(
  prefix="/api/v1/domain",
  tags=[
    "domain", "chatbot-domain"
  ],
  default_response_class=UJSONResponse
)

@router.get("/{clerk_id}/domains", response_model=list[domain_schema.GetUserDomainsClerkID_ResponseSchema])
async def domain_route_get_user_domains_clerk_id(
  clerk_id: str = Path(..., description="Clerk ID for the user"),
  controller: ChatbotDomainController = Depends()
):
  return await controller.domain_controller_get_user_domains_clerk_id(clerk_id)