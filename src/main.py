from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.user import user_route
from src.connections.database import Database
from contextlib import asynccontextmanager
from src.connections.database import db, dbAlt
from src.modules.chatbot_domain import domain_route
from src.modules.chatroom import chatroom_route
from src.modules.subscription import subscription_route
from src.modules.chatbot_domain import domain_route

@asynccontextmanager
async def pool_lifespan(app: FastAPI):
  # startup
  await db.connect()
  app.state.db = db
  yield
  # shutdown
  await db.disconnect()

app = FastAPI(lifespan=pool_lifespan)

app.add_middleware(
  CORSMiddleware,
)

# enpoint to test if everyhting is working as expected
@app.get("/")
async def root():
  return {
    "status": "ok"
  }

@app.get("/ping")
async def ping():
  return {
    "ping_pool": await db.ping(),
    "ping_engine": await dbAlt.ping()
  }

app.include_router(user_route.router)
app.include_router(domain_route.router, prefix="/api/v1/domain", tags=["domain"])
app.include_router(chatroom_route.router) # prefix and tags initialized in router
app.include_router(subscription_route.router)
app.include_router(domain_route.router)