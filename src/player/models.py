# from db import session
from db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # validates

from d2log import logger
from world import World
# from message.models import Message
# from person.models import Person
from game.parse import eorte
# from bprintf import buff
# from game.sigs import alon, aloff
from game.utils import set_name, PROGNAME


# from db import Message


MAX_PLAYERS = 16


MALE = 0
FEMALE = 1


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
    from_messages = relationship("Message", foreign_keys="Message.from_player_id", backref="Message.from_player")
    to_messages = relationship("Message", foreign_keys="Message.to_player_id", backref="Message.to_player")

    sexes = {
        'm': MALE,
        'f': FEMALE,
    }

    def __init__(self):
        Base.__init__(self)
        self.cms = -1
        self.rd_qd = 0
        self.mynum = 0
        self.iamon = False
        self.curch = 0
        self.lasup = 0
        self.user = None

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
        from db import sess
        return sess.query(Player)

    def loadw(self):
        w = World()
        return w

    def save(self, w):
        from db import sess
        w.closeworld()

        sess.add(self)
        sess.commit()

    @property
    def person(self):
        return self.user.person

    def update(self):
        logger.debug("---> update()")
        xp = self.cms - self.lasup
        if xp < 0:
            xp = -xp
        logger.debug("xp=%s", xp)
        if xp < 10:
            return

        w = self.loadw()
        self.position = self.cms
        self.lasup = self.cms

    def puton(self, user):
        logger.debug("---> puton({})".format(user))
        logger.debug('<!' + '-'*70)
        logger.debug(self)
        logger.debug("\t{{")
        logger.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
            self.lasup,
        ])
        logger.debug("\t}}")

        self.user = user
        self.iamon = False
        w = self.loadw()

        assert Player.fpbn(user.showname) is None, "You are already on the system - you may only be on once at a time"

        ct = Player.query().count()
        logger.debug("ct = %s", ct)
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

        logger.debug(self)
        logger.debug("\t{{")
        logger.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
            self.lasup,
        ])
        logger.debug("\t}}")
        logger.debug('-'*70 + '>')

    @staticmethod
    def fpbn(username):
        return None

    def rte(self):
        from db import findend
        from message.models import Message
        logger.debug("---> rte({})".format(self))
        logger.debug('<!' + '-'*70)
        logger.debug("\t{{")
        logger.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
            self.lasup,
        ])
        logger.debug("\t}}")

        w = self.loadw()
        assert w.filrf is not None, "AberMUD: FILE_ACCESS : Access failed"

        if self.cms == -1:
            self.cms = findend()

        ct = self.cms
        too = findend()
        logger.debug("%d : %d", self.cms, too)

        for ct in range(self.cms, too):
            block = Message.readmsg(ct)
            for m in block:
                logger.debug(m)
                m.mstoout(self)

        self.cms = ct
        self.update()
        eorte()

        # extern long vdes,tdes,rdes;
        rdes = 0
        tdes = 0
        vdes = 0

        logger.debug("\t{{")
        logger.debug(self)
        logger.debug([
            self.cms,
            self.curch,
            self.rd_qd,
            self.mynum,
            self.iamon,
            self.lasup,
        ])
        logger.debug("\t}}")
        logger.debug('-'*70 + '>')

    def player_load(self):
        logger.debug("---> special(\".g\", {})".format(self))
        from message.models import Message
        curmode = 1
        self.curch = -5
        self.initme()

        ufl = self.loadw()
        self.strength = self.person.strength
        self.level = self.person.level
        if self.person.level < 10000:
            self.visible = 0
        else:
            self.visible = 10000
        self.weapon = -1
        self.sex = self.person.sex
        self.helping = -1
        # us = cuserid()

        xy = "<s player=\"{}\">{}  has entered the game\n</s>".format(self.id, self.name)
        xx = "<s player=\"{}\">[ {}  has entered the game ]\n</s>".format(self.id, self.name)
        # sendsys(self.name, self.name, -10113, self.curch, xx)
        Message.send(self, self, -10113, self.curch, xx)

        self.rte()
        # if randperc() > 50:
        #     trapch(-5)
        # else:
        #     self.curch = -183
        #     trapch(-183)
        # sendsys(self.name, self.name, -10000, self.curch, xy)
        Message.send(self, self, -10000, self.curch, xx)

    def initme(self):
        from bprintf import buff
        if self.person is not None:
            return self.user.person

        buff.bprintf("Creating character....\n")
        p = self.user.new_person(self.name)
        while p.sex is None:
            buff.pbfr()
            # keysetback()
            s = input("\nSex (M/F) : ").lower()[0]
            # keysetup()
            p.sex = self.sexes.get(s)
            if p.sex is None:
                buff.bprintf("M or F")
        self.person.save()
        self.user.save()

    # ???
    def special(self, cmd):
        logger.debug("---> special({}, {})".format(cmd, self))
        pass
        # extern long curmode;
        # char ch,bk[128];
        # extern long curch,moni;
        # extern long mynum;
        # extern long my_str,my_lev,my_sco,my_sex;
        bk = cmd.lower()
        ch = bk[0]
        if ch != '.':
            return 0
        ch = bk[1]

        if ch == 'g':
            self.player_load()
        else:
            print("\nUnknown . option")
        return 1

    def prompt(self):
        from bprintf import buff
        prmpt = buff.get_prompt()
        # if debug_mode:
        #     prmpt = "#" + prmpt
        # if my_lev > 9:
        #     prmpt = "----" + prmpt
        if self.visible:
            prmpt = "({})".format(prmpt)

        prog = ''
        if self.visible > 9999:
            set_name(PROGNAME + "-csh")
        else:
            prog = "   --}----- ABERMUD -----{--     Playing as " + self.name.capitalize()

        if self.visible == 0:
            set_name(prog)
        return prmpt

    @staticmethod
    def revise(cutoff):
        from db import sess
        w = World()
        players = Player.query().filter(Player.c.name == '').filter(Player.c.position < cutoff / 2).filter(Player.c.position > 0).all()
        for p in players:
            mess = "{} has timed out\n".format(p.name)
            logger.debug(mess)
            # broad(mess)
            # dumpstuff(p.id, p.location)
            sess.delete(p)
        sess.commit()
