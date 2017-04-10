# from game.utils import crapup

buff = None


# void bprintf(args,arg1,arg2,arg3,arg4,arg5,arg6,arg7)

# The main loop
# void dcprnt(str,file)
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
    def __init__(self):
        '''
        4K of chars should be enough for worst case
        '''
        self.sysbuf = ''
        self.pr_due = False
        self.pr_qcr = None
        self.iskb = True

        self.snoopd = -1
        self.snoopt = -1

        self.log_fl = None
        # 0 = not logging

    def pbfr(self):
        # block_alarm()
        # closeworld()
        if self.sysbuf:
            self.pr_due = True
        # if self.sysbuf and self.pr_qcr:
            # putchar('\n')
        self.pr_qcr = 0
        if self.log_fl is not None:
            self.iskb = False
            # dcprnt(self.sysbuf, self.log_fl)
        # if self.snoopd != -1:
        #    # fln = opensnoop(pname(snoopd),"a")
        #    # if fln > 0:
        #        # self.iskb = False
        #        # dcprnt(self.sysbuf, fln)
        #        # fcloselock(fln)
        self.iskb = True
        # dcprnt(self.sysbuf, stdout)
        self.sysbuf = ''
        # clear buffer
        # if self.snoopt != -1:
        #     # viewsnoop()
        # unblock_alarm();


# void logcom()

# void quprnt(x)
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
