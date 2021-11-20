#!/usr/bin/env python3
import time
from influxdb import InfluxDBClient, SeriesHelper
from gpiozero import Button

wind_speed_sensor = Button(21)
wind_count = 0
client = InfluxDBClient('localhost', 8086, '', '', 'weather')

class WindSeriesHelper(SeriesHelper): 
    class Meta:
        client = client
        series_name = 'weather.stats.{location}'
        fields = ['windspeed']
        tags = ['location']
        bulk_size = 5
        autocommit = True

def spin():
    global wind_count
    wind_count = wind_count + 1
    #print("spin" + str(wind_count))

wind_speed_sensor.when_pressed = spin


while True:
  time.sleep(1)
  wind_kmh = wind_count*2.4
  #print("RPM is {0}".format(wind_count))
  print("Wind Speed:", wind_kmh)
  WindSeriesHelper(location='jaberg', windspeed=wind_kmh)
  wind_count = 0
