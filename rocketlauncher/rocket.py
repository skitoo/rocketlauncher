import os
import yaml
import tempfile
import zipfile
import shutil
from datetime import datetime
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from .errors import LoadError, InstallError
from .database import Rocket


MANDATORY_ATTRIBUTES = [
    'rom',
    'name',
    'description',
    'platform',
    'genres',
    'developper',
    'publisher',
    'players',
    'releasedate',
]

MANDATORY_FILES = [
    'front.jpg',
    'logo.png',
    'infos.yml',
]


def load_rocket(base_path):
    path = os.path.join(base_path, 'infos.yml')
    try:
        data = yaml.load(open(path, 'r'), Loader=Loader)
    except FileNotFoundError:
        raise LoadError('"%s" not found' % path)

    infos = data.keys()
    for attr in MANDATORY_ATTRIBUTES:
        if attr not in infos:
            raise LoadError(
                '"%s" invalid: "%s" attribute was not found' % (path, attr)
            )
    data = dict([(key, str(value)) for key, value in data.items()])
    data['players'] = list(map(int, data['players'].split('-')))
    data['releasedate'] = datetime.strptime(
        data['releasedate'], '%Y%m%dT%H%M%S'
    ).date()
    return data


def install(rocket_path, roms_path, db_session):
    with tempfile.TemporaryDirectory() as tmp_dir:
        zip_file = zipfile.ZipFile(rocket_path, 'r')
        zip_file.extractall(tmp_dir)
        zip_file.close()
        file_list = os.listdir(tmp_dir)
        for file_to_check in MANDATORY_FILES:
            _check_file(file_to_check, file_list)
        _check_video_and_screenshot(file_list)
        infos = load_rocket(os.path.join(tmp_dir))
        _check_file(infos['rom'], file_list)
        os.mkdir(os.path.join(roms_path, infos['platform']))
        dest_dir = os.path.join(roms_path, infos['platform'], infos['name'])
        os.mkdir(dest_dir)
        for file_name in file_list:
            shutil.copy(os.path.join(tmp_dir, file_name), dest_dir)
        return _save_rocket(infos, db_session)


def _save_rocket(infos, db_session):
    print('_save_rocket')
    rocket = Rocket(
        rom=infos['rom'],
        name=infos['name'],
        description=infos['description'],
        platform=infos['platform'],
        genres=infos['genres'],
        developper=infos['developper'],
        publisher=infos['publisher'],
        players=infos['players'],
        releasedate=infos['releasedate'],
    )
    db_session.add(rocket)
    return rocket


def _check_file(filename, file_list):
    if filename not in file_list:
        raise InstallError('This rocket has not "%s" file' % filename)


def _check_video_and_screenshot(file_list):
    if 'video1.gif' not in file_list and 'screeshot1.jpg' not in file_list:
        raise InstallError('This rocket has not video or screenshot file')
