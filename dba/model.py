from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean

Base = declarative_base()


class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    amount_usd = Column(Float)
    card = Column(Integer)
    category = Column(Integer)

    def __repr__(self) -> str:
        return f"<Transaction(name='{self.name}', amount($)={self.amount_usd}, id={self.transaction_id})>"


class Card(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)

    def __repr__(self) -> str:
        return f"<Card(name='{self.name}', owner='{self.owner}', id={self.card_id}>"


class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    is_essential = Column(Boolean)

    def __repr__(self) -> str:
        return f"<Category(name='{self.name}',is_essential={self.is_essential}, id={self.category_id})>"
