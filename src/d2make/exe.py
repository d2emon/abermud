def main():
    OBJ = ["""
    tk.o parse.o objsys.o extra.o magic.o blood.o weather.o obdat.o new1.o\
    support.o zones.o mobile.o bprintf.o bbc.o blib.o opensys.o gamego.o ndebug.o\
    key.o packer.o newuaf.o frob.o flock.o
    """, ]
    
    INCL = [
        "object.h",
        "files.h",
        "System.h",
    ]
    
    
    res = {
        "mud.1": [
            OBJ,
            "chmod 700 mud.exe",
        ],
        "INCL": [
            INCL,
        ],
    }
    print(res)