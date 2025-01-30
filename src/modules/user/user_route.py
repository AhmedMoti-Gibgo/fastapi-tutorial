from fastapi import APIRouter, Depends, HTTPException, Path
from src.modules.user.user_controller import UserController
from src.modules.user import user_schema
from fastapi.responses import UJSONResponse

router = APIRouter(
    prefix="/api/v1/user",
    tags=["chatroom"],
    default_response_class=UJSONResponse
)

# get single user (by Clerk ID)
@router.get("/auth/{clerk_id}")
async def user_route_auth_login(clerk_id: str):
  return {
    "message": "wire this up please"
  }

# create registered user (registered with Clerk)
@router.post("/create", response_model=user_schema.CreateRegisteredUser_ResponseSchema)
async def user_route_create_registered_user(
  create_data: user_schema.CreateRegisteredUser_RequestSchema,
  controller: UserController = Depends()
):
  return await controller.user_controller_create_registered_user(create_data)