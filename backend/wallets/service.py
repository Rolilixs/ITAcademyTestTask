import datetime
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from backend.wallets.models import Wallet, Transaction
from backend.wallets.schemas import OperationRequest, OperationType, WalletResponse


async def get_wallet_balance(session: AsyncSession, wallet_uuid: int | None = None):
    query = select(Wallet).where(Wallet.uuid == wallet_uuid)
    result = await session.execute(query)
    wallet = result.scalar_one_or_none()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    return WalletResponse(uuid=wallet.uuid, balance=wallet.balance)


async def change_wallet_balance(session: AsyncSession, wallet_uuid: int, operation: OperationRequest):
    query = select(Wallet).where(Wallet.uuid == wallet_uuid)
    result = await session.execute(query)
    wallet = result.scalar_one_or_none()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")

    if operation.operation_type == OperationType.withdraw:
        if wallet.balance < operation.amount:
            raise HTTPException(status_code=400, detail="The withdraw amount should be more than the balance")
        wallet.balance -= operation.amount
    else:
        wallet.balance += operation.amount

    transaction = Transaction(
        operation=operation.operation_type,
        amount=operation.amount,
        datetime=datetime.datetime.now(),
        wallet_uuid=wallet.uuid
    )

    session.add(transaction)
    await session.commit()
    return WalletResponse(uuid=wallet_uuid, balance=wallet.balance)


async def get_wallets(session: AsyncSession):
    result = await session.execute(select(Wallet))
    wallets = result.scalars().all()
    return wallets


async def get_transactions(session: AsyncSession, wallet_uuid: int | None):
    if wallet_uuid:
        query = select(Transaction).where(Transaction.wallet_uuid == wallet_uuid)
    else:
        query = select(Transaction)

    result = await session.execute(query)
    transaction = result.scalars().all()
    return transaction
