from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


def build_engine():
    """
    SQLAlchemy calls the core interface to the database, Engine.

    :return: SQLAlchemy engine
    """
    filepath = os.path.dirname(os.path.realpath(__file__))
    db_path = filepath + '/../data/testy.db'

    return create_engine('sqlite:///' + db_path, echo=True, future=True)


def create_session():
    """
    A session is what is used to interact with the database a connection has
    been established. 

    :return: SQLAlchemy session
    """
    engine = build_engine()
    Session = sessionmaker(bind=engine)

    return Session()
