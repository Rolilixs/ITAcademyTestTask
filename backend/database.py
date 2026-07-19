from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from backend.config import settings


DATABASE_URL = settings.get_db_url()

async_engine = create_async_engine(url=DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
