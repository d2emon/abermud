from d2log import mud_logger as logger
from mud.utils import validname
# from config import CONFIG
# import yaml
import socket
# from db import session
from db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
# from sqlalchemy.ext.declarative import declarative_base
# from models import Person


# Base = declarative_base()
# session = None
# engine = None


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)
    password = Column(String(16), nullable=False)
    person = relationship("Person", uselist=False, back_populates="user")

    def __init__(self, username=None, password=None):
        Base.__init__(self)
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        self.namegiv = False
        self.qnmrq = False
        self.isawiz = False

    def __repr__(self):
        return "<User '{}'\t[password: '{}']>".format(self.username, self.password)

    @validates('username')
    def validate_username(self, key, username):
        logger.debug("USERNAME %s", username)
        assert username is not None
        username = username.strip()
        assert username, "Empty username"
        assert '.' not in username, "Illegal characters in username"
        assert ' ' not in username, "Illegal characters in username"
        assert User.chkname(username), "Illegal characters in username"
        assert validname(username), "Bye Bye"
        return username

    @validates('password')
    def validate_password(self, key, password):
        assert password is not None
        assert password, "Empty password"
        assert '.' not in password, "Illegal characters in password"
        assert ' ' not in password, "Illegal characters in password"
        return password

    def check_password(self, password):
        assert password == self.password, "Wrong password"
        return True

    @staticmethod
    def query():
        from db import sess
        return sess.query(User)

    @staticmethod
    def host():
        return socket.gethostname()

    def save(self):
        from db import sess
        sess.add(self)
        sess.commit()

    @property
    def showname(self):
        username = self.username.capitalize()
        if username == "Phantom":
            return "The {}".format(username)
        return username

    @staticmethod
    def chkbnid(user):
        '''
        Check to see if UID in banned list
        '''
        c = user.lower()

        a = ""  # openlock(BAN_FILE,"r+");
        if a is None:
            return False
        b = ''
        for b in a:
            if b == '\n':
                b = ''
            b = b.lower()
            if b == user:
                raise Exception("I'm sorry- that userid has been banned from the Game")
        # fclose(a);
        return False

    @staticmethod
    def by_username(username):
        '''
        Return block data for user or -1 if not exist
        '''
        if username is None:
            return None

        # users = User.load()
        query = User.query()
        user = query.filter_by(username=username.lower()).first()
        if user is None:
            return user
        user.namegiv = False
        user.qnmrq = False
        user.ttyt = 0
        user.isawiz = user.id in [1, ]
        return user

    @staticmethod
    def chkname(username):
        import re
        return re.match("^\w*$", username)

    def new_person(self, name=None):
        from person.models import Person
        if name is None:
            name = self.showname

        self.person = Person()
        self.person.name = name
        self.person.score = 0
        self.person.strength = 40
        self.person.sex = None
        self.person.level = 1
        return self.person

    # @staticmethod
    # def load():
        # if f is None:
        #     raise Exception("No persona file")
        # with open(CONFIG["PFL"]) as f:
        #     # block = dcrypt(block)
        #     data = yaml.load(f)
        # return [User.from_dict(u) for u in data]

    # @staticmethod
    # def save(users):
        # data = [u.to_dict() for u in users]
        # if f is None:
        #     raise Exception("No persona file")
        # with open(CONFIG["PFL"], "w") as f:
        #     # block = dcrypt(block)
        #     yaml.dump(data, f)
