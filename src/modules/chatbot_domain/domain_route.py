from fastapi import APIRouter, Depends
from src.modules.chatbot_domain.domain_controller import ChatbotDomainController
from fastapi.responses import ORJSONResponse
from src.modules.chatbot_domain import domain_schema

router = APIRouter(default_response_class=ORJSONResponse)

@router.get("/")
async def test_route():
  return {
    "message": "Route working"
  }

# get all user's domains
@router.get("/{user_id}")
async def domain_route_get_domains(user_id: str):
  return {
    "user_id": user_id
  }

# get all user's domains (with Clerk ID)
@router.get("/auth/{clerk_id}")
async def domain_route_get_domains_clerk_id(clerk_id: str):
  return await ChatbotDomainController.domain_controller_get_domains_clerk_id(clerk_id)