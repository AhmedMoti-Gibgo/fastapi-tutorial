from fastapi import APIRouter
from src.modules.user.user_controller import UserController
from src.modules.user.user_schema import User, CreateUser, UpdateUser
from fastapi.responses import ORJSONResponse

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
