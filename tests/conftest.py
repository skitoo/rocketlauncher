import os
import shutil
import pytest
from contextlib import closing
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session
from rocketlauncher.database import Base
from rocketlauncher import rocket as rkt
from rocketlauncher import config as cfg


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


@pytest.fixture(scope='function')
def roms_path(request, config):
    def final():
        shutil.rmtree(config['rockets_path'])
    os.mkdir(config['rockets_path'])
    request.addfinalizer(final)
    return config['rockets_path']


@pytest.fixture(scope='session')
def config():
    return cfg.load('tests/fixtures/config.yml')


@pytest.fixture(scope='function')
def rocket(session, roms_path):
    yield rkt.install('tests/fixtures/2048.rocket', roms_path, session)
