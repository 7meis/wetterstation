!#!usr/bin/env python3

import time
import plantower
import yaml
from yaml.loader import SafeLoader
from os.path import exists


confFile = "conf/pmsa003.yml"
if(exists(confFile)):
    with open(confFile, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
else:
    conf = {
        "port": "/dev/serial0"
    }

PMSA003 = PLANTOWER = plantower.Plantower(port=conf["port"])
PLANTOWER.set_to_sleep()

def getData():
    result = measure()
    return {
        "pm10_cf1": result[1],
        "pm25_cf1": result[2],
        "pm100_cf1": result[3],
        "pm10_std": result[4],
        "pm25_std": result[5],
        "pm100_std": result[6],
        "gr03um": result[7],
        "gr05um": result[8],
        "gr10um": result[9],
        "gr25um": result[10],
        "gr50um": result[11],
        "gr100um": result[12]
    }


def measure():
    PLANTOWER.set_to_wakeup()
    PLANTOWER.mode_change(plantower.PMS_PASSIVE_MODE)
    time.sleep(30)
    readout = PLANTOWER.read_in_passive()
    result = str(readout).split(",")
    PLANTOWER.set_to_sleep()
    return result



