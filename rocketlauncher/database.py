from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UniqueConstraint, Integer, String, Date, PickleType

Base = declarative_base()


class Rocket(Base):
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
