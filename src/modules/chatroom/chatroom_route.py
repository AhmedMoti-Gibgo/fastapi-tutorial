from fastapi import APIRouter, Depends, HTTPException, Path
from src.modules.chatroom.chatroom_controller import ChatroomController
from src.modules.chatroom import chatroom_schema
from fastapi.responses import UJSONResponse

router = APIRouter(
    prefix="/api/v1/chatroom",
    tags=["chatroom"],
    default_response_class=UJSONResponse
)

@router.get("/")
async def chatroom_route_get_all_users(controller: ChatroomController = Depends()):
  return await controller.chatroom_controller_get_all_users()

@router.patch("/")
async def chatroom_service_update_chatroom_live(
    update_data: dict, 
    controller: ChatroomController = Depends()
):
  return await controller.chatroom_service_update_chatroom_live(update_data)

@router.patch("/live", response_model=chatroom_schema.UpdateChatroomLive_ResponseSchema)
async def chatroom_route_update_chatroom_live_state(
  update_data: chatroom_schema.UpdateChatroomLive_RequestSchema,
  controller: ChatroomController = Depends()
):
  return await controller.chatroom_controller_update_chatroom_live_state(
    update_data
  )

@router.patch("/live-toggle", response_model=chatroom_schema.ToggleChatRoomLive_ResponseSchema)
async def chatroom_route_toggle_live_state(
  update_data: chatroom_schema.ToggleChatroomLive_RequestSchema,
  controller: ChatroomController = Depends()
):
  return await controller.chatroom_controller_toggle_live_state(update_data)

@router.get("/{chatroom_id}/live", response_model=chatroom_schema.GetChatroomLive_Response)
async def chatroom_route_get_live_state(
  chatroom_id: str = Path(..., description="The ID of the chatroom to check"),
  controller: ChatroomController = Depends()
):
  return await controller.chatroom_controller_get_live_state(chatroom_id)