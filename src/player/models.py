from db import session
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
from world import World


Base = declarative_base()


MAX_PLAYERS = 16


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    location = Column(Integer, default=-1)
    position = Column(Integer, default=-1)
    level = Column(Integer, default=1)
    visible = Column(Integer, default=0)
    strength = Column(Integer, default=-1)
    weapon = Column(Integer, default=-1)
    sex = Column(Integer, default=0)

    name = ''
    cms = -1
    rd_qd = 0
    mynum = 0
    iamon = False

    @staticmethod
    def query():
        return session().query(Player)

    def puton(self, user):
        import logging
        logging.debug("---> puton({})".format(user))
        logging.debug([
            self,
            self.name,
            self.cms,
            self.rd_qd,
            self.mynum,
            self.iamon,
        ])

        self.iamon = False
        unit = World()
        unit.openworld()
        f = 0
        # if fpbn(user.username) != -1:
        #     crapup("You are already on the system - you may only be on once at a time")
        ct = Player.query().count()
        for ct in range(MAX_PLAYERS):
            # if pname(ct):
            #     f = 1
            pass
        if ct == MAX_PLAYERS:
            self.mynum = MAX_PLAYERS
            return
        # pname(ct) = name
        # setploc(ct,curch)
        # setppos(ct,-1)
        # setplev(ct,1)
        # setpvis(ct,0)
        # setpstr(ct,-1)
        # setpwpn(ct,-1)
        # setpsex(ct,0)
        self.mynum = ct
        self.iamon = True
