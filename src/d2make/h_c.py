import os
import socket


FSEG = {
    "UAF_RAND": "uaf.rand",
    "ROOMS": os.path.join("..", "data", "text", "ROOMS"),
    "LOG_FILE": "mud_syslog.log",
    "BAN_FILE": "banned_file",
    "NOLOGIN": os.path.join("..", "data", "nologin"),
    "RESET_T": "reset_t",
    "RESET_N": "reset_n",
    "RESET_DATA": "reset_data",
    "MOTD": os.path.join("..", "data", "text", "gmotd2"),
    "GWIZ": os.path.join("TEXT", "gwiz"),
    "HELP1": os.path.join("..", "data", "text", "help1"),
    "HELP2": os.path.join("..", "data", "text", "help2"),
    "HELP3": os.path.join("..", "data", "text", "help3"),
    "WIZLIST": os.path.join("..", "data", "text", "wiz.list"),
    "CREDITS": os.path.join("..", "data", "text", "credits"),
    "EXAMINES": os.path.join("..", "data", "examines"),
    "LEVELS": os.path.join("..", "data", "levels.txt"),
    # "PFL": os.path.join("..", "data", "user_file"),
    "PFT": "user_file.b",
    "EXE": "run_game.py",  # "EXE": "mud.exe",
    "EXE2": "run_mud.py",  # "EXE": "mud.1",
    "SNOOP": os.path.join("..", "data", "snoop"),
}


def main():
    res = packitems(os.getcwd())
    res["HOST_MACHINE"] = socket.gethostname()

    import config
    config.save(res)
    return res


def packitems(basedir):
    res = dict()
    for k, v in FSEG.items():
        res[k] = os.path.abspath(os.path.join(basedir, v))
    return res


if __name__ == "__main__":
    print(main())
