import json

from os import mkdir

CHISEL_CONFIG_DIR      = ".chisel"
CHISEL_CONFIG_TEMP_DIR = ".chisel/tmp"
CHISEL_CONFIG_FILE     = ".chisel/config"

def _safe_create_config():
    try:
        f = open(CHISEL_CONFIG_FILE)
    except IOError:
        try:
            mkdir(CHISEL_CONFIG_DIR)
            mkdir(CHISEL_CONFIG_TEMP_DIR)
        except OSError:
            pass

        f = open(CHISEL_CONFIG_FILE, "a+")
        json.dump({}, f, indent=4)

def _get_config_object():
    _safe_create_config()

    f = open(CHISEL_CONFIG_FILE, "r")
    return json.load(f)
    return json.load(open(CHISEL_CONFIG_FILE, "r"))

def _save_config_object(obj):
    if not isinstance(obj, dict):
        return False
    else:
        _safe_create_config()
        f  = open(CHISEL_CONFIG_FILE, "rw+")
        f.seek(0)
        f.truncate()

        return json.dump(obj, f, indent=4)


if __name__ == '__main__':
    _safe_create_config()
