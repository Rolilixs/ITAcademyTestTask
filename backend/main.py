import random
from contextlib import asynccontextmanager

import fastapi
from sqlalchemy import select

from backend.database import async_session_maker
from backend.wallets import api
from backend.wallets.models import Wallet

async def insert_fake_wallets(count: int = 20):
    async with async_session_maker() as session:
        # Проверяем наличие хотя бы одной записи
        stmt = select(Wallet).limit(1)
        result = await session.execute(stmt)
        existing = result.scalar_one_or_none()

        if existing is not None:
            return

        wallets = []
        for _ in range(count):
            balance = round(random.uniform(0, 10000), 2)
            wallets.append(Wallet(balance=balance))

        session.add_all(wallets)
        await session.commit()


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    await insert_fake_wallets()
    yield

app = fastapi.FastAPI(title="ITAcademy Test Task API", lifespan=lifespan)
app.include_router(api.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"text": "Тут пусто. Че нада? http://127.0.0.1:8000/docs"}
