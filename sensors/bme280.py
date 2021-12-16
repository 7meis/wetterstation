#!/usr/bin/env python3
import board
from adafruit_bme280 import basic as adafruit_bme280

"""initialize I2C and bme280 sensor"""
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


def getData():
    """gather sensor data and return it as dictionary"""
    return {
        "temperature": round(getTemperature(), 2),
        "humidity": round(getHumidity(), 2),
        "pressure": round(getPressure(), 1)
    }


def getTemperature():
    """return temperature from bme280"""
    return bme280.temperature


def getHumidity():
    """return humidity from bme280"""
    return bme280.humidity


def getPressure():
    """return pressure from bme280"""
    return bme280.pressure


def getAltitude():
    """return altitude from bme280"""
    return bme280.altitude

