from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = None
sess = None
db_url = "sqlite:///../db/mud.db"


def connect(echo=False):
    # global Base, engine, db_url
    global sess, engine

    if engine is None:
        engine = create_engine(db_url, echo=echo)

    Base.metadata.create_all(engine, checkfirst=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    sess = Session()

    return engine, sess


def session():
    global sess, engine
    if sess is None:
        engine, sess = connect()
    return sess
