import board
import digitalio
import time
from influxdb import InfluxDBClient, SeriesHelper
from adafruit_bme280 import basic as adafruit_bme280
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, cs)
client = InfluxDBClient('localhost', 8086, '', '', 'weather')


class MySeriesHelper(SeriesHelper):
    """Instantiate SeriesHelper to write points to the backend."""

    class Meta:
        """Meta class stores time series helper configuration."""

        # The client should be an instance of InfluxDBClient.
        client = client

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'weather.stats.{location}'

        # Defines all the fields in this time series.
        fields = ['temperature', 'humidity','pressure']

        # Defines all the tags for the series.
        tags = ['location']

        # Defines the number of data points to store prior to writing
        # on the wire.
        bulk_size = 5

        # autocommit must be set to True when using bulk_size
        autocommit = True




while True: 
        print("\nTemperature: %0.1f C" % bme280.temperature)
        print("Humidity: %0.1f %%" % bme280.humidity)
        print("Pressure: %0.1f hPa" % bme280.pressure)
        print("Altitude: %0.1f m" %  bme280.altitude)
        print("Relative Humidity: %0.1f RH%%" %  bme280.relative_humidity)
        MySeriesHelper(location='jaberg', temperature=bme280.temperature, humidity=bme280.humidity, pressure=bme280.pressure)
        time.sleep(10)
