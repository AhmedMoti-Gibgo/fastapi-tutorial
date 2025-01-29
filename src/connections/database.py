from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator, Optional
from sqlalchemy import sql, text
import asyncpg
from fastapi import HTTPException

connection_string = "postgresql+asyncpg://postgres:password123@localhost:5432/fastapi-backend"

class Database:
  def __init__(self, db_connection_string: str):
    self.pool: Optional[asyncpg.pool.Pool] = None
    self.db_string = db_connection_string.replace("+asyncpg", "")

  async def connect(self):
    self.pool = await asyncpg.create_pool(dsn=str(self.db_string))

  async def disconnect(self):
    if self.pool:
      await self.pool.close()

  async def ping(self):
    if self.pool is None:
      return "Pool not initialized"
    async with self.pool.acquire() as connection:
      try:
        result = await connection.fetchval("SELECT 1")
        if result == 1:
          return "Pool connected successfully"
        # return "Pool connection failed"
      except Exception as error:
        return f"Pool connection failed: {error}"
      
  async def fetch(self, query, *args):
    async with self.pool.acquire() as connection:
      return await connection.fetch(query, *args)
    
  async def fetchrow(self, query, *args):
    async with self.pool.acquire() as connection:
      return await connection.fetchrow(query, *args)    
    
  async def execute(self, query, *args):
    async with self.pool.acquire() as connection:
      return await connection.execute(query, *args)
  
      
class DatabaseWithEngine:
  def __init__(self):
    self.engine = create_async_engine(connection_string, echo=True)
    self.async_session = sessionmaker(
      self.engine, class_=AsyncSession, expire_on_commit=False
    )
  
  async def ping(self):
    async with self.engine.connect() as connection:
      try: 
        result = await connection.execute(text("SELECT 1"))
        if result:
          return "Engine connected successfully"
        return "Engine ping unsuccessful"
      except Exception as error:
        return f"Engine connection failed"

db = Database(connection_string)
dbAlt = DatabaseWithEngine()