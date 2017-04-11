from game.utils import crapup


class World:
    filrf = None

    def __init__(self):
        import logging
        logging.debug("--->\topenworld()")

        # extern long objinfo[],numobs,ublock[];
        if self.filrf is None:
            self.filrf = ["openlock", "/usr/tmp/-iy7AM", "r+"]
            if self.filrf is None:
                crapup("Cannot find World file")

            # sec_read(filrf,objinfo,400,4*numobs)
            # sec_read(filrf,ublock,350,16*48)

    def closeworld(self):
        import logging
        logging.debug("--->\tcloseworld()")

        if self.filrf is not None:
            # sec_write(filrf,objinfo,400,4*numobs)
            # sec_write(filrf,ublock,350,16*48)

            # fcloselock(filrf)
            self.filrf = None

    def findstart(self):
        import logging
        logging.debug("--->\tfindstart({})".format(self))
        # sec_read(unit,bk,0,1);
        # return(bk[0]);
        return 0

    def findend(self):
        import logging
        logging.debug("--->\tfindend({})".format(self))
        # sec_read(unit,bk,0,2);
        # return(bk[1]);
        return 10

    def readmsg(self, num):
        import logging
        logging.debug("---> readmsg({}, {})".format(self, num))
        logging.debug('<!' + '-'*60)
        # buff = sec_read(self, 0 ,64)
        # actnum = num * 2 - buff[0]
        # block = sec_read(self, actnum, 128)
        logging.debug('-'*60 + '>')
        return []

    def mstoout(self, block, name):
        '''
        Print appropriate stuff from data block
        '''
        import logging
        logging.debug("---> mstoout({}, {}, {})".format(self, block, name))
        logging.debug('<!' + '-'*60)
        # extern long debug_mode;
        luser = name.lower()
        # if debug_mode:
        #     buff.add("\n<{}>".format(block[1]))
        # if block[1] < -3:
        #     sysctrl(block, luser)
        # else:
        #     buff.add("{}".format(x))
        logging.debug('-'*60 + '>')
