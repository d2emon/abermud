# from db import session
from db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship  # validates
# from models import User

# from d2log import logger


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="person")
    name = Column(String(16), nullable=False)
    score = Column(Integer, default=0)
    strength = Column(Integer, default=40)
    sex = Column(Integer)
    level = Column(Integer, default=1)

    @staticmethod
    def query():
        from db import sess
        return sess.query(Person)

    def save(self):
        from db import sess
        sess.add(self)
        sess.commit()

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
