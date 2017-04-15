from db.base import Base
from sqlalchemy import Column, Integer, Boolean, String, Unicode


class Room(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Unicode)
    deathroom = Column(Boolean, default=False)
    nobr = Column(Boolean, default=False)
    ex_dat = dict()

    @property
    def dark(self):
        if self.id is None:
            return True
        if self.id == -1100 or self.id == -1101:
            return False
        if self.id in range(-1113, -1124):
            return True
        if self.id < -399 or self.id > -300:
            return False
        return True
    
    @staticmethod
    def open(room_id):
        import os.path
        from config import CONFIG
        from d2log import logger
        filename = os.path.join(CONFIG['ROOMS'], str(-room_id))
        logger.debug("openroom(%s)", filename)
        # x = fopen(blob, mod)
        room = None
        if room is None:
            room = Room()
            room.name = str(-room_id)
            room.description = "You are on channel {}\n".format(room_id)
        room.exits()
        return room
    
    def exits(self):
        for a in range(0, 6):
            self.ex_dat[a] = "fscanf(file, \"%ld\")"
        return self.ex_dat