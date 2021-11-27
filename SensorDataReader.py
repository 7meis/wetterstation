#!/usr/bin/env python3

import yaml
import paho.mqtt.client as mqtt
import time
import logging
from yaml.loader import SafeLoader



with open('./conf/SensorDataReader.yml') as f:
        conf = yaml.load(f, Loader=SafeLoader)
        logfile = conf['logfile']
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        logger = logging.getLogger('SensorDataReader')
        logger.debug("Config: %s", conf)



def readSensors(mqttc, mainTopic):
    for sensor in conf['sensors']:
        sensorEnabled = conf['sensors'][sensor]['enabled']
        sensorTopic = conf['sensors'][sensor]['topic']
        logger.info("Sensor: %s", sensor)
        logger.info("Sensor enabled: %s", sensorEnabled)
        logger.info("Sensor-Topic: %s", sensorTopic)
        if sensorEnabled:
            sensorModule = __import__(sensor)
            sensorData = sensorModule.getData()
            logger.debug("Sensor data: %s", sensorData)
            for metric, value in sensorData.items():
                logger.debug("Topic: %s", metric)
                logger.debug("Value: %s", value)
                topic = mainTopic + "/" + sensor + "/" + metric
                mqttc.publish(topic, value)


def mqttClient(host, port, keepalive):
    mqttc = mqtt.Client()
    mqttc.connect(str(host), int(port), int(keepalive))
    return mqttc


def main():
    logger.info('SensorDataReader started')
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