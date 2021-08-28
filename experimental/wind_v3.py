import time
from gpiozero import Button

wind_speed_sensor = Button(21)
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin" + str(wind_count))

wind_speed_sensor.when_pressed = spin


while True:
  time.sleep(1)
  wind_kmh = wind_count*2.4
  print("RPM is {0}".format(wind_count))
  print("Wind Speed:", wind_kmh)
  wind_count = 0
