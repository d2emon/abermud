from d2log import logger


buff = None


# int pfile(str,ct,file)
# int pndeaf(str,ct,file)
#  pcansee(str,ct,file)
# prname(str,ct,file)
# int pndark(str,ct,file)
# int tocontinue(str,ct,x,mx)
# int seeplayer(x)
# int ppndeaf(str,ct,file)
# int  ppnblind(str,ct,file)


class D2Buffer:
    prompt = {
        0: ">",
        1: "\"",
        2: "*",
    }

    prefix = {
        0: "",
        1: "say ",
        2: "tss ",
    }
    sysbuf = ''

    def __init__(self):
        '''
        4K of chars should be enough for worst case
        '''
        self.pr_due = False
        self.pr_qcr = None
        self.iskb = True

        self.snoopd = -1
        self.snoopt = -1

        self.log_fl = None
        # 0 = not logging

        self.convflg = 0
        self.brmode = 0
        self.cmdbuff = ""
        self.words = []
        self.wordbuff = ""
        self.stp = 0
        
        self.repl = {
            "it": "",
            "them": "",
            "him": "",
            "her": "",
            "there": "",
        }

    def __repr__(self):
        return "<D2Buffer \"\n{}\n\">".format(self.sysbuf)

    def get_prompt(self):
        return self.prompt.get(self.convflg, "?")

    def apply_conv(self, text):
        if not text:
            return text

        if text[0] == '*' and text != '*':
            return text[1:]
        return self.prefix.get(self.convflg, '') + text

    def key_input(self, prmpt):
        self.pbfr()
        self.pr_due = False

        from game.utils import PROGNAME
        print("PROGNAME:\t", PROGNAME)
        return input(prmpt)

    def sendmsg(self, player):
        logger.debug("---> sendmsg({})".format(self))

        # extern long in_fight;
        # extern long fighting;
        # l:
        while True:
            self.pbfr()
            # if tty == 4:
            #    btmscr()
            prmpt = player.prompt(self.get_prompt())
            self.pbfr()

            from game.sigs import alarm
            print("="*80)
            alarm.set_on()
            work = self.key_input(prmpt)
            alarm.set_off()
            print("="*80)

            # if tty==4:
            #     topscr()
            self.sysbuf += "<l>{}\n</l>".format(work)

            w = player.loadw()
            player.rte()
            player.save(w)

            if buff.convflg and work == "**":
                buff.convflg = 0
                continue

            work = buff.apply_conv(work)
            break
        # nadj:
        if player.curmode == 1:
            player.game(work)
        else:
            if work and work.lower() != ".q":
                a = player.special(work)
        # if fighting is not None:
        #    if fighting.username:
        #        in_fight = 0
        #        fighting = -1
        #    if fighting != self.curch:
        #        in_fight=0;
        #        fighting= -1;
        #    if in_fight:
        #        in_fight-=1

        return work.lower() == ".q"

    def bprintf(self, text):
        '''
        Max 240 chars/msg
        '''
        from game.utils import crapup
        text = str(text)
        if len(text) > 235:
            logger.info("Bprintf Short Buffer overflow")
            crapup("Internal Error in BPRINTF")

        # Now we have a string of chars expanded
        if (len(text) + len(self.sysbuf)) > 4095:
            self.sysbuf = ""
            # loseme()
            # logger.info("Buffer overflow on user %s", user)
            crapup("PANIC - Buffer overflow")
        self.sysbuf += text

    def pbfr(self):
        from game.sigs import alarm
        from game.share import player

        alarm.block()
        w = player.loadw()
        player.save(w)

        if self.sysbuf:
            self.pr_due = True
        if self.sysbuf and self.pr_qcr:
            print("")

        self.pr_qcr = 0

        if self.log_fl is not None:
            self.iskb = False
            self.dcprnt(self.log_fl)

        if self.snoopd != -1:
            fln = 1
            # fln = opensnoop(pname(snoopd),"a")
            if fln > 0:
                self.iskb = False
                self.dcprnt(fln)
                # fcloselock(fln)

        self.iskb = True
        self.dcprnt("stdout")
        # clear buffer
        self.sysbuf = ''
        if self.snoopt != -1:
            pass
            # viewsnoop()
        alarm.unblock()

    def dcprnt(self, output):
        logger.debug("dcprnt() to %s", output)
        print("-->{}<--".format(output))
        print(self.sysbuf)
        
    def getcmd(self):
        self.words = self.cmdbuff.split()
        self.stp = 0

    def nextword(self, repl):
        repl.update(self.repl)
        if self.stp >= len(self.words):
            return None
        
        self.wordbuff = self.words[self.stp]
        self.stp += 1
        
        word = self.wordbuff.lower()
        for k, v in repl.items():
            if word == k:
                word = v
                break
        return word
    
    def chkverb(self):
        return chklist(self.wordbuff, verbs)


# void logcom()

# int pnotkb(str,ct,file)
# FILE *opensnoop(user,per)

# char sntn[32];

# void snoopcom()
# void viewsnoop()
# void chksnp()
# void setname(x)  /* Assign Him her etc according to who it is */

verbs = {
    "go": 1,
    "climb": 1,
    "n": 2,
    "e": 3,
    "s": 4,
    "w": 5,
    "u": 6,
    "d": 7,
    "north": 2,
    "east": 3,
    "south": 4,
    "west": 5,
    "up": 6,
    "down": 7,
    "quit": 8,
    # "get","take","drop","look","i","inv","inventory","who",
    # 9,9,10,11,12,12,12,13,
    # "reset","zap","eat","drink","play",
    # 14,15,16,16,17,
    # "shout","say","tell","save","score"
    # 18,19,20,21,22,
    # ,"exorcise","give","steal","pinch","levels","help","value"
    # 23,24,25,25,26,27,28,
    # ,"stats","examine","read","delete","pass","password",
    # 29,30,30,31,32,32,
    # "summon","weapon","shoot","kill","hit","fire","launch","smash","break",
    # 33,34,35,35,35,35,35,35,35,
    # "laugh","cry","burp","fart","hiccup","grin","smile","wink","snigger"
    # 50,51,52,53,54,55,56,57,58,
    # ,"pose","set","pray","storm","rain","sun","snow","goto",
    # 59,60,61,62,63,64,65,66
    # "wear","remove","put","wave","blizzard","open","close",
    # ,100,101,102,103,104,105,106,    
    # "shut","lock","unlock","force","light","extinguish","where","turn",
    # 106,107,108,109,110,111,112,117,
    # "invisible","visible","pull","press","push","cripple","cure","dumb",
    # 114,115,117,117,117,118,119,120,
    # "change","missile","shock","fireball","translocate","blow",
    # 121,122,123,124,125,126,
    # "sigh","kiss","hug","slap","tickle","scream","bounce","wiz"
    # 127,128,129,130,131,132,133,134,
    # ,"stare","exits","crash","sing","grope","spray"
    # 135,136,137,138,139,140,
    # ,"groan","moan","directory","yawn","wizlist","in","smoke"
    # 141,142,143,144,145,146,147,
    # ,"deafen","resurrect","log","tss","rmedit","loc","squeeze","users"
    # 148,149,150,151,152,153,154,155,
    # ,"honeyboard","inumber","update","become","systat","converse"
    # 156,157,158,159,160,161,
    # ,"snoop","shell","raw","purr","cuddle","sulk","roll","credits"
    # 162,163,164,165,166,167,168,169,
    # ,"brief","debug","jump","wield","map","flee","bug","typo","pn"
    # 170,171,172,34,173,174,175,176,177,
    # ,"blind","patch","debugmode","pflags","frobnicate","strike"
    # 178,179,180,181,182,35,
    # ,"setin","setout","setmin","setmout","emote","dig","empty"
    # 183,184,185,186,187,188,189
}


def makebfr():
    global buff
    buff = D2Buffer()
    return buff


def chklist(word, verb):
    word = word.lower()
    # matches = [match(word, a) for a in keys]
    matches = dict()
    for a in verb.keys():
        matches[match(word, a)] = a
    max_match = max(matches.keys())
    if max_match < 5:
        return None
        # No good matches
    k = matches[max_match]
    return verb[k]


def match(word, verb):
    if not word:
        return 0
    if word == verb:
        return 10000
    if verb == "reset":
        return -1

    # c=0
    # for n in range(len(word)):
    #     if n >= len(verb):
    #         break
    #     if n == 0:
    #         c += 2
    #     if n == 1:
    #         c += 1
    #    c += 1
    # return c
    return 0