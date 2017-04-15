from db.base import Base
from sqlalchemy import Column, Integer, Boolean, String, Unicode


class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Unicode)
    deathroom = Column(Boolean)
    nobr = Column(Boolean)

    def is_dark(self):
        return True