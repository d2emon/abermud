from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base


import db.base


# Base = declarative_base()
# engine = None
# sess = None
db_url = "sqlite:///../db/mud.db"
engine = create_engine(db_url)
db.base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
sess = Session()


import user.models
import player.models
import person.models
import message.models


def connect(echo=False):
    # global Base, engine, db_url
    global sess, engine

    if engine is None:
        engine = create_engine(db_url, echo=echo)

    db.base.Base.metadata.create_all(engine, checkfirst=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    sess = Session()

    return engine, sess


def session():
    global sess, engine
    if sess is None:
        engine, sess = connect()
    return sess


def findend():
    from message.models import Message
    return Message.findend()
