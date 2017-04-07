from d2lib import cuserid
from mud.utils import cls, validname
from config import CONFIG
import yaml
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(16))
    password = Column(String(16))
    
    def validate_username(self):
        # Check for legality of names
        if not self.username:
            raise ValueError("Empty user name")

        if '.' in self.username:
            raise ValueError("Illegal characters in user name")

        username = self.username.strip()
        if ' ' in username:
            raise ValueError("Illegal characters in user name")

        if not User.chkname(username):
            raise ValueError("")

        if not validname(username):
            raise ValueError("Bye Bye")

        a = User.logscan(username)
        if a is None:
            # If he/she doesnt exist
            a = input("\nDid I get the name right {} ?".format(self.username)).lower()
            c = a[0]
            print("\n")
            return c == 'y'
            # Check name
        return True
    
    def validate_password(self):
        # Check for legality of names
        if not self.password:
            raise ValueError("Empty password")

        if '.' in self.password:
            raise ValueError("Illegal characters in password")
        return True
    
    def valid_username(self):
        try:
            return self.validate_username()
        except ValueError as e:
            print(e)
            return False
        
    def valid_password(self):
        try:
            return self.validate_password()
        except ValueError as e:
            print(e)
            return False
        
    def login(self):
        '''
        The whole login system is called from this
        '''
        # Check if banned first
        b = self.chkbnid(cuserid())  
        # cuserid(NULL));
        print(b)
    
        namegiv = False
        while not self.valid_username():
            # Get the user name
            self.username = input("By what name shall I call you ?\n*")[:15]
            print("INPUT", self.username)
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
    def logscan(username):
        '''
        Return block data for user or -1 if not exist
        '''
        users = User.load()
        for u in users:
            print(u.username, username)
            if u.username.lower() == username.lower():
                return u
        return None


    @staticmethod
    def logpass(username):
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
            while True:
                # repass:
                user.password = input("*")
                # fflush(stdout)
                # gepass(block)
                print("\n")
                if user.valid_password():
                    break
        
            persons = User.load()
            persons.append(user)
            persons.save()
        cls()
        return True

    @staticmethod
    def chkname(username):
        import re
        return re.match("^\w*$", username)
    
    @staticmethod
    def from_dict(data):
        return User(data.get('username', ''), data.get('password', ''))
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
        }
    
    @staticmethod
    def load():
        # unit = openlock(PFL,"r")
        # if unit is None:
        #     raise Exception("No persona file")
        with open(CONFIG["PFL"]) as f:
            # block = dcrypt(block)
            data = yaml.load(f)
        
        return [User.from_dict(u) for u in data]
    
    @staticmethod
    def save(users):
        data = [u.to_dict() for u in users]

        # unit = openlock(PFL,"a")
        # if unit is None:
        #     raise Exception("No persona file")
        with open(CONFIG["PFL"], "w") as f:
            # block = dcrypt(block)
            yaml.dump(data, f)