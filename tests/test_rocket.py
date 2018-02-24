import pytest
from datetime import date
import tempfile
import os
from rocketlauncher import rocket as rkt
from rocketlauncher.errors import LoadError, InstallError


def test_load_rocket():
    rocket = rkt.load_rocket('samples/roms/nes/2048')
    assert rocket['rom'] == '2048 (tsone).nes'
    assert rocket['name'] == '2048'
    description = '2048 is an originally Smartphone Game. You must play with tile to add them pair '
    description += 'by pair to obtain 2048.'
    assert rocket['description'] == description
    assert rocket['platform'] == 'nes'
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
    assert str(err.value) == '"%s/infos.yml" invalid: "name" attribute was not found' % path


def test_install_rocket_files():
    with tempfile.TemporaryDirectory() as tmp_dir:
        rkt.install('samples/2048.rocket', tmp_dir)
        assert os.path.exists(os.path.join(tmp_dir, 'nes', '2048', 'logo.png'))
        assert os.path.exists(os.path.join(tmp_dir, 'nes', '2048', 'front.jpg'))
        assert os.path.exists(os.path.join(tmp_dir, 'nes', '2048', 'video1.gif'))
        assert os.path.exists(os.path.join(tmp_dir, 'nes', '2048', '2048 (tsone).nes'))
        assert os.path.exists(os.path.join(tmp_dir, 'nes', '2048', 'infos.yml'))


def test_install_invalid_rocket_when_has_not_logo_file():
    with pytest.raises(InstallError) as err:
        with tempfile.TemporaryDirectory() as tmp_dir:
            rkt.install('samples/invalid1.rocket', tmp_dir)
    assert str(err.value) == 'This rocket has not "logo.png" file'


def test_install_invalid_rocket_when_has_not_front_file():
    with pytest.raises(InstallError) as err:
        with tempfile.TemporaryDirectory() as tmp_dir:
            rkt.install('samples/invalid2.rocket', tmp_dir)
    assert str(err.value) == 'This rocket has not "front.jpg" file'


def test_install_invalid_rocket_when_has_not_infos_file():
    with pytest.raises(InstallError) as err:
        with tempfile.TemporaryDirectory() as tmp_dir:
            rkt.install('samples/invalid3.rocket', tmp_dir)
    assert str(err.value) == 'This rocket has not "infos.yml" file'


def test_install_invalid_rocket_when_has_not_rom_file():
    with pytest.raises(InstallError) as err:
        with tempfile.TemporaryDirectory() as tmp_dir:
            rkt.install('samples/invalid4.rocket', tmp_dir)
    assert str(err.value) == 'This rocket has not "2048 (tsone).nes" file'


def test_install_invalid_rocket_when_has_not_video_and_screenshot_file():
    with pytest.raises(InstallError) as err:
        with tempfile.TemporaryDirectory() as tmp_dir:
            rkt.install('samples/invalid5.rocket', tmp_dir)
    assert str(err.value) == 'This rocket has not video or screenshot file'
