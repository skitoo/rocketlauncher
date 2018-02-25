import os
import pytest
from rocketlauncher import rocket as rkt
from rocketlauncher.database import Rocket


@pytest.fixture(scope='function')
def rocket(session, roms_path):
    Rocket.BASE_PATH = roms_path
    yield rkt.install('samples/2048.rocket', roms_path, session)


def test_rocket_str_render(rocket):
    assert str(rocket) == '<Rocket nes::2048>'


def test_rocket_path(rocket, roms_path):
    assert rocket.path == os.path.join(roms_path, 'nes/2048')


def test_rocket_rom_path(rocket, roms_path):
    assert rocket.rom_path == os.path.join(roms_path, 'nes/2048/2048 (tsone).nes')


def test_rocket_logo_path(rocket, roms_path):
    assert rocket.logo_path == os.path.join(roms_path, 'nes/2048/logo.png')


def test_rocket_front_path(rocket, roms_path):
    assert rocket.front_path == os.path.join(roms_path, 'nes/2048/front.jpg')


def test_rocket_videos_path(rocket, roms_path):
    assert rocket.videos_path == [os.path.join(roms_path, 'nes/2048/video1.gif')]


def test_rocket_screenshots_path(rocket):
    assert rocket.screenshots_path == []
