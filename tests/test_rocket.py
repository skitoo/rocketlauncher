import pytest
from datetime import date
from rocketlauncher import rocket as rkt
from rocketlauncher.errors import LoadError


def test_load_rocket():
    rocket = rkt.load_rocket('samples/roms/nes/2048')
    assert rocket['rom'] == '2048 (tsone).nes'
    assert rocket['name'] == '2048'
    description = '2048 is an originally Smartphone Game. You must play with tile to add them pair '
    description += 'by pair to obtain 2048.'
    assert rocket['description'] == description
    assert rocket['platform'] == 'NES'
    assert rocket['genres'] == 'Puzzle-Game'
    assert rocket['developper'] == 'tsone'
    assert rocket['publisher'] == 'tsone'
    assert rocket['players'] == [1]
    assert rocket['releasedate'] == date(2014, 6, 21)


def test_load_rocket_fail_with_invalid_path():
    path = 'samples/roms/nes/Not present'
    with pytest.raises(LoadError) as err:
        rkt.load_rocket(path)
    assert '"%s/infos.yml" not found' % path == str(err.value)


def test_load_rocket_fail_with_invalid_infos_file():
    path = 'samples/roms/nes/Invalid'
    with pytest.raises(LoadError) as err:
        rkt.load_rocket(path)
    assert ('"%s/infos.yml" invalid: "name" attribute was not found' % path == str(err.value))
