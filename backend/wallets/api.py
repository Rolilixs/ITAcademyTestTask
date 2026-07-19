import fastapi
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.wallets.dependencies import get_db
from backend.wallets.schemas import OperationRequest, WalletResponse, TransactionsResponse
from backend.wallets.service import change_wallet_balance, get_wallet_balance, get_transactions, get_wallets


router = fastapi.APIRouter(prefix="/wallets", tags=["WALLETS"])


@router.post("/{wallet_uuid}/operation")
async def change_balance(
        wallet_uuid: int,
        operation: OperationRequest,
        session: AsyncSession = Depends(get_db)
) -> WalletResponse:
    """Изменение баланс кошелька с указанным UUID"""
    return await change_wallet_balance(session, wallet_uuid, operation)


@router.get("/{wallet_uuid}/")
async def get_balance(
        wallet_uuid: int,
        session: AsyncSession = Depends(get_db)
) -> WalletResponse:
    """
    Получение текущего баланса кошелька с указанным UUID
    """
    return await get_wallet_balance(session, wallet_uuid)


@router.get("/")
async def wallets(
        offset: int = 0,
        limit: int = 20,
        session: AsyncSession = Depends(get_db)
) -> list[WalletResponse]:
    """
    Получение информации о всех кошельках
    """
    # add a pagination later
    return await get_wallets(session)


@router.get("/transactions")
async def transactions(
        wallet_uuid: int | None = None,
        offset: int = 0,
        limit: int = 20,
        session: AsyncSession = Depends(get_db)
) -> list[TransactionsResponse]:
    """Все транзакции примененные к кошелькам. Можно получить все транзакции к определенному кошельку
    по его UUID, например: .../transactions?wallet_uuid=4 """
    # add a pagination later
    result = await get_transactions(session, wallet_uuid)
    return result
