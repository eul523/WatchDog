from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from dotenv import dotenv
from sqlalchemy.orm import DeclarativeBase

_ = dotenv.load_env()

db_url = f'postgresql://postgres:{POSTGRES_PASSWORD}@{POSTGRES_USER}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_async_engine(db_url)
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session