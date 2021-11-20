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

while True:
    print(chan0.value)
#   print(chan0.voltage)
    time.sleep(0.5)


def voltDivider(res1, res2, voltIn):
    voltOut = (voltIn * res1) / (res1 + res2)
    return round(voltOut, 3)
