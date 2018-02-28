import pytest
from rocketlauncher import config
from rocketlauncher.errors import LoadError


def test_load_config():
    conf = config.load('tests/fixtures/config.yml')
    assert conf == {
        'db_path': 'tests/fixtures/rocketlauncher.db',
        'rockets_path': 'tests/fixtures/roms',
        'themes_path': 'tests/fixtures/themes',
    }


def test_load_config_with_invalid_file():
    with pytest.raises(LoadError) as err:
        config.load('tests/fixtures/not_exist_config.yml')
    assert str(err.value) == '"tests/fixtures/not_exist_config.yml" not found'


def test_load_config_fail_when_db_path_was_not_found():
    with pytest.raises(LoadError) as err:
        config.load('tests/fixtures/invalid_config1.yml')
    assert str(err.value) == 'Config file has not "db_path" value'


def test_load_config_fail_when_rockets_path_was_not_found():
    with pytest.raises(LoadError) as err:
        config.load('tests/fixtures/invalid_config2.yml')
    assert str(err.value) == 'Config file has not "rockets_path" value'


def test_load_config_fail_when_themes_path_was_not_found():
    with pytest.raises(LoadError) as err:
        config.load('tests/fixtures/invalid_config3.yml')
    assert str(err.value) == 'Config file has not "themes_path" value'
