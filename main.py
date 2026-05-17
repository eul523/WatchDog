from fastapi import FastApi, Depends, HTTPException, status
from app.models.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession


app = FastApi()

