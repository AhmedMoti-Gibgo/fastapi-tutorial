from fastapi import APIRouter, Depends
from src.modules.user.user_controller import UserController
from src.modules.user.user_schema import User, CreateUser, UpdateUser
from fastapi.responses import ORJSONResponse
import src.modules.user.user_schema as UserSchema

router = APIRouter(default_response_class=ORJSONResponse)

@router.get("/", response_model=list[User])
async def user_route_get_many_items():
  return await UserController.user_controller_get_many_items()

@router.get("/{user_id}", response_model=User)
async def user_route_get_item(user_id: str):
  return await UserController.user_controller_get_item(user_id)

@router.post("/", response_model=User)
async def user_route_create_item(user: CreateUser):
  return await UserController.user_controller_create_item(user)

@router.put("/{user_id}", response_model=User)
async def user_route_update_item(user_id: str, user: UpdateUser):
  return await UserController.user_controller_update_item(user_id, user)

async def clerk_get_current_user():
  # replace this with the actual Clerk authentication logic
  # this is a mock implementation
  return {
    "clerk_id": "12345"
  }

@router.post("/auth/login", response_model=UserSchema.ResponseSchema)
async def user_route_auth_login(current_user: dict = Depends(clerk_get_current_user)):
  return await UserController.user_service_on_login(current_user["clerk_id"])