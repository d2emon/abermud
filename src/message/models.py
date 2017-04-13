from db import session
from sqlalchemy import func, Column, Integer, String
# from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

from d2log import logger


Base = declarative_base()


class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    text = Column(String)

    @staticmethod
    def query():
        return session().query(Message)

    def save(self):
        session().add(self)
        session().commit()

    @staticmethod
    def findstart():
        logger.debug("--->\tfindstart()")
        # sec_read(unit,bk,0,1);
        # return(bk[0]);
        message_id = session().query(func.min(Message.id)).scalar()
        if message_id is None:
            message_id = -1
        return message_id

    @staticmethod
    def findend():
        logger.debug("--->\tfindend()")
        # sec_read(unit,bk,0,2);
        # return(bk[1]);
        message_id = session().query(func.max(Message.id)).scalar()
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
        #     buff.add("{}".format(x))
        logger.debug('-'*60 + '>')
