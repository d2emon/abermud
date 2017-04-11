from db import session
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base


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
        import logging
        logging.debug("--->\tfindstart()")
        # sec_read(unit,bk,0,1);
        # return(bk[0]);
        return 0

    @staticmethod
    def findend():
        import logging
        logging.debug("--->\tfindend()")
        # sec_read(unit,bk,0,2);
        # return(bk[1]);
        return Message.query().count()

    @staticmethod
    def readmsg(num):
        import logging
        logging.debug("---> readmsg({})".format(num))
        logging.debug('<!' + '-'*60)
        # buff = sec_read(self, 0 ,64)
        # actnum = num * 2 - buff[0]
        # block = sec_read(self, actnum, 128)
        logging.debug('-'*60 + '>')
        return []

    def mstoout(self, user):
        '''
        Print appropriate stuff from data block
        '''
        import logging
        logging.debug("---> mstoout({}, {})".format(self, user))
        logging.debug('<!' + '-'*60)
        # extern long debug_mode;
        luser = user.username.lower()
        # if debug_mode:
        #     buff.add("\n<{}>".format(block[1]))
        # if block[1] < -3:
        #     sysctrl(block, luser)
        # else:
        #     buff.add("{}".format(x))
        logging.debug('-'*60 + '>')
