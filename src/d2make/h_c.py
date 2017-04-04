import os
import socket

    
FSEG = {
    "UAF_RAND": "uaf.rand",
    "ROOMS": os.path.join("TEXT", "ROOMS"),
    "LOG_FILE": "mud_syslog",
    "BAN_FILE": "banned_file",
    "NOLOGIN": "nologin",
    "RESET_T": "reset_t",
    "RESET_N": "reset_n",
    "RESET_DATA": "reset_data",
    "MOTD": os.path.join("TEXT", "gmotd2"),
    "GWIZ": os.path.join("TEXT", "gwiz"),
    "HELP1": os.path.join("TEXT", "help1"),
    "HELP2": os.path.join("TEXT", "help2"),
    "HELP3": os.path.join("TEXT", "help3"),
    "WIZLIST": os.path.join("TEXT", "wiz.list"),
    "CREDITS": os.path.join("TEXT", "credits"),
    "EXAMINES": "EXAMINES",
    "LEVELS": os.path.join("TEXT", "level.txt"),
    "PFL": "user_file",
    "PFT": "user_file.b",
    "EXE": "mud.exe",
    "EXE2": "mud.1",
    "SNOOP": "SNOOP",
}


def main():
    res = packitems(os.getcwd())
    res["HOST_MACHINE"] = socket.gethostname()
    return res


def packitems(ary):
    res = dict()
    for k, v in FSEG.items():
        res[k] = os.path.join(ary, v)
    return res


if __name__ == "__main__":
    print(main())