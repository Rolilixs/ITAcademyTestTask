import random
from backend.database import async_session_maker
from backend.wallets.models import Wallet


async def get_db():
    async with async_session_maker() as session:
        yield session


async def insert_fake_wallets(count: int = 20):
    async with async_session_maker() as session:
        wallets = []
        for _ in range(count):
            balance = round(random.uniform(0, 10000), 2)
            wallet = Wallet(balance=balance)
            wallets.append(wallet)

        session.add_all(wallets)
        await session.commit()