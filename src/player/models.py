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
    location = Column(Integer, default=0)
    position = Column(Integer, default=-1)
    level = Column(Integer, default=1)
    visible = Column(Integer, default=0)
    strength = Column(Integer, default=-1)
    weapon = Column(Integer, default=-1)
    sex = Column(Integer, default=0)

    def __init__(self):
        Base.__init__(self)
        self.cms = -1
        self.rd_qd = 0
        self.mynum = 0
        self.iamon = False
        self.curch = 0

    def __repr__(self):
        return "<Player: '{}' {}>".format(self.name, {
            "loc": self.location,
            "pos": self.position,
            "lev": self.level,
            "vis": self.visible,
            "str": self.strength,
            "wpn": self.weapon,
            "sex": self.sex,
        })

    @staticmethod
    def query():
        return session().query(Player)

    def save(self):
        session().add(self)
        session().commit()

    def puton(self, user):
        import logging
        logging.debug("---> puton({})".format(user))
        logging.debug('<!' + '-'*70)
        logging.debug(self)
        logging.debug("\t{{")
        logging.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
        ])
        logging.debug("\t}}")

        self.iamon = False
        w = World()

        assert Player.fpbn(user.showname) is None, "You are already on the system - you may only be on once at a time"

        ct = Player.query().count()
        logging.debug("ct = %s", ct)
        if ct >= MAX_PLAYERS:
            self.mynum = MAX_PLAYERS
            return

        self.name = user.showname
        self.location = self.curch
        self.position = -1
        self.level = 1
        self.visible = 0
        self.strength = -1
        self.weapon = -1
        self.sex = 0
        # self.save()

        self.mynum = ct

        self.iamon = True

        logging.debug(self)
        logging.debug("\t{{")
        logging.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
        ])
        logging.debug("\t}}")
        logging.debug('-'*70 + '>')

    @staticmethod
    def fpbn(username):
        return None

    def rte(self):
        import logging
        logging.debug("---> rte({})".format(self))
        logging.debug('<!' + '-'*70)
        logging.debug("\t{{")
        logging.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
        ])
        logging.debug("\t}}")

        # extern long vdes,tdes,rdes;
        # extern long debug_mode;
        # long too,ct,block[128];

        w = World()
        assert w.filrf is not None, "AberMUD: FILE_ACCESS : Access failed"

        if self.cms == -1:
            cms = w.findend()

        too = w.findend()
        for ct in range(self.cms, too):
            # readmsg(unit, block, ct)
            # mstoout(block, name)
            pass

        self.cms = ct
        # update(name)
        # eorte()
        rdes = 0
        tdes = 0
        vdes = 0

        logging.debug("\t{{")
        logging.debug(self)
        logging.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
        ])
        logging.debug("\t}}")
        logging.debug('-'*70 + '>')
