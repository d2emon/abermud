from db import session
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base
from world import World
from message.models import Message
from game.parse import eorte
# from bprintf import buff
# from game.sigs import alon, aloff


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

    def save(self):
        session().add(self)
        session().commit()

    def update(self):
        import logging
        logging.debug("---> update()")
        xp = self.cms - self.lasup
        if xp < 0:
            xp = -xp
        logging.debug("xp=%s", xp)
        if xp < 10:
            return

        w = World()
        self.position = self.cms
        self.lasup = self.cms

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
            self.lasup,
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
            self.lasup,
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
            self.lasup,
        ])
        logging.debug("\t}}")

        w = World()
        assert w.filrf is not None, "AberMUD: FILE_ACCESS : Access failed"

        if self.cms == -1:
            self.cms = Message.findend()

        ct = self.cms
        too = Message.findend()
        logging.debug("%d : %d", self.cms, too)

        for ct in range(self.cms, too):
            block = Message.readmsg(ct)
            for m in block:
                logging.debug(m)
                m.mstoout(self)

        self.cms = ct
        self.update()
        eorte()

        # extern long vdes,tdes,rdes;
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
            self.lasup,
        ])
        logging.debug("\t}}")
        logging.debug('-'*70 + '>')

    def player_load(self):
        import logging
        logging.debug("---> special(\".g\", {})".format(self))
        curmode = 1
        self.curch = -5
        # initme()

        ufl = World()
        # self.strength = my_str
        # self.level = my_lev
        # if my_lev < 10000:
        #     self.visible = 0
        # else:
        #     self.visible = 10000
        # self.weapon = -1
        # self.sex = my_sex
        # self.helping = -1
        # us = cuserid()

        xy = "\001s{}\001{}  has entered the game\n\001".format(self.name, self.name)
        xx = "\001s{}\001[ {}  has entered the game ]\n\001".format(self.name, self.name)
        # sendsys(self.name, self.name, -10113, self.curch, xx)
        logging.debug(["sendsys", [self, self, -10113, self.curch, xx]])

        self.rte()
        # if randperc() > 50:
        #     trapch(-5)
        # else:
        #     self.curch = -183
        #     trapch(-183)
        # sendsys(self.name, self.name, -10000, self.curch, xy)
        logging.debug(["sendsys", [self, self, -10000, self.curch, xy]])

    # ???
    def special(self, cmd):
        import logging
        logging.debug("---> special({}, {})".format(cmd, self))
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

    def sendmsg(self):
        import logging
        logging.debug("---> sendmsg({})".format(self))

        import bprintf
        buff = bprintf.D2Buffer()

        pass
        # extern long debug_mode;
        # extern char *sysbuf;
        # extern long curch,moni,mynum;
        # char prmpt[32];
        # long a;
        # extern long tty;
        # char work[200];
        # long w2[35];
        # extern char key_buff[];
        # extern long convflg;
        convflg = ''
        # extern long my_lev;
        # extern long my_str;
        # extern long in_fight;
        # extern long fighting;
        # extern long curmode;
        # l:
        while True:
            buff.pbfr()
            # if tty == 4:
            #    btmscr()
            prmpt = "\n"
            if self.visible:
                prmpt += "("
            # if debug_mode:
            #     prmpt += "#"
            # if my_lev > 9:
            #     prmpt += "----"

            if convflg == 0:
                prmpt += ">"
            elif convflg == 1:
                prmpt += "\""
            elif convflg == 2:
                prmpt += "*"
            else:
                prmpt += "?"
            if self.visible:
                prmpt += ")"
            buff.pbfr()
            # if self.visible > 9999:
            #     set_progname(0,"-csh")
            # else:
            #     work = "   --}----- ABERMUD -----{--     Playing as {}".format(name)
            # if self.visible == 0:
            #     set_progname(0,work)

            # alon()
            # key_input(prmpt,80)
            print("PROMPT", prmpt)
            # aloff()

            work = ''  # key_buff
            # if tty==4:
            #     topscr()
            buff.sysbuf += "\001l"
            buff.sysbuf += work
            buff.sysbuf += "\n\001"

            w = World()
            self.rte()
            w.closeworld()
            if convflg and work != "**":
                convflg = 0
                continue
            if not work:
                break
            if work != "*" and work[0] == '*':
                work[0] = 32
                break
            if convflg:
                w2 = work
            if convflg == 1:
                work = "say {}".format(w2)
            else:
                work = "tss {}".format(w2)
            break
        # nadj:
        # if curmode==1:
        #     gamecom(work)
        # else:
        #    if work != ".Q" and work != ".q" and work:
        #         a = special(work, name)
        # if fighting is not None:
        #    if fighting.username:
        #        in_fight = 0
        #        fighting = -1
        #    if fighting != self.curch:
        #        in_fight=0;
        #        fighting= -1;
        #    if in_fight:
        #        in_fight-=1
        print("SYSBUF", buff.sysbuf)

        return not work == ".Q" or not work == ".q"
