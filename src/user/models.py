from d2lib import cuserid
from mud.utils import cls, validname
from config import CONFIG
import yaml
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(16), nullable=False)
    password = Column(String(16), nullable=False)

    def __init__(self, username=None, password=None):
        Base.__init__(self)
        if username:
            self.username = username
        if password:
            self.password = password

    @validates('username')
    def validate_username(self, key, username):
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
        # Check for legality of names
        assert password is not None
        assert password, "Empty password"
        assert '.' not in password, "Illegal characters in password"
        assert ' ' not in password, "Illegal characters in password"
        return password

    def get_username(self, username):
        # Check for legality of names
        try:
            self.username = self.validate_username(self.id, username)
        except AssertionError as e:
            print("ASSERTION ERROR", e)
            return False

        a = User.logscan(self.username)
        if a is None:
            # If he/she doesnt exist
            a = input("\nDid I get the name right {} ?".format(self.username)).lower()
            c = a[0]
            print("\n")
            return c == 'y'
            # Check name
        return True

    def get_password(self, password):
        try:
            self.password = self.validate_password(self.id, password)
        except AssertionError as e:
            print("ASSERTION ERROR", e)
            return False
        return True

    def login(self):
        '''
        The whole login system is called from this
        '''
        # Check if banned first
        b = self.chkbnid(cuserid())
        # cuserid(NULL));
        print(b)

        namegiv = False
        username = None
        while not self.get_username(username):
            # Get the user name
            username = input("By what name shall I call you ?\n*")[:15]
            print("INPUT", username)
        self.logpass(self.username)  # Password checking

    def chkbnid(self, user):
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
    def logscan(username, session=None):
        '''
        Return block data for user or -1 if not exist
        '''
        # users = User.load()
        if session is None:
            import db
            engine, session = db.connect()
        query = session.query(User)
        users = query.all()
        for u in users:
            print(u.username, username)
            if u.username.lower() == username.lower():
                return u
        return None

    @staticmethod
    def logpass(username, session=None):
        '''
        Main login code
        '''
        user = User.logscan(username)
        if user:
            tries = 3
            while tries:
                # pastry:
                pwd = input("\nThis persona already exists, what is the password ?\n*")
                # fflush(stdout)
                # gepass(block)
                print("\n")

                if pwd == user.password:
                    return True

                tries -= 1
                if not tries:
                    raise Exception("\nNo!\n\n")
        else:
            # this bit registers the new user
            print("Creating new persona...\n")
            user = User(username)
            print("Give me a password for this persona\n")
            password = None
            while not user.get_password(password):
                # repass:
                password = input("*")
                # fflush(stdout)
                # gepass(block)
                print("\n")
            user.password = password

            if session is None:
                import db
                engine, session = db.connect()
            session.add(user)
            session.commit()
        cls()
        return True

    @staticmethod
    def chkname(username):
        import re
        return re.match("^\w*$", username)

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
