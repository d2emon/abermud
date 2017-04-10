from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = None
db_url = "sqlite:///db/gurps.db"


def connect(echo=False):
    # global Base, engine, db_url
    global engine

    if engine is None:
        engine = create_engine("sqlite:///../db/mud.db", echo=echo)

    Base.metadata.create_all(engine, checkfirst=True)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    return engine, Session()
