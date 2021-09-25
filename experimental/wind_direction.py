#!/usr/bin/env python3
import time
import board
import busio
import digitalio
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from influxdb import InfluxDBClient, SeriesHelper

# InfluxDB Client & Helper Class
client = InfluxDBClient('localhost', 8086, '', '', 'weather')

class WindDirectionHelper(SeriesHelper):
    class Meta:
        client = client
        series_name = 'weather.stats.{location}'
        fields = ['winddir']
        tags = ['location']
        bulk_size = 5
        autocommit = True



# initialize SPI BUS
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Chip-Set
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)


resList = [33000, 6570, 8200, 891, 
           1000, 688, 2200, 1410,
           3900, 3140, 16000, 14120,
           120000, 42120, 64900, 21880]


def voltDivider(res1, res2, voltIn):
    voltOut = (voltIn * res1) / (res1 + res2)
    return round(voltOut, 3)


for x in range(len(resList)):
    print(resList[x], voltDivider(10000, resList[x], 3.3))


#while True:
#    print(chan0.value)
#   print(chan0.voltage)
#    time.sleep(0.5)


count = 0
values = []
#voltList = {2.4: 0.0,
#            1.3: 45.0,
#            0.3: 90.0,
#            0.4: 135.0,
#            0.8: 180.0,
#            1.8: 225.0,
#            3.0: 270.0,
#            2.7: 315.0}

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



while True:
    time.sleep(1)
    #print("Value: ", chan0.value)
    #print("Voltage: ", round(chan0.voltage,1))
    wind = round(chan0.voltage, 1)
    if not wind in voltList:
        print('unknown value ' + str(wind))
    else:
        WindDirectionHelper(location='jaberg', winddir=str(voltList[wind]))
        print('found ' + str(wind) + ' ' + str(voltList[wind]))

