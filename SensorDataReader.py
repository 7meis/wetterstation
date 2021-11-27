#!/usr/bin/env python3

import yaml
import paho.mqtt.client as mqtt
import time
from yaml.loader import SafeLoader

with open('./conf/SensorDataReader.yml') as f:
        conf = yaml.load(f, Loader=SafeLoader)
        print(conf)

def readSensors(mqttc, mainTopic):
    for sensor in conf['sensors']:
        sensorEnabled = conf['sensors'][sensor]['enabled']
        sensorTopic = conf['sensors'][sensor]['topic']
        print("Sensor: ", sensor)
        print("Sensor enabled: ", sensorEnabled)
        print("Sensor-Topic: ", sensorTopic)
        if sensorEnabled:
            sensorModule = __import__(sensor)
            sensorData = sensorModule.getData()
            print("Sensor data: ", sensorData)
            for metric, value in sensorData.items():
                print("Topic: ", metric)
                print("Value: ", value)
                topic = mainTopic + "/" + sensor + "/" + metric
                mqttc.publish(topic, value)


def mqttClient(host, port, keepalive):
    mqttc = mqtt.Client()
    mqttc.connect(str(host), int(port), int(keepalive))
    return mqttc


def main():
    mqttHost = conf['mqtt']['broker-host']
    mqttPort = conf['mqtt']['broker-port']
    mqttKeepalive = conf['mqtt']['keepalive']
    mqttc = mqttClient(mqttHost, mqttPort, mqttKeepalive)
    mainTopic = conf['mqtt']['main-topic']
    readInterval = conf['read-interval']
    while True:
        readSensors(mqttc, mainTopic)
        time.sleep(readInterval)


if __name__ == "__main__":
    main()