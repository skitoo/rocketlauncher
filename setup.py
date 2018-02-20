import rocketlauncher
import os
import sys
from setuptools import setup

if sys.version_info[0] < 3:
    sys.exit('Python < 3 is unsupported')

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name=rocketlauncher.__title__,
    version=rocketlauncher.__version__,
    description=rocketlauncher.__description__,
    long_description=open(os.path.join(here, 'README.md')).read(),
    author=rocketlauncher.__author__,
    author_email=rocketlauncher.__author_email__,
    url=rocketlauncher.__url__,
    license=rocketlauncher.__license__,
    packages=['rocketlauncher'],
    zip_safe=False,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'rocketlauncher = rocketlauncher.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)
