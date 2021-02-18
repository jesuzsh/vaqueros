from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey
)
#from dba.environment import build_engine

metadata = MetaData()

transaction = Table('transaction', metadata,
                    Column('transaction_id', Integer,
                           primary_key=True, autoincrement=True),
                    Column('transaction_name', String(30), nullable=False),
                    Column('amount_usd', Float, nullable=False),
                    Column('card_id', Integer,
                           ForeignKey('card.card_id'), nullable=False),
                    Column('category_id', Integer,
                           ForeignKey('category.category_id'), nullable=False)
                    )

card = Table('card', metadata,
             Column('card_id', Integer,
                    primary_key=True, autoincrement=True),
             Column('name', String(30), nullable=True),
             Column('owner', String(30))
             )

category = Table('category', metadata,
                 Column('category_id', Integer,
                        primary_key=True, autoincrement=True),
                 Column('name', String(30), nullable=False),
                 Column('is_essential', Boolean, nullable=False)
                 )

# metadata.create_all(build_engine())
