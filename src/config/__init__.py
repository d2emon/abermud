import os
import yaml


basedir = os.path.join(os.getcwd(), '..')
config_file = os.path.join(basedir, 'config', 'files.yml')
CONFIG = dict()
SERVER = "http://localhost:2000/abernode-server"


def load():
    global CONFIG
    data = None
    try:
        with open(config_file, "r") as f:
            data = yaml.load(f)
    except:
        data = dict()
    # print(data)
    CONFIG = data
    return data


def save(data):
    with open(config_file, "w") as f:
        yaml.dump(data, f, default_flow_style=False)


load()


if __name__ == "__main__":
    print(load())
