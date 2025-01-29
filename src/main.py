from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.modules.user import user_route
from src.connections.database import db
from contextlib import asynccontextmanager
from src.connections.database import db, dbAlt

@asynccontextmanager
async def pool_lifespan(app: FastAPI):
  # startup
  await db.connect()
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

app.include_router(user_route.router, prefix="/api/v1/user", tags=["user"])