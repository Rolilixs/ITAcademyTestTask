from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Wallet(BaseModel):
    uuid: int
    balance: float


class Operation(str, Enum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"


class Transaction(BaseModel):
    wallet_uuid: int
    operation: Operation
    amount: float
    datetime: datetime


user_wallets = [
    Wallet(uuid=1, balance=1523.47),
    Wallet(uuid=2, balance=48765.91),
    Wallet(uuid=3, balance=932.15),
    Wallet(uuid=4, balance=25000.00),
    Wallet(uuid=5, balance=18745.39),
    Wallet(uuid=6, balance=456.80),
    Wallet(uuid=7, balance=9780.25),
    Wallet(uuid=8, balance=34567.42),
    Wallet(uuid=9, balance=789.99),
    Wallet(uuid=10, balance=12500.50),
    Wallet(uuid=11, balance=6400.10),
    Wallet(uuid=12, balance=998.75),
    Wallet(uuid=13, balance=21500.33),
    Wallet(uuid=14, balance=5000.00),
    Wallet(uuid=15, balance=745.65),
    Wallet(uuid=16, balance=18999.99),
    Wallet(uuid=17, balance=3200.40),
    Wallet(uuid=18, balance=99999.99),
    Wallet(uuid=19, balance=150.25),
    Wallet(uuid=20, balance=8450.80),
]
