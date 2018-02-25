import pytest
from contextlib import closing
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session
from rocketlauncher.database import Base


@pytest.fixture(scope='function')
def connection():
    engine = create_engine('sqlite:///:memory:')
    connection = engine.connect()
    transaction = connection.begin()
    Base.metadata.create_all(connection)
    yield connection
    transaction.rollback()
    connection.close()
    engine.dispose()


@pytest.fixture(scope='function')
def session(connection):
    with closing(Session(connection)) as session:
        yield session
