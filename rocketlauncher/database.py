import os
import glob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UniqueConstraint, Integer, String, Date, PickleType


Base = declarative_base()


class Rocket(Base):
    BASE_PATH = ''

    __tablename__ = 'rocket'
    __table__args = (
        UniqueConstraint('name', 'platform', name='unique_on_name_and_platform'),
    )

    id = Column(Integer, primary_key=True)
    rom = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    genres = Column(String, nullable=False)
    developper = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    players = Column(PickleType, nullable=False)
    releasedate = Column(Date, nullable=False)

    def __str__(self):
        return '<Rocket %s::%s>' % (self.platform, self.name)

    @property
    def path(self):
        print(Rocket.BASE_PATH)
        return os.path.join(Rocket.BASE_PATH, self.platform, self.name)

    @property
    def rom_path(self):
        return os.path.join(self.path, self.rom)

    @property
    def logo_path(self):
        return os.path.join(self.path, 'logo.png')

    @property
    def front_path(self):
        return os.path.join(self.path, 'front.jpg')

    @property
    def videos_path(self):
        return glob.glob(os.path.join(self.path, 'video*.gif'))

    @property
    def screenshots_path(self):
        return glob.glob(os.path.join(self.path, 'screenshot*.jpg'))
