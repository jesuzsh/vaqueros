from sqlalchemy import create_engine
import os


def build_engine():
    """
    SQLAlchemy calls the core interface to the database, Engine.
    """
    print("Building the SQLAlchemy engine.")

    filepath = os.path.dirname(os.path.realpath(__file__))
    db_path = filepath + '/../data/testy.db'

    print(db_path)
    return create_engine('sqlite:///' + db_path)
