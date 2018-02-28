import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
from .errors import LoadError


MANDATORY_VALUES = [
    'db_path',
    'rockets_path',
    'themes_path',
]


def load(file_path):
    try:
        data = yaml.load(open(file_path, 'r'), Loader=Loader)
    except FileNotFoundError:
        raise LoadError('"%s" not found' % file_path)
    for value in MANDATORY_VALUES:
        if value not in data.keys():
            raise LoadError('Config file has not "%s" value' % value)
    return data
