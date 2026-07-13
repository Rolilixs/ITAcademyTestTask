import fastapi
from .models import *

router = fastapi.APIRouter(prefix="/wallets", tags=["WALLETS"])


@router.get("/")
async def wallets(offset: int = 0, limit: int = 20):
    """

    :param offset:
    :param limit:
    :return:
    """
    # add a pagination later
    return user_wallets


@router.post("/{wallet_uuid}/operation")
async def change_balance(wallet_uuid: int, operation: Operation, amount: float):
    """

    :param wallet_uuid: wallet's User Unique Identification
    :param operation: WITHDRAW or DEPOSIT
    :param amount: increase or decrease value (Доллары или рубли?)
    :return:
    """
    for user_wallet in user_wallets:
        if user_wallet.uuid == wallet_uuid:
            if operation is Operation.withdraw:
                user_wallet.balance -= amount
                return user_wallet
            elif operation == Operation.deposit:
                user_wallet.balance += amount
                return user_wallet
    else:
        # If not found
        raise fastapi.HTTPException(404, f"Wallet with UUID {wallet_uuid} doesn't exist.")


@router.get("/{wallet_uuid}/")
async def get_balance(wallet_uuid: int):
    """

    :param wallet_uuid: wallet's User Unique Identification
    :return:
    """
    for user_wallet in user_wallets:
        if user_wallet.uuid == wallet_uuid:
            return user_wallet
    else:
        # If not found
        raise fastapi.HTTPException(404, f"Wallet with UUID {wallet_uuid} doesn't exist.")


@router.get("/transactions")
async def transactions(offset: int = 0, limit: int = 20):
    """

    :param offset:
    :param limit:
    :return:
    """
    # add a pagination later
    return {"message": "Here is history of all transactions!"}
