def main():
    OBJ = ["""
    blib.o gmain2.o gmainstubs.o gmlnk.o obdat.o flock.o
    """, ]
    
    INCL = [
        "object.h",
        "files.h",
        "System.h",
    ]
    
    
    res = {
        "mud.1": [
            OBJ,
            "strip mud.1",
            "chmod 4711 mud.1",
        ],
        "INCL": [
            INCL,
        ],
    }
    print(res)