from db.base import Base
from sqlalchemy import func, Column, Integer, String

from d2log import logger


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    from_player_id = None
    to_player_id = None
    code = None
    channel = None

    @staticmethod
    def query():
        from db import sess
        return sess.query(Message)

    def save(self):
        from db import sess
        sess.add(self)
        sess.commit()

    @staticmethod
    def findstart():
        from db import sess
        logger.debug("findstart()")
        # sec_read(unit,bk,0,1);
        # return(bk[0]);
        message_id = sess.query(func.min(Message.id)).scalar()
        if message_id is None:
            message_id = -1
        return message_id

    @staticmethod
    def findend():
        from db import sess
        logger.debug("findend()")
        # sec_read(unit,bk,0,2);
        # return(bk[1]);
        message_id = sess.query(func.max(Message.id)).scalar()
        if message_id is None:
            message_id = -1
        return message_id

    @staticmethod
    def readmsg(num):
        logger.debug("---> readmsg({})".format(num))
        logger.debug('<!' + '-'*60)
        # buff = sec_read(self, 0 ,64)
        # actnum = num * 2 - buff[0]
        # block = sec_read(self, actnum, 128)
        logger.debug('-'*60 + '>')
        return []

    def mstoout(self, user):
        '''
        Print appropriate stuff from data block
        '''
        logger.debug("---> mstoout({}, {})".format(self, user))
        logger.debug('<!' + '-'*60)
        # extern long debug_mode;
        luser = user.username.lower()
        # if debug_mode:
        #     buff.add("\n<{}>".format(block[1]))
        # if block[1] < -3:
        #     sysctrl(block, luser)
        # else:
        #     buff.bprintf(x)
        logger.debug('-'*60 + '>')

    @staticmethod
    def send(user_from, user_to, code, channel, text):
        logger.debug(["sendsys", [user_from.name, user_to.name, code, channel, text]])
