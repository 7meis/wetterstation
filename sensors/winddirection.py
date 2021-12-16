#!/usr/bin/env python3
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# initialize SPI BUS
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Chip-Set
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

# rsistor value list
resList = [33000, 6570, 8200, 891, 
           1000, 688, 2200, 1410,
           3900, 3140, 16000, 14120,
           120000, 42120, 64900, 21880]


def voltDivider(res1, res2, voltIn):
    """volt divider to calculate the out volts"""
    voltOut = (voltIn * res1) / (res1 + res2)
    return round(voltOut, 3)

# initialize variables
count = 0
values = []

# dictionary volts to wind direction in compass heading
voltList = {1.8: 'N',
            2.0: 'NNE',
            0.7: 'NE',
            0.8: 'ENE',
            0.1: 'E',
            0.3: 'ESE',
            0.2: 'SE',
            0.6: 'SSE',
            0.4: 'S',
            1.4: 'SSW',
            1.2: 'SW',
            2.8: 'WSW',
            2.7: 'W',
            2.9: 'WNW',
            2.2: 'NW',
            2.5: 'NNW'}



def getData():
    """gather sensor data and return it as dictionary"""
    wind = round(chan0.voltage, 1)
    if not wind in voltList:
        winddir = "unknown"
    else:
        winddir =  str(voltList[wind])
    
    return {
        "winddir": winddir
    }
    

