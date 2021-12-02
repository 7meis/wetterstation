#!/usr/bin/env python3
import board
from adafruit_bme280 import basic as adafruit_bme280


i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


def getData():
    return {
        "temperature": round(getTemperature(), 2),
        "humidity": round(getHumidity(), 2),
        "pressure": round(getPressure(), 1)
    }


def getTemperature():
    return bme280.temperature


def getHumidity():
    return bme280.humidity


def getPressure():
    return bme280.pressure


def getAltitude():
    return bme280.altitude

