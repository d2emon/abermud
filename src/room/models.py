from db.base import Base
from sqlalchemy import Column, Integer, Boolean, String, Unicode


class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Unicode)
    deathroom = Column(Boolean)
    nobr = Column(Boolean)

    def dark(self):
        if self.id == -1100 or self.id == -1101:
            return False
        if self.id in range(-1113, -1124):
            return True
        if self.id < -399 or self.id > -300:
            return False
        return True
    
    @staticmethod
    def open(self, n):
        import os.path
        from config import CONFIG
        from d2log import logger
        filename = os.path.join(CONFIG['ROOMS'], -n)
        logger.debug("openroom(%s)", filename)
        # x = fopen(blob, mod)
        return Room()