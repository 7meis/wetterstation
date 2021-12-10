#!/usr/bin/env python3
import sys
from concurrent import futures
import yaml
import paho.mqtt.client as mqtt
import time
import logging
from yaml.loader import SafeLoader

sys.path.insert(0, './sensors')

with open('./conf/SensorDataReader.yml') as f:
        conf = yaml.load(f, Loader=SafeLoader)
        logfile = conf['logfile']
        logging.basicConfig(filename=logfile, level=logging.DEBUG)
        logger = logging.getLogger('SensorDataReader')
        logger.debug("Config: %s", conf)



def startSensors(mqttc, mainTopic):
    e = futures.ThreadPoolExecutor(max_workers=8)
    try:
        for sensor in conf['sensors']:
            logger.info("Start sensor: %s", sensor)
            e.submit(readSensor, mqttc, mainTopic, sensor)
    except KeyboardInterrupt:
        e.shutdown
        

def readSensor(mqttc, mainTopic, sensor):
    sensorEnabled = conf['sensors'][sensor]['enabled']
    sensorTopic = conf['sensors'][sensor]['topic']
    sensorPollIntervall = conf['sensors'][sensor]['poll-intervall']
    logger.info("Sensor: %s", sensor)
    logger.info("Sensor enabled: %s", sensorEnabled)
    logger.info("Sensor-Topic: %s", sensorTopic)
    if sensorEnabled:
        while True:
            sensorModule = __import__(sensor)
            sensorData = sensorModule.getData()
            logger.debug("Sensor data: %s", sensorData)
            for metric, value in sensorData.items():
                logger.debug("Topic: %s", metric)
                logger.debug("Value: %s", value)
                topic = mainTopic + "/" + sensorTopic + "/" + metric
                logger.debug("Full-Topic: %s", topic)
                mqttc.publish(topic, value)
            time.sleep(sensorPollIntervall)


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
    startSensors(mqttc, mainTopic)
    #while True:
        
    #time.sleep(readInterval)


if __name__ == "__main__":
    main()