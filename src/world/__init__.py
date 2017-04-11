from game.utils import crapup


filrf = None


class World:
    def openworld(self):
        import logging
        logging.debug("--->\topenworld()")

        global filrf
        # extern long objinfo[],numobs,ublock[];
        if filrf is not None:
            return filrf

        filrf = ["openlock", "/usr/tmp/-iy7AM", "r+"]
        if filrf is None:
            crapup("Cannot find World file")

        # sec_read(filrf,objinfo,400,4*numobs)
        # sec_read(filrf,ublock,350,16*48)
        return filrf

    def closeworld(self):
        import logging
        logging.debug("--->\tcloseworld()")

        global filrf
        if filrf is None:
            return

        # sec_write(filrf,objinfo,400,4*numobs)
        # sec_write(filrf,ublock,350,16*48)

        # fcloselock(filrf)
        filrf = None
