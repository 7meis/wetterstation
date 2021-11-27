#!/usr/bin/env python3

import yaml
import paho.mqtt.client as mqtt
import bme280_i2c
from yaml.loader import BaseLoader


with open('./conf/SensorDataReader.yml') as f:
    conf = yaml.load(f, Loader=BaseLoader)
    print(conf)

bme280 = bme280_i2c.BME280()
print(bme280.data)

