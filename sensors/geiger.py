#!/usr/bin/env python3
import time
import datetime
import RPi.GPIO as GPIO  
from collections import deque
GPIO.setmode(GPIO.BCM)

# set GPIO PIN 16 to input
GPIO.setup(16, GPIO.IN)

# initialize variables
count = deque()

# specify ratio fo J305 detection tube
j305_tube_ratio = 0.00812037037037

def geigerCount(channel):
    """count hits on sensor tube"""
    global count
    timestamp = datetime.datetime.now()
    count.append(timestamp)


#start event listener for geiger counter on fallng edge
GPIO.add_event_detect(16, GPIO.FALLING, callback=geigerCount) 


def getData():
    """gather sensor data and return ist as dictionary"""
    loop_count = 0
    # loop to count
    while loop_count < 10:
        try: 
            while count[0] < datetime.datetime.now() - datetime.timedelta(seconds=60):
                count.popleft()
            loop_count += 1
        except IndexError:
            # No count
            pass
    
    # if the loop count is 10 return the data dictonary
    if loop_count == 10:
        cpm = int(len(count))
        usvh = round(cpm * j305_tube_ratio, 6)
        print("Count: ", cpm)
        print("uSv/h: ", usvh)
        return {
            "count": cpm,
            "uSvh": usvh
        }
