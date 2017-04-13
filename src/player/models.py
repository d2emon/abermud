from db import session
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

from d2log import logger
from world import World
from message.models import Message
from game.parse import eorte
# from bprintf import buff
# from game.sigs import alon, aloff
from game.utils import set_name, PROGNAME


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
        self.lasup = 0

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

    def save(self, w):
        w.closeworld()

        session().add(self)
        session().commit()

    def update(self):
        logger.debug("---> update()")
        xp = self.cms - self.lasup
        if xp < 0:
            xp = -xp
        logger.debug("xp=%s", xp)
        if xp < 10:
            return

        w = World()
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

        self.iamon = False
        w = World()

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

        w = World()
        assert w.filrf is not None, "AberMUD: FILE_ACCESS : Access failed"

        if self.cms == -1:
            self.cms = Message.findend()

        ct = self.cms
        too = Message.findend()
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
        curmode = 1
        self.curch = -5
        self.initme()

        ufl = World()
        # self.strength = my_str
        # self.level = my_lev
        # if my_lev < 10000:
        #     self.visible = 0
        # else:
        #     self.visible = 10000
        self.weapon = -1
        # self.sex = my_sex
        self.helping = -1
        # us = cuserid()

        xy = "\001s{}\001{}  has entered the game\n\001".format(self.name, self.name)
        xx = "\001s{}\001[ {}  has entered the game ]\n\001".format(self.name, self.name)
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
        # PERSONA x;
        # chaar s[32];
        # extern char globme[];
        errno = 0
        # if findpers(self, x) !=-1:
        #     s, my_str, my_sco, my_lev, my_sex = decpers(x)
        #     return
        if errno != 0:
            crapup("Panic: Timeout event on user file")
        # x.p_score = 0
        buff.bprintf("Creating character....")
        my_sco = 0
        my_str = 40
        my_lev = 1
        # moan1:
        buff.bprintf("\nSex (M/F) : ")
        buff.pbfr()
        # keysetback()
        s = input()[:2]
        # keysetup()
        s = s.lower()
        if s[0] == 'm':
            my_sex = 0
        elif s[0] == 'f':
            my_sex = 1
        else:
            buff.bprintf("M or F")
            # goto moan1
        # x.p_name = self.name
	# x.p_strength = my_str
        # x.p_level = my_lev
        # x.p_sex = my_sex
        # x.p_score = my_sco
        # putpers(self, x)

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
