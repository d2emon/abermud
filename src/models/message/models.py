from db.base import Base
from sqlalchemy import func, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship  # validates

from d2log import logger


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    from_player_id = Column(Integer, ForeignKey('player.id'))
    to_player_id = Column(Integer, ForeignKey('player.id'))
    from_player = relationship("Player", foreign_keys=from_player_id, back_populates="from_messages")
    to_player = relationship("Player", foreign_keys=to_player_id, back_populates="to_messages")
    code = Column(Integer)
    channel = Column(Integer)
    text = Column(String)

    @staticmethod
    def query():
        from db import sess
        return sess.query(Message)

    def save(self):
        from db import sess
        sess.add(self)
        sess.commit()

        c = Message.query().count()
        if c >= 199:
            Message.cleanup(self.id)
            # longwthr()

    def __repr__(self):
        return "<Message#{}({}) '{}' to '{}' in {}: '{}'>".format(self.id, self.code, self.from_player.name, self.to_player.name, self.channel, self.text)

    @staticmethod
    def cleanup(mid_id):
        from db import sess
        from player.models import Player
        min_id = mid_id - 100
        Message.query().filter(Message.id < min_id).delete()
        sess.commit()
        Player.revise(mid_id)

    @staticmethod
    def findstart():
        from db import sess
        # logger.debug("findstart()")
        message_id = sess.query(func.min(Message.id)).scalar()
        if message_id is None:
            message_id = -1
        return message_id

    @staticmethod
    def findend():
        from db import sess
        # logger.debug("findend()")
        message_id = sess.query(func.max(Message.id)).scalar()
        if message_id is None:
            message_id = -1
        return message_id

    @staticmethod
    def readmsg(min_id):
        logger.debug("---> readmsg({})".format(min_id))
        return Message.query().filter(Message.id > min_id).all()

    def mstoout(self, player):
        '''
        Print appropriate stuff from data block
        '''
        from bprintf import buff
        logger.debug("mstoout({}, {})".format(self, player.id))
        if player.debug_mode:
            buff.bprintf("\n<{}>".format(self))
        if self.code < -3:
            # self.sysctrl(player)
            logger.debug("---> sysctrl({}, {})".format(self, player.name))
        else:
            buff.bprintf(str(self))

    @staticmethod
    def send(user_from, user_to, code, channel, text):
        logger.debug(["sendsys", [user_from.name, user_to.name, code, channel, text]])
        m = Message()
        m.from_player_id = user_from.id
        m.to_player_id = user_to.id
        m.code = code
        m.channel = channel
        # if code != -9900 and code != -10021:
        #     m.text = text
        # else:
        #     m.text = [
        #         i[0],
        #         i[1],
        #         i[2],
        #     ]
        m.text = text
        m.save()
