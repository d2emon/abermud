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

        # extern long debug_mode;
        # extern long curch,moni,mynum;
        # extern long tty;
        # extern long my_lev;
        # extern long my_str;
        # extern long in_fight;
        # extern long fighting;
        # extern long curmode;
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

        return work.lower() == ".q"
        pass

    def bprintf(self, text):
        '''
        Max 240 chars/msg
        '''
        from game.utils import crapup
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

# void logcom()

# int pnotkb(str,ct,file)
# FILE *opensnoop(user,per)

# char sntn[32];

# void snoopcom()
# void viewsnoop()
# void chksnp()
# void setname(x)  /* Assign Him her etc according to who it is */


def makebfr():
    global buff
    buff = D2Buffer()
    return buff
