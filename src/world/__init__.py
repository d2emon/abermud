class World:
    filrf = None

    def __init__(self):
        import logging
        logging.debug("--->\topenworld()")

        # extern long objinfo[],numobs,ublock[];
        if self.filrf is None:
            self.filrf = ["openlock", "/usr/tmp/-iy7AM", "r+"]
            assert self.filrf is not None, "Cannot find World file"
            # if self.filrf is None:
            #     crapup("Cannot find World file")

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
