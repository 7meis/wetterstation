#!/usr/bin/env python3
import time
from gpiozero import Button

# initialize wind sensor as button
wind_speed_sensor = Button(21)

# initialize wind count with 0
windCount = 0

def spin():
    """count spins"""
    global windCount
    windCount = windCount + 1


# every time the wheel makes a turn call spin
wind_speed_sensor.when_pressed = spin

def getData():
    """gather sensor data and return it as dictionary"""
    return {
        "windspeed": getWindspeed()
    }


def getWindspeed():
    """calculate windspeed in km/h"""
    global windCount
    windCount = 0
    time.sleep(1)
    currentWindspeed = round(windCount * 2.4, 1)
    windCount = 0
    return currentWindspeed





