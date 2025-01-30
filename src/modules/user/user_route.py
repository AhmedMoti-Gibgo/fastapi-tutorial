from fastapi import APIRouter, Depends
from src.modules.user.user_controller import UserController
from fastapi.responses import ORJSONResponse
from src.modules.user import user_schema

router = APIRouter(default_response_class=ORJSONResponse)

# get all users
@router.get("/")
async def user_route_get_many_items():
  return await UserController.user_controller_get_many_items()

# get single user
@router.get("/{user_id}")
async def user_route_get_item(user_id: str):
  return await UserController.user_controller_get_item(user_id)

# get single user (by Clerk ID)
@router.get("/auth/{clerk_id}")
async def user_route_auth_login(clerk_id: str):
  return await UserController.user_controller_get_item_clerk_id(clerk_id)

# create user
@router.post("/")
async def user_route_create_item(user: user_schema.user_schema_CreateUser):
  return await UserController.user_controller_create_item(user)

# update user
@router.put("/{user_id}")
async def user_route_update_item(user_id: str, user: user_schema.user_schema_UpdateUser):
  return await UserController.user_controller_update_item(user_id, user)