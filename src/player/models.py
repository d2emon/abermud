# from db import session
from db.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship  # validates

from models import Room

from d2log import logger
from world import World
# from message.models import Message
# from person.models import Person
# from bprintf import buff
# from game.sigs import alon, aloff
from game.utils import set_name, PROGNAME, randperc
import cmd


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
        self.debug_mode = True
        self.curmode = 0
        
        self.blind = False
        self.ivct = 0
        self.cal = False

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

        self.user = user
        self.iamon = False
        w = self.loadw()

        assert Player.fpbn(user.showname) is None, "You are already on the system - you may only be on once at a time"

        ct = Player.query().count()
        logger.debug("ct = %s", ct)
        logger.debug("{} >= {}".format(ct, MAX_PLAYERS))
        if ct >= MAX_PLAYERS:
            self.mynum = MAX_PLAYERS
            # assert player.mynum < MAX_PLAYERS, "Sorry AberMUD is full at the moment"
            return

        self.name = user.showname
        self.location = self.curch
        self.position = -1
        self.level = 1
        self.visible = 0
        self.strength = -1
        self.weapon = -1
        self.sex = 0

        self.mynum = ct

        self.iamon = True
        logger.debug('-'*70 + '>')

    @staticmethod
    def fpbn(username):
        return None

    def rte(self):
        from db import findend
        from message.models import Message
        logger.debug("---> rte({})".format(self))
        logger.debug('<!' + '-'*70)

        w = self.loadw()

        if self.cms == -1:
            self.cms = findend()

        ct = self.cms
        block = Message.readmsg(self.cms)
        logger.debug(block)
        for m in block:
            ct = m.id
            logger.debug("#%d", ct)
            logger.debug(m)
            m.mstoout(self)
        logger.debug("%s:%s->%s", self.position, self.cms, ct)

        self.cms = ct
        self.update()
        self.eorte()

        # extern long vdes,tdes,rdes;
        rdes = 0
        tdes = 0
        vdes = 0

        logger.debug('-'*70 + '>')
        
    def eorte(self):
        logger.debug("---> eorte()")
        # extern long mynum,me_ivct;
        # extern long me_drunk;
        # extern long ail_dumb;
        # extern long curch,tdes,rdes,vdes,ades;
        # extern long me_cal;
        # extern long wpnheld;
        # extern long my_str;
        # extern long i_setup;
        # extern long interrupt;
        # extern long fighting,in_fight;
    
        # ctm = time()
        # if ctm - last_io_interrupt > 2:
        #    interrupt = 1
    
        # if interrupt:
        #     last_io_interrupt = ctm
    
        if self.ivct:
            self.ivct -= 1
        
        if self.ivct == 1:
            self.visible = 0
    
        if self.cal:
            self.cal = False
            # calibme()
    
        # if tdes:
        #     dosumm(ades)
    
        # if in_fight:
        #     if ploc(fighting) != curch:
        #         fighting = -1
        #         in_fight = 0
        #     if not strlen(pname(fighting)):
        #         fighting = -1
        #         in_fight = 0
        #     if in_fight:
        #         if interrupt:
        #             in_fight = 0
        #             hitplayer(fighting, wpnheld)
    
        # if self.iswornby(18) or randperc() < 10:
        #     my_str += 1
        #     if i_setup:
        #         calibme()
    
        # forchk()
    
        # if me_drunk > 0:
        #     me_drunk -= 1
        #     if not ail_dumb:
        #         gamecom("hiccup")
    
        # interrupt = 0

    def player_load(self):
        logger.debug("---> special(\".g\", {})".format(self))
        from message.models import Message
        self.curmode = 1
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

        xy = "<s player=\"{}\">{}  has entered the game\n</s>".format(self.id, self.name)
        xx = "<s player=\"{}\">[ {}  has entered the game ]\n</s>".format(self.id, self.name)
        Message.send(self, self, -10113, self.curch, xx)

        self.rte()
        if randperc() < 50:
            self.curch = -183
        self.goto_channel(self.curch)

        Message.send(self, self, -10000, self.curch, xy)

    def initme(self):
        from bprintf import buff
        if self.person is not None:
            return self.person

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
        return self.person

    # ???
    def special(self, cmd):
        logger.debug("---> special({}, {})".format(cmd, self))
        bk = cmd.lower()
        if bk[0] != '.':
            return 0
        if bk[1] == 'g':
            self.player_load()
        else:
            print("\nUnknown . option")
        return 1

    def prompt(self, prmpt):
        if self.debug_mode:
            prmpt = "#" + prmpt
        if self.person.level > 9:
            prmpt = "----" + prmpt
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

    def goto_channel(self, channel):
        w = self.loadw()
        self.location = channel
        self.look(channel)

    def look(self, room_id):
        from bprintf import buff
        logger.debug("lookin(%d)", room_id)
        dead = False
        w = self.loadw()
        self.save(w)
        if self.blind:
            buff.bprintf("You are blind... you can't see a thing!\n")
        if self.person.level > 9:
            logger.debug("showname(%d)", room_id)
        room = Room.open(room_id)
        if self.is_dark(room):
            buff.bprintf("It is dark\n")
            w = self.loadw()
            self.onlook()
            return
        if room.deathroom:
            self.blind = False
            if self.person.level > 9:
                buff.bprintf("<DEATH ROOM>\n")
            else:
                dead = True
        if room.nobr:
            buff.brmode = 0
        if not self.blind and buff.brmode == 0:
            buff.bprintf(room.description)
        if dead:
            # self.loseme()
            # crapup("bye bye.....\n")
            pass
        w = self.loadw()
        if not self.blind:
            pass
        #     lisobs()
            if self.curmode == 1:
                pass
                # lispeople()
        buff.bprintf("\n")
        self.onlook()
        
    def onlook(self):
        # fpbns("shazareth").chkfight()
        # if not self.iscarrby(45):
        #     fpbns("wraith").chkfight()
        # fpbns("bomber").chkfight()
        # fpbns("owin").chkfight()
        # fpbns("glowin").chkfight()
        # fpbns("smythe").chkfight()
        # fpbns("dio").chkfight()
        # if not self.iscarrby(45):
        #     fpbns("zombie").chkfight()
        # fpbns( "rat" ) ).chkfight()
        # fpbns( "ghoul" ) ).chkfight()
        # fpbns( "ogre" ) ).chkfight()
        # fpbns( "riatha" ) ).chkfight()
        # fpbns( "yeti" ) ).chkfight()
        # fpbns( "guardian")).chkfight()
        # if self.iscarrby(32):
        #     dorune()
        # if self.helping != -1:
        #     helpchkr()
        pass

    def is_dark(self, room):
        if self.person.level > 9:
            return False
        if not room.dark:
            return False
        # for c in range(0, numobs):
        #    if c != 32 and otstbit(c, 13) == 0:
        #        continue
        #    if ishere(c)
        #        return False
        #    if ocarrf(c) == 0 or ocarrf(c) == 3:
        #        continue
        #    if oloc(c).location != self.location:
        #        continue
        #    return False                
        return False
    
    def game(self, cmd):
        from bprintf import buff
        logger.debug("GAMEGO")
        # extern long in_fight;
        # extern long stp;
        # extern char strbuf[];
        if cmd == ".q":
            cmd = ""
            # Otherwise drops out after command
        if not cmd:
            return 0
        if cmd == "!":
            cmd = buff.cmdbuf
        else:
            buff.cmdbuf = cmd
        stp = 0
        # if brkword() == -1:
        #     buff.bprintf("Pardon ?\n")
        #     return -1
        a = -1
        # a = chkverb()
        if a == -1:
            buff.bprintf("I don't know that verb\n")
            return -1
        # doaction(a)
        return 0