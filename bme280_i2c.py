#!/usr/bin/env python3
import yaml
import board
import digitalio
import time
import datetime
import paho.mqtt.client as mqtt
from yaml.loader import BaseLoader
from adafruit_bme280 import basic as adafruit_bme280


i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)


def mqttClient(host, port, keepalive):
    mqttc = mqtt.Client()
    client = mqttc.connect(str(host), int(port), int(keepalive))
    return client


def mqttPublish(client, topic, message):
    client.publish(topic, message)



if __name__ == "__main__":
    with open('./conf/bme280.yml') as f:
        conf = yaml.load(f, Loader=BaseLoader)
        print(conf)
        print(conf['mqttSettings']['mqttHost'])
        print(conf['mqttSettings']['mqttPort'])
        print(conf['mqttSettings']['mqttKeepalive'])
        mqttc = mqtt.Client()
        mqttc.connect(str(conf['mqttSettings']['mqttHost']), int(conf['mqttSettings']['mqttPort']), int(conf['mqttSettings']['mqttKeepalive']))
        while True:
            datetime.datetime.now()
            mqttc.publish(str(conf['bme380Settings']['mainTopic']) + "/" + str(conf['bme380Settings']['SubTopics'][0]), "datetime=" + str(datetime.datetime.now()) + ",location=" + str(conf['bme380Settings']['location']) + ",temperature=" + str(bme280.temperature))
            time.sleep(int(conf['bme380Settings']['interval']))




#while True: 
        #print("\nTemperature: %0.1f C" % bme280.temperature)
        #print("Humidity: %0.1f %%" % bme280.humidity)
        #print("Pressure: %0.1f hPa" % bme280.pressure)
        #print("Altitude: %0.1f m" %  bme280.altitude)
        #print("Relative Humidity: %0.1f RH%%" %  bme280.relative_humidity)
#        MySeriesHelper(location='jaberg', temperature=bme280.temperature, humidity=bme280.humidity, pressure=bme280.pressure)
#        time.sleep(10)
