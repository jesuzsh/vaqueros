from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


def build_engine():
    """
    SQLAlchemy calls the core interface to the database, Engine.

    :return: SQLAlchemy engine
    """
    print("Building the SQLAlchemy engine.")

    filepath = os.path.dirname(os.path.realpath(__file__))
    db_path = filepath + '/../data/testy.db'

    print(db_path)
    return create_engine('sqlite:///' + db_path)

def create_session():
    """
    A session is what is used to interact with the database a connection has
    been established. 

    :return: SQLAlchemy session
    """
    engine = build_engine()
    Session = sessionmaker(bind=engine)
    
    return Session()
