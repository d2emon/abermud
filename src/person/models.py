from db import session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship  # validates
from sqlalchemy.ext.declarative import declarative_base

# from d2log import logger


Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user")
    name = Column(String(16), nullable=False)
    score = Column(Integer)
    strength = Column(Integer)
    sex = Column(Integer)
    level = Column(Integer)

    @staticmethod
    def query():
        return session().query(Person)

    def save(self):
        session().add(self)
        session().commit()

    @staticmethod
    def find(player):
        return Person.query().filter_by(name=player.name).first()


# extern char *oname();
# extern char *pname();

# delpers(name)

# saveme()
# validname(name)
# resword(name)
# getpersona(file,pers)
