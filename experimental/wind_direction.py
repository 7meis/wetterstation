import time
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

voltList = {2.4: 'N',
            1.3: 'NE',
            0.3: 'E',
            0.4: 'SE',
            0.8: 'S',
            1.8: 'SW',
            3.0: 'W',
            2.7: 'NW'}



while True:
    time.sleep(1)
    print("Value: ", chan0.value)
    print("Voltage: ", round(chan0.voltage,2))
    wind = round(chan0.voltage, 1)
    if not wind in voltList:
        print('unknown value ' + str(wind))
    else:
        print('found ' + str(wind) + ' ' + str(voltList[wind]))

