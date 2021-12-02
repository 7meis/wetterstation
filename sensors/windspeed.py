#!/usr/bin/env python3
import time
from gpiozero import Button

wind_speed_sensor = Button(21)

windCount = 0

def spin():
    global windCount
    windCount = windCount + 1


wind_speed_sensor.when_pressed = spin

def getData():
    return {
        "windspeed": getWindspeed()
    }


def getWindspeed():
    global windCount
    windCount = 0
    time.sleep(1)
    currentWindspeed = round(windCount * 2.4, 1)
    windCount = 0
    return currentWindspeed





