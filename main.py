from fastapi import FastApi, Depends, HTTPException, status
from app.models.db.session import get_db, engine
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app_: FastApi):
    yield
    # shutdown
    engine.dispose()
app = FastApi()

