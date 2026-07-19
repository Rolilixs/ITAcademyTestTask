import datetime
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, Field


class WalletResponse(BaseModel):
    uuid: int
    balance: float


class OperationType(str, Enum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"


class OperationRequest(BaseModel):
    operation_type: OperationType
    amount: Decimal = Field(gt=0, decimal_places=2)


class TransactionsResponse(BaseModel):
    id: int
    operation: OperationType
    amount: Decimal = Field(gt=0, decimal_places=2)
    datetime: datetime.datetime
    wallet_uuid: int
