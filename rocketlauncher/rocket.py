import os
import yaml
from datetime import datetime
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from .errors import LoadError


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
