from dba.model import metadata
from dba.environment import build_engine


def create_datastore():
    """
    Create the tables needed for minimum functionality.
    """
    engine = build_engine()
    metadata.create_all(engine)


if __name__ == '__main__':
    create_datastore()
