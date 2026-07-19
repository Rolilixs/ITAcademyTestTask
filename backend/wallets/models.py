import enum
from sqlalchemy import Column, DateTime, Double, Enum, ForeignKey, Integer, Numeric
from backend.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    uuid = Column(Integer, primary_key=True)
    balance = Column(Numeric(12, 2), nullable=False)


class Operation(str, enum.Enum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    operation = Column(Enum(Operation))
    amount = Column(Double)
    datetime = Column(DateTime)
    wallet_uuid = Column(Integer, ForeignKey("wallets.uuid"), nullable=False)
